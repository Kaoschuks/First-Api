import enum
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

class genre(str, Enum):
    action = 'action'
    adventure = 'adventure'
    horror = 'horror'

class Movie(BaseModel):
    title: str
    director: str 
    movie_genre: genre
    age_rating: int
    id : Optional[UUID] = uuid4()


