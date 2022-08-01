from flask import Flask
import certifi

ca = certifi.where()

app = Flask(__name__)