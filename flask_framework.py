# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return '<h1>home</home>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['post'])
def sign():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>hello admin！</h3>'
    return '<h3>bad username or password</h3>'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static\uploads',
                                   secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('upload_file.html')

    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=7777)
