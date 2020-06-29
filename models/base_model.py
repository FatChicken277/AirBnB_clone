#!/usr/bin/python3
"""This module contains a BaseModel class.
"""
import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """BaseModel class from which all the others will inherit
    """

    def __init__(self, *args, **k):
        """Initializer function (also known as constructor)
Will make an object with specific values if given kwargs, otherwise, standard
        """
        if k:
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            if "created_at" in k and type(k["created_at"]) is str:
                k["created_at"] = datetime.strptime(k["created_at"], fmt)
            if "updated_at" in k and type(k["updated_at"]) is str:
                k["updated_at"] = datetime.strptime(k["updated_at"], fmt)
            k.pop("__class__", "pizza")
            self.__dict__.update(k)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This function returns a pretty version of the object in a string

        Returns:
            str: Object in a pretty format
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This functions saves in the storage, also updates the updated_at
parameter
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This functions makes the object representation in a dictionary
The dates created_at and updated_At are formatted in isoformat

        Returns:
            dict: Dictioanry representation with JSONable date formats
        """
        didi = self.__dict__.copy()
        didi["__class__"] = self.__class__.__name__
        didi["created_at"] = didi["created_at"].isoformat()
        didi["updated_at"] = didi["updated_at"].isoformat()
        return didi
