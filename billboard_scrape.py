from bs4 import BeautifulSoup
import requests
import lyricsgenius
import json

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
			"lyrics" : None
		}
		print(yearend)
		mydata['rank'] = a_div.find('div', attrs = {'class':'ye-chart-item__rank'}).text.replace('\n','')
		mydata['artist_name'] = a_div.find('div', attrs = {'class':'ye-chart-item__artist'}).text.replace('\n','')
		mydata['song_title'] = a_div.find('div', attrs = {'class':'ye-chart-item__title'}).text.replace('\n','')
		
		genius = lyricsgenius.Genius("SDz9JqIhSC4EmyYkkYUXieoujaqWqffF76nK73StrCPYj5qECgRImHt875qQepq3")
		song = genius.search_song(mydata['song_title'], mydata['artist_name'])
		if song is not None:
			mydata['lyrics'] = song.lyrics
		else:
			mydata['lyrics'] = ""

		all_my_data.append(mydata)
		top_10_count = top_10_count + 1

		if top_10_count == 10:
			break;

	yearend = yearend + 1

my_open_file = open('webscraping_data.json','w')

json.dump(all_my_data,my_open_file,indent=2)