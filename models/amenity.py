#!/usr/bin/python3
"""This module contains a Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define the Amenity class that inherits from BaseModel.

    Args:
        BaseModel (class): Base Model class.
    """
    name = ""
