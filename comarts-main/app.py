from flask import Flask, render_template, jsonify, request, session
from python_scripts.UserAuthentication import UserAuthentication

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
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


@app.route('/comarts', methods=['GET'])
def index():
    return render_template('comarts.html')

@app.route('/postings', methods=['GET'])
def postings():
    return render_template('postings.html')

@app.route('/upload', methods=['POST'])
def postAds():
    
    files = request.files.getlist('files')
    category = request.form.get('category')
    description = request.form.get('description')
    adTitle = request.form.get('adTitle')

    user_id = session.get('user_id')

    file_data = [file.read() for file in files]

    return render_template('comarts.html')



if __name__ == '__main__':
    app.run(debug=True)