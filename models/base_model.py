#!/usr/bin/python3
"""
    Base Model
    HolbertonBnB
"""
import uuid
import datetime


class BaseModel():
    """ BaseModel class for command interpreter """

    def __init__(self, *args, **kwargs):
        """ constructor for BaseModel """
        from models import storage
        if kwargs:
            for item in list(kwargs.keys()):
                if item == 'created_at' or item == 'updated_at':
                    self.__dict__[item] = datetime.datetime.strptime(
                        kwargs[item], '%Y-%m-%dT%H:%M:%S.%f')
                elif item == "__class__":
                    pass
                else:
                    self.__dict__[item] = kwargs[item]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ string representation of our badass command interpreter """
        s = "[{}] ({}) {}".format(str(
            type(self).__name__), self.id, self.__dict__)
        return s

    def save(self):
        """ saves up in this motherfucker """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Creates a dictionary """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = str(type(self).__name__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
