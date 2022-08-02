from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.libb3xt.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recipe')
def detail():
    return render_template('recipe.html')

@app.route("/recipe", methods =["POST"])
def save_recipe():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    img_receive = request.form['img_give']
    # id_receive = request.form['id_give'] -> 유저 아이디
    # pw_receive = request.form['pw_give'] -> 유저 패스워드
    # num_receive = request.form['num_give'] -> 유저 작성글 넘버
    doc = {'title': title_receive, 'content': content_receive, 'img': img_receive}
    db.recipe.insert_one(doc)
    return jsonify({'msg': '작성 완료'})

@app.route("/temp_img", methods = ["POST"])
def save_image():
    img_receive = request.form['img_give']
    db.temp_img.update_one({'num' :1}, {'$set': {'img': img_receive}})
    return jsonify({'msg': '이미지로드 완료'})

@app.route("/temp_img", methods = ["GET"])
def load_image():
    image = list(db.temp_img.find({}, {'_id': False}))
    return jsonify({'temp_img': image})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
