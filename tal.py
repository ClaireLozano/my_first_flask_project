import os
import sys
import matplotlib.pyplot as plt
import json
import glob




#########################################
##        Create frequence.json        ##
#########################################

def getDataFromTextFile(folder):
	"""
    Get a list of words from html files

    Parameters
    ----------
    folder : str
        Directory path

    Returns
    -------
    object
        {'en': ['IP/09/48', 'Brussels,', '14', 'January', '2009.eu', ...], 'es': [ ... ] }

    """
	dictionnary = {}
	for f in folder:
		pathSplit = '/'.join(f.split('\\')).split('/')
		language = pathSplit[3]
		data = []
		with open(f, encoding="utf8") as inp:
			for line in inp:
				words = line.split()
				for w in words:
					data.append(w)
		if dictionnary.get(language) is not None:
			resToAppend = dictionnary[language]
			dictionnary[language] = dictionnary[language] + data
		else :
			dictionnary[language] = data
	return dictionnary


def sortByWord(words, number):
	"""
    Get a list of the most used words by language

    Parameters
    ----------
    words : str
        List of words
    number : int
        Number of [occurence, words] returned 

    Returns
    -------
    []
        [[276, "de"], [157, "la"], [109, "en"], [91, "y"], ... ]

    """
	dictionnary = {}
	for w in words:
		if len(dictionnary):
			if w in dictionnary.keys():
				dictionnary[w] = dictionnary.get(w) + 1
			else:
				dictionnary[w] = 1
		else : 
			dictionnary[w] = 1
	l = sorted([[y, x] for x,y in dictionnary.items()], reverse=True)
	return l[0:number]


def constructFrequenceFile():
	""" Construct the frequence.json file """
	
	# Get all html file from appr folder
	folderAppr = glob.glob("projet/tal/corpus_multi/*/appr/*.html")

	# Get words from html file
	words = getDataFromTextFile(folderAppr)

	# Write into the json file
	file = open('frequence.json', 'w+')
	file.write("{")
	for language, element in words.items():
		listSortedWords = sortByWord(element, 20)
		file.write('\n\t"' + language + '"' + " : ")
		json.dump(listSortedWords, file)
		file.write(",") 

	file.close()
	file = open('frequence.json', 'ab')
	file.seek(-1, os.SEEK_END)
	file.truncate()
	file.close()

	file = open('frequence.json', 'a')
	file.write("\n}" + "\n")
	file.close()


# Construct frequence.json when run serve
constructFrequenceFile()




#########################################
##     Determine langue from text      ##
#########################################

def findLanguage(listSortedWords, data, n):
	"""
    Determine langue from text

    Parameters
    ----------
    listSortedWords : []
        List of words
    data : json
    	content of json file
        {
			"en" : [[184, "the"], [96, "to"], [95, "in"], [89, "and"], [79, "of"], [36, "is"], [34, "a"], [33, "for"], [30, "on"], [22, ".eu"], [21, "The"], [20, "will"], [19, "be"], [18, "this"], [18, "as"], [18, "EU"], [15, "with"], [14, "that"], [14, "expected"], [14, "by"]],
			"es" : [[276, "de"], [157, "la"], [109, "en"], [91, "y"], [81, "el"], [80, "los"], [74, "a"], [63, "que"], [51, "se"], [51, "del"], [49, "las"], [26, "por"], [25, "al"], [22, "una"], [19, "un"], [19, "para"], [18, ".eu"], [17, "mercado"], [14, "UE"], [13, "precios"]],
			"fr" : [[391, "de"], [245, "la"], [191, "et"], [156, "des"], [148, "les"], [118, "le"], [112, "\u00e0"], [111, "en"], [74, "du"], [57, "dans"], [54, "sur"], [53, "que"], [47, "qui"], [43, "pour"], [43, "plus"], [39, "par"], [37, "une"], [37, "a"], [35, "the"], [34, "l'UE"]],
			"it" : [[288, "di"], [193, "e"], [129, "in"], [120, "a"], [116, "per"], [116, "la"], [112, "il"], [80, "del"], [80, "che"], [62, "le"], [61, "i"], [56, "\u00e8"], [49, "dei"], [48, "un"], [48, "della"], [41, "si"], [41, "delle"], [39, "al"], [36, "nel"], [35, "una"]]
		}

    Returns
    -------
    []
        [[0.375, 'it'], [0.125, 'fr'], [0.125, 'es'], [0.125, 'en']]

    """
	dictionnary = {}
	# For each languages found into the json file
	for key, value in data.items():
		# Return number of similar words
		nbcount = compareWords(listSortedWords, value)
		# Percentage calculation
		res = nbcount/float(n)
		dictionnary[key] = res

	l = sorted([[y, x] for x,y in dictionnary.items()], reverse=True)
	return l


def compareWords(listSortedWords, text):
	"""
    Count occurence of similar words

    Parameters
    ----------
    listSortedWords : []
        List of words
    text : str
        String 

    Returns
    -------
    float
        Number of found occurence

    """
	count = 0
	for w in listSortedWords:
		for v in text:
			if w[1] == v[1]:
				count += 1
	return float(count)


def getDataFromText(text, precision):
	"""
    Parse the text and return percentage of similarity of language per languages 

    Parameters
    ----------
    text : str
        List of words
    precision : int
        integer between 1 and 20 

    Returns
    -------
    []
        [
	        [0.375, 'it'], [0.125, 'fr'], [0.125, 'es'], [0.125, 'en'], 
	        {
				"en" : [[184, "the"], [96, "to"], [95, "in"], [89, "and"], [79, "of"], [36, "is"], [34, "a"], [33, "for"], [30, "on"], [22, ".eu"], [21, "The"], [20, "will"], [19, "be"], [18, "this"], [18, "as"], [18, "EU"], [15, "with"], [14, "that"], [14, "expected"], [14, "by"]],
				"es" : [[276, "de"], [157, "la"], [109, "en"], [91, "y"], [81, "el"], [80, "los"], [74, "a"], [63, "que"], [51, "se"], [51, "del"], [49, "las"], [26, "por"], [25, "al"], [22, "una"], [19, "un"], [19, "para"], [18, ".eu"], [17, "mercado"], [14, "UE"], [13, "precios"]],
				"fr" : [[391, "de"], [245, "la"], [191, "et"], [156, "des"], [148, "les"], [118, "le"], [112, "\u00e0"], [111, "en"], [74, "du"], [57, "dans"], [54, "sur"], [53, "que"], [47, "qui"], [43, "pour"], [43, "plus"], [39, "par"], [37, "une"], [37, "a"], [35, "the"], [34, "l'UE"]],
				"it" : [[288, "di"], [193, "e"], [129, "in"], [120, "a"], [116, "per"], [116, "la"], [112, "il"], [80, "del"], [80, "che"], [62, "le"], [61, "i"], [56, "\u00e8"], [49, "dei"], [48, "un"], [48, "della"], [41, "si"], [41, "delle"], [39, "al"], [36, "nel"], [35, "una"]]
			},
			[[355, ' '], [226, 'e'], [197, 'a'], [168, 'o']]
		]

    """
	jsonFile = "frequence.json"
	with open(jsonFile, 'r', encoding="utf8") as f:
		data = json.load(f)
		f.close()
		
		# Sort word - keep the n most used words
		listSortedWords = sortByWord(text.split(), int(precision))

		# Find the language of a text
		return [findLanguage(listSortedWords, data, int(precision)), data, listSortedWords]