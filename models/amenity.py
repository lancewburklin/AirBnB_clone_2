#!/usr/bin/python3
"""
    Amenity Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ User class for HBNB """
    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        super().__init__(**kwargs)
