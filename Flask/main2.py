from flask import Flask, render_template, request
from flask_script import Manager, Command, Shell

app = Flask(__name__, template_folder="templates")
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'

manager = Manager(app)

class Faker(Command):
    'Команда для добавления поддельных данных в таблицы'
    def run(self):
        # логика функции
        print("Fake data entered")

manager.add_command("faker", Faker())



@manager.command
def foo():
    "Это созданная команда"
    print("foo command executed")


def shell_context():
    import os, sys
    return dict(app=app, os=os, sys=sys)

manager.add_command("shell", Shell(make_context=shell_context))

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/', methods=['post', 'get'])
def login():

    message = ''

    if request.method == 'POST':
        password = request.form.get('password')
        username = request.form.get('username')

    if username == 'root' and password == 'pass':
        message = "Correct username and password"

    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)

    


@app.route('/user//')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books//')
def books(genre):
    return "All Books in {} category".format(genre)


if __name__ == "__main__":
    app.run()
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT=int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT= 5555
    app.run(HOST, PORT)
