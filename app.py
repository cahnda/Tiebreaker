#Code for App Framework
#References: Tour-De-City (Previous Flask Framework Implemented by David Cahn)

from flask import Flask, render_template, request, redirect, session, url_for
from py import *
# import getKeys, os, stripe, json, datetime, random
import os, stripe, json, datetime, random
import returnResults

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/contact", methods = ["GET"])
def contact():
    return render_template("contact.html")

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
            errString = ""
            if len(session['description']) == 0:
                errString += "Please include a description. "
            if len(session['option_1']) == 0:
                errString += "Please include a value for Option 1. "
            if len(session['option_2']) == 0:
                errString += "Please include a value for Option 2. "
            if len(errString) != 0:
                return render_template('input.html', error=errString)
            session['time_to_pay'] = 0;
            session['loaded_data'] = 0;
            session['payment_accepted'] = 0;
            session['added_DB'] = 0
            return redirect('/payment')
    return render_template("input.html")


@app.route ("/payment",  methods = ["GET","POST"])
def payment():
    if (session['loaded_data'] == 0 and session['payment_accepted']):
        #Implement Query Here
        print ("start loading")
        timeVal  = utils.useTime()
        #session['data_array'] = utils.getActualData(session['option_1'],session['option_2'])
        os.environ["JAVA_HOME"] = "/usr"
        HIT_ID = int(utils.get_random_ID())
        num_results = 5
        session['num_results'] = num_results
        os.system("python mturk.py arg1 arg2 " + str(num_results) + " " + str(HIT_ID))
        print HIT_ID
        #Replace with call to 
        if (timeVal == 0):
            print ("finished loading")
            session['loaded_data'] = 1
            return redirect('/results')
    if not('time_to_pay' in session and session['time_to_pay'] == 0):
        return redirect("input")
    if (session['payment_accepted'] == 0): 
        if not request.method == "GET":
            # Set your secret key: remember to change this to your live secret key in production
            # See your keys here https://dashboard.stripe.com/account/apikeys
            stripe.api_key = getKeys.stripePrivate()
            # Get the credit card details submitted by the form
            token = request.form['stripeToken'] if 'stripeToken' in request.form else None

            # Create the charge on Stripe's servers - this will charge the user's card
            try:
                charge = stripe.Charge.create (
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
        currentResults = returnResults.main()
        session["currentResults"] = currentResults
        for x in session["currentResults"]: 
            print x
        queryResults = currentResults.get("0")
        print "CURRENT RESULTS LENGTH"
        print len(currentResults)
        print "QUERY RESULTS LENGTH"
        if not queryResults:
            return render_template("index.html", error = "No query results.")
        print len(queryResults)
        session['data_array'] = utils.getTurkResults(queryResults)
        arr = session['data_array']
        if (session['added_DB'] == 0):
            try:
                utils.add_mongo_result(
                session["google_user_dict"]["id"],
                session["description"],
                session["option_1"],
                session["option_2"],
                arr)
            except:
                utils.add_mongo_result(
                "Anon",
                session["description"],
                session["option_1"],
                session["option_2"],
                arr)
            session['added_DB'] = 1
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


@app.route ("/account",  methods = ["GET","POST"])
def account():
    if "google_user_dict" in session:
        myName = session["google_user_dict"]["displayName"]
        myID = session["google_user_dict"]["id"]
        results = sorted(utils.get_my_results(myID), 
            key=lambda x: datetime.datetime.strptime(x['time'], "%Y-%m-%d %H:%M:%S"))
        return render_template("account.html",name=myName,allResults=results)
    else: 
        return redirect('/')

@app.route("/result=<result_id>", methods=["GET", "POST"])
def showResult(result_id):
    if request.method == "GET":
        print ID
        result = utils.get_mongo_result(result_id)
        data = result["html_data"]
        dsc = result["description"]
        opt1 = result["option_1"]
        opt2 = result["option_2"]
        return render_template(
            "results.html", 
            dscr=dsc,
            optn1=opt1,
            optn2=opt2,
            arr=data
            )

@app.route("/logout")
def logout():
    if "google_user_dict" in session.keys():
        session.pop("google_user_dict")
    return redirect(url_for("index"))

@app.route("/googleoauth", methods = ["POST"])
def googleoauth():
    session["google_user_dict"] = request.json
    #print session["google_user_dict"]
    return ""

@app.errorhandler(404)
def error400(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
    return render_template("errors/500.html"), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)