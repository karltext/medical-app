from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import declarative_base

# https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html

db = SQLAlchemy()
Base = declarative_base()

diagnosis_table = db.Table('diagosis', Base.metadata,
    db.Column('patient_id', db.Integer, db.ForeignKey('patient.patient_id')),
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.problem_id')))

class LabManager(db.Model):
    __tablename__ = "lab_manager"
    lm_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))

class Patient(db.Model):
    __tablename__ = "patient"
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    location = db.Column(db.String(50))
    problems = db.relationship("Problem", secondary=diagnosis_table)

class Problem(db.Model):
    __tablename__ = 'problem'
    problem_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

