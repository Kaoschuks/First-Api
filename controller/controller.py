from fastapi import FastAPI
from views.movieListView import *

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

def showAll():
    movies_in_db = get_movies()
    return showAllView(movies_in_db)
