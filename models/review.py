#!/usr/bin/python3
"""This module contains a Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define the Review class that inherits from BaseModel.

    Args:
        BaseModel (class): Base Model class.
    """
    place_id = ""
    user_id = ""
    text = ""
