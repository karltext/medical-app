from app.app import db

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    print('initialised database schema')
