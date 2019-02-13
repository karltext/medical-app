from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/medicaldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class LabManager(db.Model):
    __tablename__ = "lab_manager"
    lm_id = db.Column(db.Integer,primary_key=True)
    name = db.Column('name',db.String(50))
    location = db.Column('location',db.String(50))
    
    def __init__(self,params):
        self.name = params["Name"]
        self.location = params["location"]
        pass
    
@app.route("/labmanager")
def example_LabManager():
    db.session.add(LabManager({"Name":"Dr Who","location":"UK"}))
    db.session.commit()
    labmanager = LabManager.query.all()
    for lab in labmanager:
        print("Id: ", lab.lm_id, "Name: ", lab.name, "location: ",lab.location)
    
'''    
class PatientHistory(db.Model): #lab manager's patient history
    pass

class ManageReports(db.Model): #lab manager's managing reports [CRUD]
    pass

class AreaDashboard(db.Model): #lab manager's area dashboard [summary of medical stats]
    pass
'''
        
if __name__ == '__main__':
    db.create_all() # create the schema using the alchemy context
    example_LabManager()
    app.run(port=7700)
    pass