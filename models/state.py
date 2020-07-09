#!/usr/bin/python3
"""
    State Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ User class for HBNB """
    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        super().__init__(**kwargs)
