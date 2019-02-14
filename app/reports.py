from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

# import your required models
from models import db
from models import Report

# define your blueprint
report_bp = Blueprint('reports', __name__, url_prefix='/reports')

@report_bp.route('/patient/<int:patient_id>')
def view_patient_reports(patient_id):
    ptreports = Report.query.filter_by(patient_id=patient_id)
    return render_template('reports/patient.html', ptreports=ptreports)

@report_bp.route('/lab-manager/<int:lm_id>')
def view_lab_manager_reports(lm_id):
    lmreports = Report.query.filter_by(lm_id=lm_id)
    return render_template('.html', lmreports=lmreports)

# @report_bp_route('/register')
# def register_report():
    

