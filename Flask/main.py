from flask import Flask, render_template


app = Flask(__name__, template_folder="templates", static_folder="static")


#Домашняя страница
@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    user = {'nickname': 'Miguel',
            'age': '24',
            'prof': 'Admin'}

    return render_template("index.html",
        title = 'Home',
        user = user)
def hello():
    print ("hello")


#Контакты
@app.route('/contact/')





#Юсеры
@app.route('/user/<int:id>')
def user_profile(id):
    return "Profile page of user #{}".format(id)



#Книги
#@app.route('/books/')
#def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/')
def http_500_handler():
    return ("500 Error", 500)

if __name__ == "__main__":
    app.run()
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT=int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT= 5555
    app.run(HOST, PORT)
