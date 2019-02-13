from app.app import app
# from app.app import db

if __name__ == '__main__':
    # creates tables from schema defined in app classes
    with app.app_context():
        db.create_all()
        db.session.commit()
        print('initialised database schema')
