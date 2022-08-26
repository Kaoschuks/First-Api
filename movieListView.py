from fastapi import FastAPI
from pydantic import BaseModel
from main import movielist
from typing import List
from models.movie_models import Movie       

app = FastAPI()


@app.get("/items/")
async def get_movies():
    for movie in movielist:
        print(movie) 
