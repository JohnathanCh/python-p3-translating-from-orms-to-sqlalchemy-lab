#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Dog(Base):
    __tablename__ = 'dogs'

    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    breed = Column(String())
    
    def __repr__(self):
        return f"<Dog(id={self.id}, name={self.name}, breed={self.breed})>"
