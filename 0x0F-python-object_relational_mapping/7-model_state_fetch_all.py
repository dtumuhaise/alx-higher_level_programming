#!/usr/bin/python3
"""
class definition of a state and intance Base
"""


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    """ create an engine """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    """create configured session class"""
    Session = sessionmaker(bind=engine)
    """create a session"""
    session = Session()    
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
