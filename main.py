from http.client import HTTPException
import imp
from turtle import title
from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from models.movie_models import Movie, genre, updateMovie
import requests

app = FastAPI()

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
