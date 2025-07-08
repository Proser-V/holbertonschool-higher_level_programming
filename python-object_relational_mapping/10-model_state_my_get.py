#!/usr/bin/python3
'''
Module that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa.
'''


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    check = 0

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        if state.name == state_name:
            print(f"{state.id}")
            check = 1
    if check == 0:
        print("Not found")

    session.close()
