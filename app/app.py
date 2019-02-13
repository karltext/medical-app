from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

# import mysqlAlchemy
from models import db

# import views 
from patients import patient_bp

app = Flask(__name__)

# register your blueprints here
app.register_blueprint(patient_bp)


app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+mysqlconnector://root:root@localhost:3306/medicaldb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


if __name__ == '__main__':
    app.run(port=8000, debug=True)