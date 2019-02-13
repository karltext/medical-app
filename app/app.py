from flask import Flask
from flask import request
from flask import render_template

from flask_sqlalchemy import SQLAlchemy

# import our defined data models
import model

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+mysqlconnector://root:root@localhost:3306/medicaldb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/profiles/list')
def list_profiles():
    profiles = model.Profile.query.all()
    return render_template('base.html', profiles=profiles)

# @app.route('/profiles/view/<profile_id>')
# def view_profile(profile_id):
#     profiles = Product.query.all()
#     return "ok"

@app.route('/profiles/create', methods=['POST'])
def create_profile():
    p = model.Profile(name="dave") 
    db.session.add(p)
    db.session.commit()
    pass

if __name__ == '__main__':
    app.run(port=8000, debug=True)