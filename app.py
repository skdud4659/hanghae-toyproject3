from flask import Flask, render_template, request, jsonify, redirect, session, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhanghae3


# 메인
@app.route('/')
def home():
   return render_template('home.html')


# 로그인
@app.route('/login')
def login():
    return render_template('login.html')


# 회원가입
@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)