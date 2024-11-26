from flask import Flask, render_template, request
from models import Users, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']
        users_list = Users.query.all()
        return render_template('user.html', users=users_list)

    else:
        return render_template('index.html')

@app.route('/user')
def user(username):
    return render_template('user.html')

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
