#!/usr/bin/python3
"""
    Tests for file_storage class
"""
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
import os
from models import storage


class TestFileStorage(unittest.TestCase):
    """ The beginning of the unittests """
    '''def setUp(self):
        """ Creates the JSON file """
        with open("file.json", mode="w", encoding="UTF-8") as f:
            pass
        setattr(storage, "_FileStorage__objects", dict())'''

    def test_doc(self):
        """ Testing for docstring """
        self.assertIsNotNone(("models.engine.file_storage".__doc__))
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_atr(self):
        """ Tests for attributes """
        s1 = FileStorage()
        self.assertTrue(hasattr(s1, "_FileStorage__objects"))
        self.assertTrue(hasattr(s1, "_FileStorage__file_path"))

    def test_class(self):
        """ Makes sure we're making the class """
        s1 = FileStorage()
        self.assertTrue(type(s1), FileStorage)

    def test_all_new(self):
        """ Tests the functionality of new and all """
        setattr(storage, "_FileStorage__objects", dict())
        m1 = BaseModel()
        m2 = BaseModel()
        new_dict = dict()
        new_dict["BaseModel." + m1.id] = m1
        new_dict["BaseModel." + m2.id] = m2
        thing = storage.all()
        self.assertDictEqual(thing, new_dict)

    def test_save_reload(self):
        """ Test save and reload """
        os.remove('file.json')
        b1 = BaseModel()
        b1.save()
        storage.reload()
        new = storage.all()
        self.assertDictEqual(new["BaseModel." + b1.id].to_dict(), b1.to_dict())

    '''def tearDown(self):
        """ Tear that shit down homie """
        os.remove('file.json')'''
