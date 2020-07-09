#!/usr/bin/python3
"""
    City Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ User class for HBNB """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        super().__init__(**kwargs)
