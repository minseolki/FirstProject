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

# 저장된 레시피 전체 불러오기 ( _id 값은 제외하고 출력)
@app.route('/recipe', methods=['GET'])
def recipe_list():
    recipes = list(db.recipes.find({}, {'_id': False}))
    return jsonify({'recipe': recipes})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
