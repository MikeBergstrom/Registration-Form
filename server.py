from flask import Flask, render_template, request, redirect, flash
import re

app= Flask(__name__)
app.secret_key="sosecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile('^[^0-9]+$')
PASSWORD_REGEX = re.compile('\d.*[A-Z]|[A-Z].*\d')
DATE_REGEX = re.compile('\d{1,2}\/\d{1,2}\/\d{4}$')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/input', methods=['post'])
def input():
    for i in request.form:
        if len(request.form[i]) < 1:
            flash("All fields are required")
            return redirect('/')
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['first']):
        flash("First name must not contain numbers")
        return redirect ('/')
    elif not NAME_REGEX.match(request.form['last']):
        flash("Last name must not contain numbers")
        return redirect ('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        return redirect('/')
    elif request.form['password'] != request.form['confirm']:
        flash("Passwords do not match")
        return redirect('/')
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Password must contain at least one number and one capitol letter")
        return redirect('/')
    elif not DATE_REGEX.match(request.form['birddt']):
        flash("Birth date must be in format MM/DD/YYYY")
        return redirect('/')
    else:
        return redirect('/')
app.run(debug=True)