from fastapi import FastAPI
from views.movieListView import *

app = FastAPI()

def showAll():
    movies_in_db = get_movies
    return showAllView(movies_in_db)

def start():
    startView()
    if input == 'y':
        return showAll()
    else:
        return endView()

if __name__ == "__main__":
    start(