from flask import Flask, render_template, request, redirect, url_for, session
import random
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        name = request.form['name']
        birth_month = request.form['birth_month']
        
        session['name'] = name
        session['birth_month'] = birth_month
        
        return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html",name=session['name'])

	elif request.method == 'POST':
		birth_month = request.form.get('birthMonth')
		return render_template(url_for("fortune.html", birth_month=birth_month))
fortunes = ["YOU WILL DIE!", "you will be killed","you will live", "you wont live","you wont die", "you will be lonely", "you wont be lonely", "you will be happy", "you wont be happy", "you will be sad"]

@app.route('/fortune/<month>')
def fortune(month):
	num=random.choice(fortunes)
	return render_template("fortune.html",num=num)

if __name__ == '__main__':
    app.run(debug = True)