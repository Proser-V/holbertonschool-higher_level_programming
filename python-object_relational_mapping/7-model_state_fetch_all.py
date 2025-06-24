#!/usr/bin/python3
'''
Module that lists all State objects from the database hbtn_0e_6_usa.
'''


from model_state import Base, State
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa")
Base.metadata.create_all(engine)
