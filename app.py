from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.libb3xt.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta




@app.route('/')
def home():
    return render_template('sign_in.html')

@app.route('/sign_in', methods=["POST"])
def sign_in():

    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']


    doc = {
        'name' : name_receive,
        'id': id_receive,
        'password': password_receive
    }
    db.user.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)