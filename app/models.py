from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import declarative_base

# Notes:
# https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html
# https://github.com/sloria/cookiecutter-flask
# http://flask-sqlalchemy.pocoo.org/2.3/queries/

#### TODO:
# redesign model structure
# Records as a core unit

db = SQLAlchemy()
Base = declarative_base()

class Serializable(object):
    '''Helper class for converting SQLAlchemy objects to dicts
    for json serialisation.'''
    def to_dict(self):
        return {c.name: getattr(self, c.name) 
                for c in self.__table__.columns}


#### Models

diagnosis_table = db.Table('diagosis',
    db.Column('patient_id', 
              db.Integer, 
              db.ForeignKey('patient.patient_id'),
              primary_key=True),
    db.Column('problem_id', 
              db.Integer, 
              db.ForeignKey('problem.problem_id'),
              primary_key=True))


class LabManager(db.Model, Serializable):
    __tablename__ = 'lab_manager'
    lm_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))


class Patient(db.Model, Serializable):
    __tablename__ = 'patient'
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    location = db.Column(db.String(50))
    problems = db.relationship('Problem', 
                                secondary=diagnosis_table, 
                                lazy='subquery')


class Problem(db.Model, Serializable):
    __tablename__ = 'problem'
    problem_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))