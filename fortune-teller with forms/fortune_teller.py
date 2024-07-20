from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")

	elif request.method == 'POST':
		birth_month = request.form['birth_month']
        #birth_month = request.form.get('birthMonth')
		return redirect(url_for('fortune', month=birth_month))
		#return render_template("fortune.html", birth_month=birth_month)
fortunes = ["YOU WILL DIE!", "you will be killed","you will live", "you wont live,you wont die", "you will be lonely", "you wont be lonely", "you will be happy", "you wont be happy", "you will be sad"]

@app.route('/fortune/<month>')
def fortune(month):
	num_letters = len(month)
	fortune_index = num_letters % len(fortunes)
	fortune_result = fortunes[fortune_index]
	return render_template('fortune.html', fortune=fortune_result)
	#num=random.choice(fortunes)
	#return render_template("fortune.html",num=num)

if __name__ == '__main__':
    app.run(debug = True)