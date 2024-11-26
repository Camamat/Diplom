from flask import Flask
from models import Users, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        user1 = Users(name='Azat', age=22)
        user2 = Users(name='Andrey', age=23)
        user3 = Users(name='Anton', age=24)
        user4 = Users(name='Denis', age=25)
        db.session.add_all([user1, user2, user3, user4])
        db.session.commit()