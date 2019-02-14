from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

# import your required models
from models import db
from models import Report

# define your blueprint
report_bp = Blueprint('reports', __name__, url_prefix='/reports')

# /reports/new
@report_bp.route('/create', methods=['POST'])
def create_report():
    'Api end-point for creating a new report'
    # add the report
    db.session.add(Report(**request.form))
    db.session.commit()
    # fetch the newly created
    r = db.session.query(Report).order_by(Report.report_id.desc()).first()
    return jsonify(r.to_dict())

