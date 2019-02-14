from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

# import your required models
from models import db
from models import Patient

# define your blueprint
patient_bp = Blueprint('profiles', __name__, url_prefix='/patients')

# /patients/view/<patient_id>
@patient_bp.route('/view/<int:patient_id>')
def view_patient(patient_id):
    patient = Patient.query.filter_by(patient_id=patient_id).first()
    return render_template('profile.html', patient=patient)

# /patients/register
@patient_bp.route('/register', methods=['GET','POST'])
def register_patient():
    '''
    p = Patient(**request.form)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict())
    return render_template('registerpatient.html', p=p)
    '''
    if request.form:
        regpatient = Patient(name=request.form.get("name"), age=request.form.get("age"), gender=request.form.get("gender"), 
                             height=request.form.get("height"), weight=request.form.get("weight"), location=request.form.get("location"))
        db.session.add(regpatient)
        db.session.commit()
    return render_template("registerpatient.html") 

# /patients/register/problem
@patient_bp.route('/register/problem', methods=['POST'])
def register_patient_problem():
    problem_id = request.form['problem_id']
    patient_id = request.form['patient_id']

