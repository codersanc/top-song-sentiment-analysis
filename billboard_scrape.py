from bs4 import BeautifulSoup
import requests
import lyricsgenius
import json

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def analyzer(words, total_count):
	posLex=loadLexicon('positive-words.txt')
	negLex=loadLexicon('negative-words.txt')

	num_positive = 0
	num_negative = 0
	num_neutral = 0

	for word in words: #for every word in the review
		if word in posLex: # if the word is in the positive lexicon
			num_positive = num_positive + 1
		if word in negLex: # if the word is in the negative lexicon
			num_negative = num_negative + 1

	positives = num_positive/total_count * 100
	negatives = num_negative/total_count * 100
	neutrals = 100 - (positives + negatives)

	return positives, negatives, neutrals

yearend = 2018

all_my_data = []

while yearend <= 2018:
	url = "https://www.billboard.com/charts/year-end/" + str(yearend) + "/hot-100-songs"
	results_page = requests.get(url)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	all_labels = soup.find_all("article", attrs = {'class':'ye-chart-item'})
	top_10_count = 0
	for a_div in all_labels:
		mydata = {
			"year-end": yearend,
			"rank" : None,
			"artist_name" : None,
			"song_title" : None,
			"words" : None,
			"decision" : None
		}
		print(yearend)
		mydata['rank'] = a_div.find('div', attrs = {'class':'ye-chart-item__rank'}).text.replace('\n','')
		mydata['artist_name'] = a_div.find('div', attrs = {'class':'ye-chart-item__artist'}).text.replace('\n','')
		mydata['song_title'] = a_div.find('div', attrs = {'class':'ye-chart-item__title'}).text.replace('\n','')
		
		genius = lyricsgenius.Genius("SDz9JqIhSC4EmyYkkYUXieoujaqWqffF76nK73StrCPYj5qECgRImHt875qQepq3")
		song = genius.search_song(mydata['song_title'], mydata['artist_name'])
		if song is not None:
			splitLyrics = song.lyrics.split(' ')
			mydata["words"] = len(splitLyrics)
			mydata['decision'] = analyzer(splitLyrics, len(splitLyrics)) # split the lyrics into individual words
		else:
			mydata['decision'] = ""
			mydata["words"] = 0

		all_my_data.append(mydata)
		top_10_count = top_10_count + 1

		if top_10_count == 2:
			break;

	yearend = yearend + 1

my_open_file = open('webscraping_data.json','w')

json.dump(all_my_data,my_open_file,indent=2)