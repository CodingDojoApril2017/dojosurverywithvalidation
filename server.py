from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def firstpage():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    if session['counter'] == 1:
        session['flashmsg'] = ''
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def create_user():

    if request.form['comments'] == '' and request.form['name'] == '':
        session['flashmsg'] = flash("Name cannot be empty!" + '\n' + "Please fill out the comment section")
        session['counter'] = 0
        return redirect('/')

    if request.form['name'] == '':
        session['flashmsg'] = flash("Name cannot be empty!")
        session['counter'] = 0
        return redirect('/')

    if request.form['comments'] == '':
        session['flashmsg'] = flash("Please fill out the comment section")
        session['counter'] = 0
        return redirect('/')

    if len(request.form['comments']) >= 120:
        session['flashmsg'] = flash("Please keep comments under 120 characters")
        session['counter'] = 0
        return redirect('/')

    return render_template('results.html')
    name = request.form['name']
    dloc = request.form['dloc']
    favlang = request.form['favlang']
    comments = request.form['comments']



app.run(debug=True)
