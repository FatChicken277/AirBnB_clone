#!/usr/bin/python3
"""This module contains a City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Define the City class that inherits from BaseModel.

    Args:
        BaseModel (class): Base Model class.
    """
    state_id = ""
    name = ""
