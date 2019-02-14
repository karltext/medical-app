from flask import Blueprint
from flask import request
from flask import jsonify

# import your required models
from models import db
from models import LabManager

# define your blueprint
lab_manager_bp = Blueprint('lab_managers', __name__, url_prefix='/lab_managers')




# /lab_managers/private/list
@lab_manager_bp.route('/list')
def view_lab_manager():
    lab_managers = db.session.query(LabManager).all()
    return jsonify([p.to_dict() for p in lab_managers])

# /lab_managers/private/register
@lab_manager_bp.route('/register', methods=['POST'])
def register_lab_manager():
    p = LabManager(**request.form)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_dict())
