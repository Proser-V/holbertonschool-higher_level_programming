#!/usr/bin/python3
'''
Module that contains the class definition of a State and an instance Base.
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    '''
    Defines a State mapped to the states table with a relationship to City.
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
        'City',
        back_populates="state",
        cascade="all, delete-orphan",
        order_by='City.id'
        )
