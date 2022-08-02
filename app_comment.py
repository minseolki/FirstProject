from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#db연결
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:1234@cluster0.uibxg7e.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('comment.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_r = request.form['name_g']
    comment_r = request.form['comment_g']
    # db에 저장
    doc = {
        'name': name_r,
        'comment': comment_r
    }
    db.comments.insert_one(doc)

    return jsonify({'msg':'입력되었습니다.'})

@app.route("/homework", methods=["GET"])
def homework_get():
    # db 꺼내기(리스트)
    fancomments_ilst = list(db.comments.find({}, {'_id': False}))
    return jsonify({'fanlist':fancomments_ilst,'msg2':'GET완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)