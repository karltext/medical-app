from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

# import your required models
from models import db
from models import LabManager
from models import Patient
from models import Report

# define your blueprint
lab_manager_bp = Blueprint('lab_managers', __name__, url_prefix='/lab_managers')

# /lab_managers/view/<lm_id>
@lab_manager_bp.route('/view/<int:lm_id>')
def view_lab_manager(lm_id):
    'View a single lab_manager profile'
    lab_manager = LabManager.query.filter_by(lm_id=lm_id).first()
    return render_template('lab_managers/view.html', lab_manager=lab_manager)

# /lab_managers/<int:lm_id>/patient/<int:patient_id>
@lab_manager_bp.route('/<int:lm_id>/patient/<int:patient_id>')
def view_patient_reports(lm_id, patient_id):
    'view reports for a specfic patient'
    context = dict(
        lab_manager=LabManager.query.filter_by(lm_id=lm_id).first(),
        reports=Report.query.filter_by(lm_id=lm_id, patient_id=patient_id),
        patient=Patient.query.filter_by(patient_id=patient_id).first())
    return render_template('lab_managers/patient.html', **context)

#### Private helpers for creating and debugging.

# /lab_managers/private/register
@lab_manager_bp.route('/register', methods=['POST'])
def register_lab_manager():
    p = LabManager(**request.form)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict())

