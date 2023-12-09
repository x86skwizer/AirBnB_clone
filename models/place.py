#!/usr/bin/python3

"""
This file defines the Place class, which represents a place in a city.
It inherits from the BaseModel class and provides attributes to store
information about the place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """A class representing a place."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __str__(self):
        """Representation of class Place"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
