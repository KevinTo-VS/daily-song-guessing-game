# Daily Song Guessing Game

# Requirements

- Operating System:
- macOS 15+ / Windows 10+
- Python Version: 3.10.6+
  
Dependencies: 
-FastAPI
- Uvicorn
- Requests

# Installation and Running Project:

1. Clone the Repository
- git clone https://github.com/KevinTo-VS/daily-song-guessing-game.git

2. Install Python
- You can install Python from https://www.python.org/downloads/
- You can check if you have Python installed with putting in "python --version" in your terminal.

3. Open the project in an IDE and open a terminal

4. Install the required dependencies
- pip install fastapi requests uvicorn

5. Run the FastAPI server using the following command
- uvicorn backend.main:app --reload

6. Test the API
- Open browser and go to http://127.0.0.1:8000/random-song
