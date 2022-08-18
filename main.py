from http.client import HTTPException
import imp
from re import A
from turtle import title
from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from models import Movie, genre, updateMovie
import requests

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
async def get_movielist():
    return movielist

@app.post("/myApp/path")
async def new_movie(movie: Movie):
    movielist.append(movie)
    return {"id": movie.id}

@app.delete("/myApp/path/{movie_id}")
async def del_movie(movie_id: UUID):
    for movie in movielist:
        if movie.id == movie_id: 
            movielist.remove(movie)
            return
    raise HTTPException(
        status_code= 404, 
        detail= f"Movie was not found"
    )

@app.put("/myApp/path/{movie_id}")
async def update_movie(movie_update: updateMovie, movie_id: UUID):
    for movie in movielist:
        if movie.id == movie_id:
            if movie_update.title is not None:
                movie.title = movie_update.title
            if movie_update.director is not None:
                movie.director = movie_update.director
            if movie_update.movie_genre is not None:
                movie.movie_genre = movie_update.movie_genre
            if movie_update.age_rating is not None:
                movie.age_rating = movie_update.age_rating
            return
    raise HTTPException(
        status_code=404,
        detail= f"Movie was not found"
    )
                

@app.get("/")
def test():
    return{"Hi : Uchenna"} 