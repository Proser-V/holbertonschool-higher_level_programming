#!/usr/bin/python3
'''
Module that lists all State objects from the database hbtn_0e_6_usa.
'''


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    "mysql+mysqldb://valentin:mypassword@localhost:3306/hbtn_0e_6_usa"
    )
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).all()

for state in states:
    print(f"{state.id}: {state.name}")

session.close()
