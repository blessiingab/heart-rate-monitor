#!/usr/bin/env python3


import os
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# Setup DB
BASE_DIR = os.path.dirname(__file__)
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
os.makedirs(INSTANCE_DIR, exist_ok=True)
DB_PATH = os.path.join(INSTANCE_DIR, 'heart_monitor.db')

engine = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Person table
class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    gender = Column(String)
    readings = relationship('HeartRate', back_populates='person')

# Heart rate table
class HeartRate(Base):
    __tablename__ = 'heart_rates'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    bpm = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    person = relationship('Person', back_populates='readings')

# Create tables
Base.metadata.create_all(engine)

