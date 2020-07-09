#!/usr/bin/python3
"""
    Place Model
    HolbertonBnB
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ User class for HBNB """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ constructor for User """
        super().__init__(**kwargs)
