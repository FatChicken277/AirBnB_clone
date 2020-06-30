#!/usr/bin/python3
"""Test file storage class.
"""
import unittest
import json
import os
import pep8
from re import search
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """This class test all about file storage.
    """

    models = {"BaseModel": BaseModel, "User": User,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review,
              "State": State}

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
        m = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage._FileStorage__models.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_inittest(self):
        """Test init method.
        """
        with self.assertRaises(TypeError) as err:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(err.exception), msg)
        with self.assertRaises(TypeError) as err:
            FileStorage("piña")
        msg = "object() takes no parameters"
        self.assertEqual(str(err.exception), msg)

    def test_attributes(self):
        """Test class attributes.
        """
        trex = r"\w+\.json"
        path = storage._FileStorage__file_path
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
        self.assertIsInstance(path, str)
        self.assertTrue(search(trex, path))
        obj = storage._FileStorage__objects
        self.assertIsInstance(obj, dict)
        self.assertTrue(storage.all() is obj)

    def test_all(self):
        """Test all method.
        """
        self.assertIsInstance(storage.all(), dict)
        self.assertTrue(storage.all() is storage._FileStorage__objects)

        with self.assertRaises(TypeError) as err:
            storage.all("the devil in i")
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(err.exception), msg)

        with self.assertRaises(TypeError) as err:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), msg)

    def test_new(self):
        """Test new method.
        """
        for k, v in TestFileStorage.models.items():
            a = v()
            storage.new(a)
            key = "{}.{}".format(type(a).__name__, a.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], a)

        with self.assertRaises(TypeError) as err:
            storage.new("devil's", "trill")
        msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(err.exception), msg)

        with self.assertRaises(TypeError) as err:
            storage.new()
        msg = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(err.exception), msg)

    def test_save(self):
        """Test save method.
        """
        a = 0
        for k, v in TestFileStorage.models.items():
            new_obj = v()
            storage.new(new_obj)
            storage.save()
        with open("file.json", mode="r") as file:
            self.assertIsInstance(json.load(file), dict)
            a = 1
        self.assertTrue(a == 1)

        with self.assertRaises(TypeError) as err:
            storage.save("devil's", "trill")
        msg = "save() takes 1 positional argument but 3 were given"
        self.assertEqual(str(err.exception), msg)

        with self.assertRaises(TypeError) as err:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), msg)

    def test_reload(self):
        """Test reload method.
        """
        for k, v in TestFileStorage.models.items():
            new_obj = v()
            no_id = new_obj.id
            storage.new(new_obj)
            storage.reload()
            inin = "{}.{}".format(k, no_id)
            self.assertTrue(inin in FileStorage._FileStorage__objects)
            self.assertIsInstance(storage, FileStorage)

        with self.assertRaises(TypeError) as err:
            storage.reload("devil's", "trill")
        msg = "reload() takes 1 positional argument but 3 were given"
        self.assertEqual(str(err.exception), msg)

        with self.assertRaises(TypeError) as err:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), msg)

if __name__ == "__main__":
    unittest.main()
