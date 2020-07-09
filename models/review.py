#!/usr/bin/python3
"""
    Review Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ User class for HBNB """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        super().__init__(**kwargs)
