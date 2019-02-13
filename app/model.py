from app import db

class Profile(db.Model):
    __tablename__ = "alc_profile"
    profile_id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
