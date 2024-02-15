#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = None  # type: ignore
Session = sessionmaker  # type: ignore
session = None  # type: ignore

def connect_to_database() -> None:
    """Connect to the SQLite database."""
    global engine, Session, session
    try:
        engine = create_engine('sqlite:///restaurants.db')
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        exit(1)

if __name__ == '__main__':
    connect_to_database()
    ipdb.set_trace()
