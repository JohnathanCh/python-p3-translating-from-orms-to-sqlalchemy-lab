import pdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dog

engine = create_engine('sqlite:///:memory:')

def create_table(base):
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, row):
    return Dog(id=row.id, name=row.name, breed=row.breed)

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    # pdb.set_trace()
    return session.query(Dog).filter_by(id=dog.id).update({Dog.breed: breed})