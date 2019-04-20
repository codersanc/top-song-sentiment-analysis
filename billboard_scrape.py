from bs4 import BeautifulSoup
import requests
import json

yearend = 2013

all_my_data = []

while yearend <= 2018:
	print(yearend)
	url = "https://www.billboard.com/charts/year-end/" + str(yearend) + "/hot-100-songs"
	print(url)
	results_page = requests.get(url)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	all_labels = soup.find_all("article", attrs = {'class':'ye-chart-item'})

	for a_div in all_labels:
		# print(a_div)
		# rank = a_div['data-rank']
		mydata = {
			"year-end": yearend,
			"rank" : None,
			"artist_name" : None,
			"song_title" : None
		}
		print(yearend)
		mydata['rank'] = a_div.find('div', attrs = {'class':'ye-chart-item__rank'}).text.replace('\n','')
		mydata['artist_name'] = a_div.find('div', attrs = {'class':'ye-chart-item__artist'}).text.replace('\n','')
		mydata['song_title'] = a_div.find('div', attrs = {'class':'ye-chart-item__title'}).text.replace('\n','')
		
		all_my_data.append(mydata)

	yearend = yearend + 1





		#printing the results/---

		# print('Rank:',rank.text.replace('\n',''))
		# print('Artist:',artist_name.text.replace('\n',''))
		# print('Song:',song_title.text.replace('\n',''))
	
		# print('------------')


my_open_file = open('webscraping_data.json','w')

json.dump(all_my_data,my_open_file,indent=2)

	
	
