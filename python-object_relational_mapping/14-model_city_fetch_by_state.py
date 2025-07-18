#!/usr/bin/python3
'''
Module that prints all City objects from the database hbtn_0e_14_usa.
'''


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    session.commit()
    session.close()
