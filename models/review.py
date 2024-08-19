# models/review.py
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
