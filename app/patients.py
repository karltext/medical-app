from flask import Blueprint

# import your required models
from models import Patient

# define your blueprint
patient_bp = Blueprint('profiles', __name__, url_prefix='/patients')

# create routes in the same way you would do @app.route
@patient_bp.route('/list')
def view_patients():
    return 'ok'