from fastapi import FastAPI
from pydantic import BaseModel
from main import movielist
from typing import List
from models.movie_models import Movie       

app = FastAPI()


@app.get("/items/")
async def get_movies():
    for movie in movielist:
        return movie


def showAllView(movielist : List[Movie]):
    print 'In our db, we have %i movies' % len(movielist)
    for item in movielist:
        print item.title

def startView():
    print 'Welcome'
    print 'Show all movies?[y/n]'

def endView():
    print 'Goodbye!'
