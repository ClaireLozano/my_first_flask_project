# run app : 
# FLASK_APP=init.py flask run
# py init.py

from flask import Flask, render_template, url_for

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
	#data = getDataFromText()
	# text = "Bruxelles, le 15 janvier 2009Marché laitier: la Commission propose des mesures complémentaires d'aide au secteur. À la suite de la récente chute des prix du lait et des produits laitiers, Mme Mariann Fischer Boel, commissaire chargée de l’agriculture, s'est engagée aujourd'hui à introduire de nouvelles mesures de soutien du marché. La semaine prochaine, la Commission réintroduira les restitutions à l'exportation pour le beurre, le fromage ainsi que le lait entier et écrémé en poudre. Lorsque l'achat à l'intervention de beurre et de lait écrémé en poudre débutera en mars, la Commission s'engage, si nécessaire, à acheter davantage que les quantités prédéterminées par les appels d'offres réguliers. En novembre, elle a réintroduit le stockage privé du beurre, applicable à partir du 1er janvier 2009, y compris pour la production du mois de décembre. Celui-ci est donc intervenu plus tôt que d'habitude.  «La chute spectaculaire des prix du lait au cours des derniers mois en a surpris plus d'un» a déclaré Mme Fischer Boel. «J'ai parlé à de nombreux producteurs au cours de mes déplacements dans différents États membres et leur inquiétude est évidente. Il est maintenant temps pour l'Union européenne de les aider. Les mesures introduites dans le cadre du bilan de santé permettront une relance vigoureuse du secteur laitier, mais nous devons agir immédiatement car ce dernier n'entrera en vigueur qu'à la saison prochaine."	
	text = "Bruxelles, 15 gennaio 2009 Mercato alimentare: la Commissione propone misure supplementari per aiutare il settore. In seguito al recente calo dei prezzi del latte e dei prodotti lattiero-caseari, Mariann Fischer Boel, Commissario per l'agricoltura, si è impegnata oggi a introdurre nuove misure di sostegno del mercato. La prossima settimana la Commissione reintrodurrà le restituzioni all'esportazione per burro, formaggio e latte intero e scremato in polvere. Quando l'acquisto di intervento di burro e latte scremato in polvere inizia a marzo, la Commissione si impegna, se necessario, ad acquistare più dei quantitativi predeterminati dai regolari bandi di gara. A novembre, ha reintrodotto l'ammasso privato di burro, applicabile dal 1 ° gennaio 2009, anche per la produzione a dicembre. Questo è intervenuto prima del solito. Il drammatico calo dei prezzi del latte negli ultimi mesi ha sorpreso molti, ha detto Fischer Boel. Ho parlato con molti produttori durante i miei viaggi in diversi Stati membri e la loro preoccupazione è ovvia. È giunto il momento che l'Unione europea li aiuti. Le misure introdotte nell'ambito del controllo sanitario consentiranno una vigorosa ripresa del settore lattiero-caseario, ma dobbiamo agire immediatamente perché non entrerà in vigore fino alla prossima stagione."
	# text = "Ceci est un test rapide pour déterminer le language de ce texte. Bien sur, plus il y aura de texte, plus le programme sera précis. Il faudra aussi éviter les thermes trop technique car il se base sur les mot les plus courant d'un langague."
	# text = "Questo è un test rapido per determinare la lingua di questo testo. Ovviamente, più testo hai, più preciso sarà il programma. Eviterà anche i bagni troppo tecnici perché si basa sulla parola più comune di langague."
	# text = "Esta es una prueba rápida para determinar el idioma de este texto. Por supuesto, cuanto más texto tenga, más preciso será el programa. También evitará que los baños sean demasiado técnicos porque se basa en la palabra más común de langague."
	precision = 8
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
