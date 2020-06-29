#!/usr/bin/python3
"""This module test all Amenity class.
"""
import unittest
import pep8
import os
import json
import datetime
from re import search
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Amenity class tests.
    """

    def setUp(self):
        """Clean code after each test.
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/amenity.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_heritage(self):
        """Test Amenity heritage.
        """
        new = Amenity()
        self.assertTrue(issubclass(type(new), BaseModel))

    def test_attributes(self):
        """Test Amenity attributes.
        """
        new = Amenity()
        self.assertTrue(hasattr(new, "name"))
        self.assertIsInstance(new.name, str)
        self.assertTrue(new.name == "")

    def test_create(self):
        """Test creation of a new instance of Amenity.
        """
        new = Amenity()
        trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+"
        self.assertTrue(type(new.id) == str)
        self.assertTrue(search(trex, new.id))
        self.assertTrue(type(new.created_at) == datetime.datetime)
        self.assertTrue(type(new.updated_at) == datetime.datetime)
        with self.assertRaises(TypeError) as error:
            Amenity.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(error.exception))

    def test_str(self):
        """Test Amenity str representation.
        """
        new = Amenity()
        trex = r"\[Amenity\] \(.*\) .*"
        self.assertIsInstance(new, Amenity)
        self.assertTrue(type(new.__str__()) == str)
        self.assertTrue(search(trex, new.__str__()))
        args = ["hola", 2, 3.2, "poads"]
        new = Amenity(*args)
        self.assertIsInstance(new, Amenity)
        new = Amenity("hola", 2, 3.2, "poads")
        self.assertIsInstance(new, Amenity)

    def test_save(self):
        """Test Amenity save method.
        """
        new = Amenity()
        old_up = new.updated_at
        new.save()
        self.assertFalse(old_up == new.updated_at)
        with open("file.json", mode="r"):
            a = 1
        self.assertTrue(a == 1)

    def test_todict(self):
        """Test Amenity to_dict method.
        """
        new = Amenity()
        di = new.to_dict()
        self.assertTrue(type(di), dict)
        trex = r"\d+-\d+-\d+T\d+:\d+:\d+\.\d+"
        for key in new.__dict__:
            self.assertTrue(key in di)
        self.assertTrue(di["__class__"])
        self.assertTrue(di["__class__"] == "Amenity")
        self.assertTrue(type(di["created_at"]) == str)
        self.assertTrue(search(trex, di["created_at"]))
        self.assertTrue(type(di["updated_at"]) == str)
        self.assertTrue(search(trex, di["updated_at"]))

    def test_kwargs(self):
        """Test Amenity init method with kwargs.
        """
        new = Amenity({})
        self.assertIsInstance(new, Amenity)
        trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+"
        self.assertTrue(type(new.id) == str)
        self.assertTrue(search(trex, new.id))
        self.assertTrue(type(new.created_at) == datetime.datetime)
        self.assertTrue(type(new.updated_at) == datetime.datetime)
        new = Amenity(**{"hola": 3})
        self.assertIsInstance(new, Amenity)
        self.assertTrue(new.__dict__["hola"])
        self.assertTrue(new.__dict__["hola"] == 3)
        with self.assertRaises(KeyError) as error:
            self.assertTrue(new.to_dict()["hola"])
        self.assertEqual("'created_at'", str(error.exception))
        didi = {"id": "68fe96ab-2a31-4394-824a-082820dbc960",
                "created_at": "2017-06-14T22:31:03.285259",
                "updated_at":
                datetime.datetime(2020, 6, 29, 15, 34, 58, 459047),
                "__class__": "Pizza"}
        new = Amenity(**didi)
        with self.assertRaises(KeyError) as error:
            self.assertTrue(new.__dict__["__class__"])
        id = "68fe96ab-2a31-4394-824a-082820dbc960"
        self.assertTrue(new.__dict__["id"] == id)
        self.assertIsInstance(new.__dict__["created_at"], datetime.datetime)
        self.assertIsInstance(new.__dict__["updated_at"], datetime.datetime)

    def test_filestorage(self):
        """Test file storage.
        """
        storage = FileStorage()
        new = Amenity()
        a = 0
        nid = new.id
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertTrue(storage.all() is storage._FileStorage__objects)
        storage.new(new)
        sti = "Amenity.{}".format(nid)
        self.assertTrue(storage._FileStorage__objects[sti])
        storage.save()
        with open("file.json", mode="r") as file:
            self.assertIsInstance(json.load(file), dict)
            a = 1
        self.assertTrue(a == 1)
        storage.reload()
        inin = "Amenity.{}".format(nid)
        self.assertTrue(inin in FileStorage._FileStorage__objects)
        from models.__init__ import storage
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
