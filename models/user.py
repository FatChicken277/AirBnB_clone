#!/usr/bin/python3
"""This module contains a User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define the User class that inherits from BaseModel.

    Args:
        BaseModel (class): Base Model class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
