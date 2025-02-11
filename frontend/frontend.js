import { useState, useEffect } from "react";

function App() {
  const [song, setSong] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/random-song")
      .then(response => response.json())
      .then(data => setSong(data));
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Songguessr</h1>
      {song ? (
        <>
          <h2>{song.title} by {song.artist}</h2>
          {song.preview_url && <audio controls src={song.preview_url}></audio>}
        </>
      ) : (
        <p>Loading song</p>
      )}
    </div>
  );
}

export default App;
