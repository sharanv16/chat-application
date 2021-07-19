from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def first():
    return render_template('puppy.html')

@app.route('/second/<name>')
def second(name):
    return f'<h1>hi {name.upper()}this is the second page'

app.run(debug=True)
