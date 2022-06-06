from fastapi import FastAPI
import uvicorn
import pandas as pd

songs = pd.read_csv('songs.csv')

app = FastAPI()

@app.get('/songs')
def index():
	return list(songs['title'])

@app.get('/ping')
def ping():
	return 'pong'

@app.get('/artist/{anArtist}')
def getSongsFrom(anArtist):
	return list(songs[songs['artist'] == anArtist]['title'])

@app.get('/song/{aSongTitle}')
def getDescriptionOf(aSongTitle):
	return list(songs[songs['title'] == aSongTitle]['description'])

# localhost
# if __name__ == '__main__':
# 	uvicorn.run(app, port=8000)
