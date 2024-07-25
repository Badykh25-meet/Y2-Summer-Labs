from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCnLfTMnFkKPPMsyVympjS8a3qpdiSwZrM",
  "authDomain": "web-app-project-fafd7.firebaseapp.com",
  "projectId": "web-app-project-fafd7",
  "storageBucket": "web-app-project-fafd7.appspot.com",
  "messagingSenderId": "657839735178",
  "appId": "1:657839735178:web:8e3d3b77c9978660afc873",
  "measurementId": "G-GKDSL68598",
  "databaseURL" : "https://web-app-project-fafd7-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "guh"

@app.route('/home', methods=['GET', 'POST'])
def home():
		return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html") 
	else:
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('home'))
		except:
			error = "email address or pasword is incorrect"
			return render_template("login.html", error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template("signup.html") 
	else:
		email = request.form['email']
		password = request.form['password']
		name = request.form['name']
		age = request.form['age']
		weight = request.form['weight']
		height = request.form['height']
		try:
			user = auth.create_user_with_email_and_password(email, password)
			login_session['user'] = user
			login_session['name'] = name
			login_session['age'] = age
			login_session['weight'] = weight
			login_session['height'] = height
			UID = login_session['user']['localId']
			user_data = {
			"name": name,
			 "age": age, 
			 "weight": weight,
			  "height": height
			  }
			db.child("Users").child(UID).set(user_data)
			login_session['quotes']=[]
			return redirect(url_for('home'))
		except:
			error = "email address does not exist"
			return render_template("signup.html",error=error)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	user = db.child("Users").child(login_session['user']['localId']).get().val()
	print(user)
	return render_template("profile.html",name = user['name'],age = user['age'],weight = user['weight'],height = user['height'])
@app.route('/signout', methods=["GET", "POST"])
def signout():
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(debug=True)