import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False)
    password = Column(String(80), nullable=False)
    name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(120), nullable=False)
    image = Column(String(120), nullable=False)
    favorites = relationship("Favorites", backref= "user", lazy=True)

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    origin = Column(String(250), nullable=False)
    image = Column(String(120), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'))
    
    
class Locations(Base):
    __tablename__= 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    dimension = Column(String(250), nullable=False)
    image = Column(String(120), nullable=False)
    residents = relationship("Characters", lazy=True)
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    locations_id = Column(Integer, ForeignKey('locations.id'))
    
def to_dict(self):
    return {}

render_er(Base, 'diagram.png')