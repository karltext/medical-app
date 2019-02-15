from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

# import mysqlAlchemy
from models import db
from models import Patient
from models import LabManager

# import views 
from patients import patient_bp
from lab_managers import lab_manager_bp
from reports import report_bp

app = Flask(__name__)

# add configurations
app.config.from_pyfile('settings.py')

# register your blueprints here
app.register_blueprint(patient_bp)
app.register_blueprint(lab_manager_bp)
app.register_blueprint(report_bp)

@app.route('/')
def home():
    'List all patients an lab managers for demo purposes'
    context = dict(patients=Patient.query.all(), 
                   lab_managers=LabManager.query.all())
    return render_template('home.html', **context)
    #return render_template('home.html', **context)

# initialise database
with app.app_context():
    db.init_app(app)
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    app.run(port=8000, debug=True)