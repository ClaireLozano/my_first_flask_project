# run app : 
# FLASK_APP=init.py flask run
# py init.py

from flask import Flask, render_template, url_for, request

from tal import getDataFromText, constructFrequenceFile

app = Flask(__name__)

posts = [
	{
		'author' : 'Pouet Pouet',
		'title' : 'Blog Post 1',
		'content' : 'Content',
		'date_posted' : 'April 20, 2018',
	},
	{
		'author' : 'John Doe',
		'title' : 'Blog Post 2',
		'content' : 'Content 2',
		'date_posted' : 'April 21, 2018',
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/TALProject")
def talProject():
	return render_template('TALProject.html', data={ 
			'title': 'TAL Project'
		})

@app.route("/TALProject/submit", methods=['POST'])
def talProjectSubmit():
	text = request.form['text']
	precision = request.form['precision']
	[data, frequence] = getDataFromText(text, precision)
	return render_template('TALProject.html', data={
			'text': text, 
			'precision': precision, 
			'title': 'TAL Project',
			'data': data,
			'frequence': frequence
		})

if __name__ == '__main__':
	app.run(debug=True)
