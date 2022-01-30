#!/usr/bin/python3
""" This is the State class """
from jinja2 import ModuleLoadeer
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class 
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade='delete')
    else:
        @property
        def cities(self):
            """ Getter method for cities
            Return: list of cities with state_id equal to self.id
            """
            #return list of City objs in __objects
            cities_in_state = []

            #copy values from dict to list
            for city in models.storage.all(City).values():
                if self.id == city:
                    cities_in_state.append(city)
            return cities_in_state
