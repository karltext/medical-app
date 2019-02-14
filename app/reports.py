from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import url_for

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
    return render_template('viewreport.html', lmreports=lmreports)

#/reports/register
@report_bp.route('/register', methods=['POST', 'GET'])
def register_report():
    'Api end-point for creating a new user'
    r = Report(**request.form)
    db.session.add(r)
    db.session.commit()
    #return jsonify(r.to_dict())
    return render_template('/reports/createreport.html', r=r)


# /reports/create
@report_bp.route('/create', methods=['POST', 'GET'])
def create_report():
    'Api end-point for creating a new report'
    # add the report
    db.session.add(Report(**request.form))
    db.session.commit()
    # fetch the newly created
    r = db.session.query(Report).order_by(Report.report_id.desc()).first()
    return jsonify(r.to_dict())


