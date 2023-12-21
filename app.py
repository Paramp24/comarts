from flask import Flask, render_template, jsonify, request
from python_scripts.UserAuthentication import UserAuthentication

app = Flask(__name__)
user_authentication = UserAuthentication()


@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')


@app.route('/signup', methods=['GET'])
def sign():
    return render_template('signup.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    result = user_authentication.user_loader(data)
    return jsonify(result)


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)