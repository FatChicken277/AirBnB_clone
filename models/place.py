#!/usr/bin/python3
"""This module contains a Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Define the Place class that inherits from BaseModel.

    Args:
        BaseModel (class): Base Model class.
    """
    city_id, user_id, name, description = "", "", "", ""
    number_rooms, number_bathrooms = 0, 0
    max_guest, price_by_night = 0, 0
    latitude, longitude = 0.0, 0.0
    amenity_ids = []
