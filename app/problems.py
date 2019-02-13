from flask import Blueprint
from flask import request
from flask import jsonify

# import your required models
from models import db
from models import Problem

# define your blueprint
problem_bp = Blueprint('problems', __name__, url_prefix='/problems')

# /problems/list
@problem_bp.route('/list')
def view_problems():
    problems = db.session.query(Problem).all()
    return jsonify([p.to_dict() for p in problems])

# /problems/register
@problem_bp.route('/register', methods=['POST'])
def register_problem():
    p = Problem(**request.form)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict())

