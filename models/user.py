#!/usr/bin/python3
"""
    User Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class for HBNB """
    email = ""
    last_name = ""
    password = ""
    first_name = ""

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        super().__init__(**kwargs)
