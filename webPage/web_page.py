import io
from datetime import date

today = date.today()
from flask import Flask, redirect, url_for, request, send_file, render_template

from certificate_generator import certificat

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('return_file', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('return_file', name=user))


@app.route('/return-files/<name>', methods=['GET'])
def return_file(name):
    file_object = io.BytesIO()
    img = certificat(name)
    img.save(file_object, 'PNG')
    file_object.seek(0)
    return send_file(file_object, mimetype='image/PNG', attachment_filename=name + '.png', as_attachment=True)


@app.route('/')
def hello_world():
    return render_template("login.html")


def run():
    app.run(debug=True, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    app.run(debug=True)
