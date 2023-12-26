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


@app.route('/comarts', methods=['GET'])
def index():
    return render_template('comarts.html')

@app.route('/postings', methods=['GET'])
def postings():
    return render_template('postings.html')

@app.route('/upload', methods=['POST'])
def postAds():
    '''
    CREATE TABLE IF NOT EXISTS postingData (
            posting_user_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
            file_data_1 BLOB,
            file_data_2 BLOB,
            file_data_3 BLOB,
            file_data_4 BLOB,
            file_data_5 BLOB,
            text_input1 TEXT,
            text_input2 TEXT,
            text_input3 TEXT,
            text_input4 TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
    '''
    files = request.files.getlist('files')
    category = request.form.get('category')
    description = request.form.get('description')
    adTitle = request.form.get('adTitle')

    return render_template('comarts.html')



if __name__ == '__main__':
    app.run(debug=True)