#!/usr/bin/python3
"""This module test all User class.
"""
import unittest
import pep8
import os
import json
import datetime
from re import search
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """User class tests.
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
        m = style.check_files(["models/user.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(User.__doc__)

    def test_heritage(self):
        """Test User heritage.
        """
        new = User()
        self.assertTrue(issubclass(type(new), BaseModel))

    def test_attributes(self):
        """Test User attributes.
        """
        new = User()
        menu = {"email", "password", "first_name", "last_name"}
        for key in menu:
            self.assertTrue(hasattr(new, key))

        menu2 = {new.email, new.password, new.first_name, new.last_name}
        for val in menu2:
            self.assertIsInstance(val, str)
            self.assertTrue(val == "")

    def test_create(self):
        """Test creation of a new instance of User.
        """
        new = User()
        trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+"
        self.assertTrue(type(new.id) == str)
        self.assertTrue(search(trex, new.id))
        self.assertTrue(type(new.created_at) == datetime.datetime)
        self.assertTrue(type(new.updated_at) == datetime.datetime)
        with self.assertRaises(TypeError) as error:
            User.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(error.exception))

    def test_str(self):
        """Test User str representation.
        """
        new = User()
        trex = r"\[User\] \(.*\) .*"
        self.assertIsInstance(new, User)
        self.assertTrue(type(new.__str__()) == str)
        self.assertTrue(search(trex, new.__str__()))
        args = ["hola", 2, 3.2, "poads"]
        new = User(*args)
        self.assertIsInstance(new, User)
        new = User("hola", 2, 3.2, "poads")
        self.assertIsInstance(new, User)

    def test_save(self):
        """Test User save method.
        """
        new = User()
        old_up = new.updated_at
        new.save()
        self.assertFalse(old_up == new.updated_at)
        with open("file.json", mode="r"):
            a = 1
        self.assertTrue(a == 1)

    def test_todict(self):
        """Test User to_dict method.
        """
        new = User()
        di = new.to_dict()
        self.assertTrue(type(di), dict)
        trex = r"\d+-\d+-\d+T\d+:\d+:\d+\.\d+"
        for key in new.__dict__:
            self.assertTrue(key in di)
        self.assertTrue(di["__class__"])
        self.assertTrue(di["__class__"] == "User")
        self.assertTrue(type(di["created_at"]) == str)
        self.assertTrue(search(trex, di["created_at"]))
        self.assertTrue(type(di["updated_at"]) == str)
        self.assertTrue(search(trex, di["updated_at"]))

    def test_kwargs(self):
        """Test User init method with kwargs.
        """
        new = User({})
        self.assertIsInstance(new, User)
        trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+"
        self.assertTrue(type(new.id) == str)
        self.assertTrue(search(trex, new.id))
        self.assertTrue(type(new.created_at) == datetime.datetime)
        self.assertTrue(type(new.updated_at) == datetime.datetime)
        new = User(**{"hola": 3})
        self.assertIsInstance(new, User)
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
        new = User(**didi)
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
        new = User()
        a = 0
        nid = new.id
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertTrue(storage.all() is storage._FileStorage__objects)
        storage.new(new)
        sti = "User.{}".format(nid)
        self.assertTrue(storage._FileStorage__objects[sti])
        storage.save()
        with open("file.json", mode="r") as file:
            self.assertIsInstance(json.load(file), dict)
            a = 1
        self.assertTrue(a == 1)
        storage.reload()
        inin = "User.{}".format(nid)
        self.assertTrue(inin in FileStorage._FileStorage__objects)
        from models.__init__ import storage
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
