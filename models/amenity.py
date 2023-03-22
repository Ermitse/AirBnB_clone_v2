#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    """ Class attribute place_amenities must represent a relationship
    Many-To-Many between the class Place and Amenity. Please see below more
    detail: place_amenity in the Place update """
    place_amenities = relationship("Place", secondary='place_amenity',
                                   back_populates="_amenities")
