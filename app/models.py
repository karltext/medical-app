from flask_sqlalchemy import SQLAlchemy

# Notes:
# https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html
# https://github.com/sloria/cookiecutter-flask
# http://flask-sqlalchemy.pocoo.org/2.3/queries/

# db initialised with application in app.py
db = SQLAlchemy()


class Serializable(object):
    '''Helper class for converting SQLAlchemy objects to dicts
    for json serialisation.'''

    def to_dict(self):
        cols = self.__table__.columns
        return {c.name: getattr(self, c.name) for c in cols}


#### Models


class LabManager(db.Model, Serializable):
    __tablename__ = 'lab_manager'
    lm_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    reports = db.relationship('Report', backref='lab_manager', lazy=True)


class Patient(db.Model, Serializable):
    __tablename__ = 'patient'
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    location = db.Column(db.String(50))
    reports = db.relationship('Report', backref='patient', lazy=True)


class Report(db.Model, Serializable):
    report_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    lm_id = db.Column(db.Integer, db.ForeignKey('lab_manager.lm_id'))
    created = db.Column(db.DateTime)
    description = db.Column(db.String(256))