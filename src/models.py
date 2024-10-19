import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))
    description = Column(String(250))
    diameter = Column(String(250))


class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))
    description = Column(String(250))
    model = Column(String(250))

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    color_eyes = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(6))
    starships = Column(String(250), ForeignKey(Vehicles.id))
    planets = relationship("Planets", back_populates="characters")
    vehicles = relationship("Vehicles", back_populates="characters")

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    favorites = Column(Enum('personaje', 'vehiculo', 'planeta', name='favorite_type'))
    usuario = relationship("Usuario", back_populates="favorites")

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
    email = Column(String(250))
    login = relationship("Login", back_populates="usuario")
    favorites = relationship("Favorites", back_populates="usuario")

class Login(Base):
    __tablename__ = 'Login'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    password = Column(String(250))
    usuario_id = Column(String(250), ForeignKey(Usuario.id))
    usuario = relationship("Usuario", back_populates="login")

class FavoriteCharacters(Base):
    __tablename__ = 'favoriteCharacters'
    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    characters_id = Column(Integer, ForeignKey('Characters.id'))
    favorites = relationship("Favorites", back_populates="favorite_characters")
    planet = relationship("Planets", back_populates="favorite_characters")
    Favorites.favorite_characters = relationship("favoriteCharacters", back_populates="favorites")

class FavoriteVehicles(Base):
    __tablename__ = 'FavoriteVehicles'
    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    vehicles_id = Column(Integer, ForeignKey('Vehicles.id'))
    favorites = relationship("Favorites", back_populates="favorite_vehicles")
    vehicles = relationship("Planets", back_populates="favorite_vehicles")
    Favorites.favorite_vehicles = relationship("FavoriteVehicles", back_populates="favorites")

class FavoritePlanets(Base):
    __tablename__ = 'FavoritePlanets'
    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    planets_id = Column(Integer, ForeignKey('Planets.id'))
    favorites = relationship("Favorites", back_populates="favorite_planets")
    planet = relationship("Planets", back_populates="favorite_planets")
    Favorites.favorite_planets = relationship("FavoritePlanets", back_populates="favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')