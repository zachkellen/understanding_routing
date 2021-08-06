from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
    return "Dojo"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    return f"{word * num}"

@app.errorhandler(404)
def no_response(e):
    return "Sorry! No reponse. Try again."

if __name__=='__main__':
    app.run(debug=True)