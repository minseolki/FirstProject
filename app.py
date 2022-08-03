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


@app.route('/recipe')
def write():
    return render_template('recipe.html')


@app.route('/comment/<keyword>')
def comment(keyword):
    return render_template('comment.html', word=keyword)


@app.route('/login')
def log_in():
    return render_template('login.html')


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


# 저장된 레시피 전체 불러오기 ( _id 값은 제외하고 출력)
@app.route('/api/recipe', methods=['GET'])
def recipe_get():
    recipes = list(db.recipe.find({}, {'_id': False}))
    return jsonify({'recipe': recipes})


@app.route("/recipe", methods=["POST"])
def save_recipe():
    title_receive = request.form['title_give']
    line_desc_receive = request.form['line_desc_give']
    content_receive = request.form['content_give']
    img_receive = request.form['img_give']
    time_receive = request.form['time_give']
    # id_receive = request.form['id_give'] -> 유저 아이디
    # pw_receive = request.form['pw_give'] -> 유저 패스워드
    # num_receive = request.form['num_give'] -> 유저 작성글 넘버
    doc = {'title': title_receive, 'line_desc': line_desc_receive, 'content': content_receive, 'img': img_receive,
           'time': time_receive}
    db.recipe.insert_one(doc)
    return jsonify({'msg': '작성 완료'})


@app.route("/temp_img", methods=["POST"])
def save_image():
    img_receive = request.form['img_give']
    db.temp_img.update_one({'num': 1}, {'$set': {'img': img_receive}})
    return jsonify({'msg': '이미지로드 완료'})


@app.route("/temp_img", methods=["GET"])
def load_image():
    image = list(db.temp_img.find({}, {'_id': False}))
    return jsonify({'temp_img': image})


@app.route('/api/login', methods=['POST'])
def log_in_api():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    # pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    pw_hash = password_receive;
    result = db.user.find_one({'id': username_receive, 'password': pw_hash})
    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/api/sign_in', methods=["POST"])
def api_sign_in():
    name_receive = request.form['name_give']
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']

    # 비밀번호 암호화
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    doc = {
        'name': name_receive,
        'id': id_receive,
        'password': password_hash
    }
    db.user.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


# 아이디 중복 확인
@app.route('/sign_in/check_dup', methods=['POST'])
def check_dup():
    id_receive = request.form['id_give']
    exists = bool(db.user.find_one({"id": id_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route("/comment", methods=["POST"])
def comment_post():
    name_r = request.form['name_g']
    comment_r = request.form['comment_g']
    doc = {
        'name': name_r,
        'comment': comment_r
    }
    db.comments.insert_one(doc)

    return jsonify({'msg': '입력되었습니다.'})


@app.route("/comment", methods=["GET"])
def comment_get():
    comments_ilst = list(db.comments.find({}, {'_id': False}))
    return jsonify({'cmtlist': comments_ilst, 'msg2': 'GET완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
