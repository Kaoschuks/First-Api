from fastapi import FastAPI
from typing import List
from uuid import uuid4
from models import Movie, genre

app = FastAPI()

movielist: List[Movie] = [
    Movie(
        title= 'The Unholy',
        director= 'Evan Spiliopoulos',
        movie_genre= genre.horror,
        age_rating= 16,
        id= uuid4()
    ),    
    Movie(
        title= 'Infinity Wars',
        director= 'Anthony Russo, Joe Russo',
        movie_genre= genre.action,
        age_rating= 13,
        id= uuid4()
    ), 
    Movie(
        title= 'Uncharted',
        director= 'Ruben Fleischer',
        movie_genre= genre.adventure,
        age_rating= 13,
        id= uuid4()
    )
]

@app.get("/myApp/path")
async def test2():
    return movielist

@app.get("/")
def test():
    return{"Hi : Uchenna"}