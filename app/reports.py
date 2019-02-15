from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import url_for

# import your required models
from models import db
from models import Report
import jsonpickle

# define your blueprint
report_bp = Blueprint('reports', __name__, url_prefix='/reports')

# /reports/register
@report_bp.route('/register', methods=['POST', 'GET'])
def register_report():
    'Api end-point for creating a new user'
    db.session.add(Report(**request.form))
    db.session.commit()
    return render_template('/reports/register.html')


# /reports/create
@report_bp.route('/create', methods=['POST', 'GET'])
def create_report():
    'Api end-point for creating a new report'
    # add the report
    db.session.add(Report(**request.form))
    db.session.commit()
    # fetch the newly created for display of successful response
    r = db.session.query(Report).order_by(Report.report_id.desc()).first()
    # return redirect(url_for())
    # TODO !!! redirect to lab manager page
    if request.method == 'POST':
        return redirect(url_for('reports.view_report', report_id=r.report_id))
    

# /reports/view/<report_id>
@report_bp.route('/view/<int:report_id>')
def view_report(report_id):
    'View a single report'
    report = Report.query.filter_by(report_id=report_id).first()
    return render_template('reports/view.html', report=report)

@report_bp.route("/view-all")
def view_all_reports():
    reports = Report.query.all()
    report_list = []
    for r in reports:
        report_list.append(r)
    
    return jsonpickle.encode(report_list)