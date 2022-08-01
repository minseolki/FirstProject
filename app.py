from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:sparta@cluster0.eualsuf.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recipeWrite')
def detail():
    return render_template('recipeWrite.html')

@app.route("/recipe", methods =["post"])
def recipe_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    img_receive = request.form['img_give']
    doc = {'title': title_receive, 'content': content_receive, 'img': img_receive}
    db.recipe.insert_one(doc)
    return jsonify({'msg': '작성 완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
