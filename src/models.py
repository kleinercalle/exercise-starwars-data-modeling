import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    population = Column(Integer)
    gravity = Column(String(40))
    climate = Column(String(50))
    terrain = Column(String(50))
    created = Column(Date)  # Assuming this stores a date
    surface_water = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    pic = Column(String(500))
    url = Column(String(100))

    # Relationship to Person
    residents = relationship("Person", backref="homeworld")

    def to_dict(self):
        return {}

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    birth_year = Column(Date, nullable=False)
    created = Column(Date)  # Assuming this stores a date
    homeworld_id = Column(Integer, ForeignKey('planet.id'))  # Reference to Planet.id
    eye_color = Column(String(10))
    gender = Column(String(15))
    hair_color = Column(String(20))
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String(20))
    pic = Column(String(500))
    url = Column(String(100))

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))  # Reference to Planet.id
    person_id = Column(Integer, ForeignKey('person.id'))  # Reference to Person.id
    name = Column(String(50))

    user = relationship("User", backref="favorites")
    planet = relationship("Planet", backref="favorites")
    person = relationship("Person", backref="favorites")

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
