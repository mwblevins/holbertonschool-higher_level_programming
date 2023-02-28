#!/usr/bin/python3
"""State Class"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """subclass of Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
