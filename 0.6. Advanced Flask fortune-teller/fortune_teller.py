from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/home')
def home():
	# the_random=fortunes[num]
	return render_template("home.html")

@app.route('/fortune')
def fortune():
	fortunes = ["YOU WILL DIE!", "you will eat IASA food","you will live", "you wont live,you wont die", "you will be lonely", "you wont be lonely", "you will be happy", "you wont be happy", "you will be sad"]
	num=random.choice(fortunes)
	return render_template("fortune.html",num=num)

if __name__ == '__main__':
    app.run(debug = True)