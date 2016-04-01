#Code for App Framework
#References: Tour-De-City (Previous Flask Framework Implemented by David Cahn)

from flask import Flask, render_template, request, redirect, session, url_for
from py import *
from py import output
import stripe
import json

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

@app.route("/", methods = ["GET","POST"])
def index():
	return render_template("index.html")

@app.route ("/input",  methods = ["GET","POST"])
def input():
	if request.method == "GET":
		print ("get")
	else: 
		print("post request")
		button = request.form['button'] if 'button' in request.form else None
		print (button)
		if button == "Submit":
			session['description'] = request.form.get("description", None)
			session['option_1'] = request.form.get("option1", None)
			session['option_2'] = request.form.get("option2", None)
			session['time_to_pay'] = 0;
			session['payment_accepted'] = 0;
			return redirect('/payment')
	return render_template("input.html")

@app.route ("/payment",  methods = ["GET","POST"])
def payment():
	if not('time_to_pay' in session and session['time_to_pay'] == 0):
		return redirect("input")
	if (session['payment_accepted'] == 0): 
		if not request.method == "GET":
			# Set your secret key: remember to change this to your live secret key in production
			# See your keys here https://dashboard.stripe.com/account/apikeys
			stripe.api_key = "sk_test_tk6tmmWXCJhAf1dIp0wUisuL"
			
			# Get the credit card details submitted by the form
			token = request.form['stripeToken'] if 'stripeToken' in request.form else None

			# Create the charge on Stripe's servers - this will charge the user's card
			try:
				charge = stripe.Charge.create(
			    	amount=500, # amount in cents, again
			    	currency="usd",
			      	source=token,
			      	description="Payment"
			  		  )
			  	session['payment_accepted'] = 1;
			  	session['time_to_pay'] = 1;
			except stripe.error.CardError, e:
				session['payment_accepted'] = -1;
			return render_template("payment.html", status=session['payment_accepted'])
	return render_template("payment.html", status=session['payment_accepted'])

@app.route ("/results",  methods = ["GET","POST"])
def results():
    if ('description' in session.keys() and 'option_1' in session.keys() and "option_2" in session.keys()):
    	arr = output.getFakeResults()
    	return render_template(
    		"results.html",
    		dscr=session["description"],
    		optn1=session["option_1"],
    		optn2=session["option_2"],
    		arr=arr
    		)
    else:
    	return redirect('/')
	return render_template("results.html")

@app.route("/logout")
def logout():
	if "google_user_dict" in session.keys():
		session.pop("google_user_dict")
	return redirect(url_for("index"))

@app.route("/googleoauth", methods = ["POST"])
def googleoauth():
	session["google_user_dict"] = request.json
	return ""

@app.errorhandler(404)
def error400(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
    return render_template("errors/500.html"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)