from fastapi import FastAPI
from movieListView import *

app = FastAPI()

def showAll():
    movies_in_db = get_movies
    return showAllView(movies_in_db)

def start():
    
 #input = raw_input() how to?
    if input == 'y':
        return showAll()
    else:
        return pass

if __name__ == "__main__":
    start()