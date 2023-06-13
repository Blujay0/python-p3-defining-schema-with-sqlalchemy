#!/usr/bin/env python3

# create_engine needs to be imported to persist the schema
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    '''
    The __tablename__ attribute will eventually be used as the name of our 
    SQL database table
    '''
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
if __name__ == '__main__':
    '''
    the create_all() command tells the engine that any models that were
    created using Base as a parnet should be used to create tables    
    '''
    engine = create_engine('sqlite:///studnets.db')
    Base.metadata.create_all(engine)
    
'''
run chmod +x lib/sqlalchemy_sandbox.py to make the script executable
then, run lib/sqlalchemy_sandbox.py from the shell and you should see
a databse file pop up with a table
'''