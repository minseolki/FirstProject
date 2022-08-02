import hashlib
from datetime import datetime, timedelta
import jwt
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.libb3xt.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)

SECRET_KEY = 'SPARTA'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/sign_in',methods=['POST'])
def sign_in():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    #pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    pw_hash = password_receive;
    result = db.user.find_one({'id':username_receive,'password':pw_hash})
    if result is not None:
        payload = {
            'id': username_receive,
            'exp':datetime.utcnow() + timedelta(seconds=60*5)
        }
        token = jwt.encode(payload,SECRET_KEY,algorithm='HS256').decode('utf-8')
        return jsonify({'result':'success','token':token})
    else:
        return jsonify({'result':'fail','msg':'아이디/비밀번호가 일치하지 않습니다.'})
    

@app.route('/login')
def login():
    return render_template('login.html')

# 저장된 레시피 전체 불러오기 ( _id 값은 제외하고 출력)
@app.route('/recipe', methods=['GET'])
def recipe_list():
    recipes = list(db.recipes.find({}, {'_id': False}))
    return jsonify({'recipe': recipes})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
