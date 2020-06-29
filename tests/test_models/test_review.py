#!/usr/bin/python3
"""This module test all Review class.
"""
import unittest
import pep8
import os
import json
import datetime
from re import search
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Review class tests.
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
        m = style.check_files(["models/review.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(Review.__doc__)

    def test_heritage(self):
        """Test Review heritage.
        """
        new = Review()
        self.assertTrue(issubclass(type(new), BaseModel))

    def test_attributes(self):
        """Test Review attributes.
        """
        new = Review()
        menu = {"place_id", "user_id", "text"}
        for key in menu:
            self.assertTrue(hasattr(new, key))

        menu2 = {new.place_id, new.user_id, new.text}
        for val in menu2:
            self.assertIsInstance(val, str)
            self.assertTrue(val == "")

    def test_create(self):
        """Test creation of a new instance of Review.
        """
        new = Review()
        trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+"
        self.assertTrue(type(new.id) == str)
        self.assertTrue(search(trex, new.id))
        self.assertTrue(type(new.created_at) == datetime.datetime)
        self.assertTrue(type(new.updated_at) == datetime.datetime)
        with self.assertRaises(TypeError) as error:
            Review.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(error.exception))

    def test_str(self):
        """Test Review str representation.
        """
        new = Review()
        trex = r"\[Review\] \(.*\) .*"
        self.assertIsInstance(new, Review)
        self.assertTrue(type(new.__str__()) == str)
        self.assertTrue(search(trex, new.__str__()))
        args = ["hola", 2, 3.2, "poads"]
        new = Review(*args)
        self.assertIsInstance(new, Review)
        new = Review("hola", 2, 3.2, "poads")
        self.assertIsInstance(new, Review)

    def test_save(self):
        """Test Review save method.
        """
        new = Review()
        old_up = new.updated_at
        new.save()
        self.assertFalse(old_up == new.updated_at)
        with open("file.json", mode="r"):
            a = 1
        self.assertTrue(a == 1)

    def test_todict(self):
        """Test Review to_dict method.
        """
        new = Review()
        di = new.to_dict()
        self.assertTrue(type(di), dict)
        trex = r"\d+-\d+-\d+T\d+:\d+:\d+\.\d+"
        for key in new.__dict__:
            self.assertTrue(key in di)
        self.assertTrue(di["__class__"])
        self.assertTrue(di["__class__"] == "Review")
        self.assertTrue(type(di["created_at"]) == str)
        self.assertTrue(search(trex, di["created_at"]))
        self.assertTrue(type(di["updated_at"]) == str)
        self.assertTrue(search(trex, di["updated_at"]))

    def test_kwargs(self):
        """Test Review init method with kwargs.
        """
        new = Review({})
        self.assertIsInstance(new, Review)
        trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+"
        self.assertTrue(type(new.id) == str)
        self.assertTrue(search(trex, new.id))
        self.assertTrue(type(new.created_at) == datetime.datetime)
        self.assertTrue(type(new.updated_at) == datetime.datetime)
        new = Review(**{"hola": 3})
        self.assertIsInstance(new, Review)
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
        new = Review(**didi)
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
        new = Review()
        a = 0
        nid = new.id
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertTrue(storage.all() is storage._FileStorage__objects)
        storage.new(new)
        sti = "Review.{}".format(nid)
        self.assertTrue(storage._FileStorage__objects[sti])
        storage.save()
        with open("file.json", mode="r") as file:
            self.assertIsInstance(json.load(file), dict)
            a = 1
        self.assertTrue(a == 1)
        storage.reload()
        inin = "Review.{}".format(nid)
        self.assertTrue(inin in FileStorage._FileStorage__objects)
        from models.__init__ import storage
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
