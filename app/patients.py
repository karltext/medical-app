from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

# import your required models
from models import db
from models import Patient

# define your blueprint
patient_bp = Blueprint('profiles', __name__, url_prefix='/patients')

# create routes in the same way you would do @app.route

# /patients/list
@patient_bp.route('/list')
def view_patients():
    patients = db.session.query(Patient).all()
    print(patients)
    print([p.name for p in patients])
    return render_template('profile.html', patients=patients)

# /patients/register
@patient_bp.route('/register', methods=['POST'])
def register_patient():
    p = Patient(**request.form)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict())

# /patients/register/problem
@patient_bp.route('/register/problem', methods=['POST'])
def register_patient_problem():
    problem_id = request.form['problem_id']
    patient_id = request.form['patient_id']

