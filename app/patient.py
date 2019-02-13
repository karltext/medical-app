'''
Created on 13 Feb 2019

@author: George61080
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from unicodedata import category
from sqlalchemy.orm import backref
import jsonpickle

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@Localhost:3306/medicaldb"
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = "Patient_Information"
    patient_id = db.Column(db.Integer,primary_key=True)
    name = db.Column('patient_name',db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column('patient_gender',db.String(50))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    location = db.Column("patient_location",db.String(50))
    
    
    def __init__(self,params):
        self.name = params["name"]
        self.age = params["age"]
        self.gender = params["gender"]
        self.height = params["height"]
        self.weight = params["weight"]
        self.location = params["location"]
        pass
    
@app.route("/patient-information")
def example_patient():
#     patient1 = Patient({"name":"John","age":57,"gender":"Non-Binary","height":200,"weight":80})
#     db.session.add(patient1)
    db.session.add(Patient({"name":"John","age":57,"gender":"Non-Binary","height":200,"weight":80,"location":"Leeds"}))
    db.session.commit()
    patient = Patient.query.all()
    for p in patient:
        print("patient_id: ",p.patient_id,"name: ",p.name,"age: ",p.age,"gender",p.gender,"height: ",p.height,"weight: ",p.weight,"location",p.location)
      
   

if __name__ == '__main__':
    db.create_all()
    example_patient()
    app.run(port=7700)
    pass