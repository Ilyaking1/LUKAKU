from flask import Flask, render_template, request, redirect, json, url_for
import datetime
app = Flask(__name__)
age = 0


@app.route('/', methods=['POST'])
def index():
    global age
    file = open('cat.txt', 'r', encoding='utf-8')
    cat = json.loads(file.read())
    file.close()
    age = request.form['age']
    return render_template('mainpicture.html')


app.run(debug=True, port=8101)
