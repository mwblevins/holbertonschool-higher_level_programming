#!/usr/bin/python3
"""test comment"""
import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    toggle = False
    for state in session.query(State):
        if state.name == "Louisiana":
            toggle = True
            break
    if toggle:
        print("LA already exists in db")
    else:
        LA = State(name="Louisiana")
        session.add(LA)
        session.commit()
        print(LA.id)
