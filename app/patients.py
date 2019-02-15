from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import url_for

# import your required models
from models import db
from models import Patient

# define your blueprint
patient_bp = Blueprint('patients', __name__, url_prefix='/patients')

# /patients/view/<patient_id>
@patient_bp.route('/view/<int:patient_id>')
def view_patient(patient_id):
    'View a single patient profile'
    patient = Patient.query.filter_by(patient_id=patient_id).first()
    return render_template('patients/view.html', patient=patient)

# /patients/list
@patient_bp.route("/list")
def view_all_patients():
    return jsonify([p.to_dict() for p in Patient.query.all()])

# /patients/register
@patient_bp.route('/register', methods=['GET'])
def register_patient():
    'Form page to for users to register a new patient'
    return render_template('patients/register.html')

# /patients/new
@patient_bp.route('/create', methods=['POST'])
def create_patient():
    'Api end-point for creating a new user'
    if not request.form: 
        return ''
    db.session.add(Patient(**request.form))
    db.session.commit()
    p = db.session.query(Patient).order_by(Patient.patient_id.desc()).first()
    url = url_for('patients.view_patient', patient_id=p.patient_id)
    return redirect(url, code=302)


