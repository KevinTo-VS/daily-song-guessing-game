from fastapi import FastAPI
import requests
import base64

app = FastAPI()


CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"

def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    auth_data = {"grant_type": "client_credentials"}
    
    response = requests.post(auth_url, headers=auth_headers, data=auth_data)
    token = response.json().get("access_token")
    
    return token

@app.get("/random-song")
def get_random_song():
    token = get_spotify_token()  
    headers = {"Authorization": f"Bearer {token}"}
    params = {"seed_genres": "pop", "limit": 1}

    SPOTIFY_API_URL = "https://api.spotify.com/v1/recommendations"
    response = requests.get(SPOTIFY_API_URL, headers=headers, params=params)
    data = response.json()

    if "tracks" in data and data["tracks"]:
        song = data["tracks"][0]
        return {
            "title": song["name"],
            "artist": song["artists"][0]["name"],
            "preview_url": song["preview_url"]
        }
    
    return {"error": "No song found"}
