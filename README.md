# Top 20 Song Lyrics Sentiment Analysis
This is the repository for the final project for our Python class at Pratt Institute. 

Sentiment Analysis is the process of determining whether a piece of writing is positive, negative or neutral. In this project, sentiment analysis is performed on the lyrics of the top 20 songs for the last 10 years. Song Title, Artist Name and Year in which the song was on the list were scrapped from billboard.com. Initially, musixmatch API was considered to call to get lyrics for each year’s top 20 songs. However, only 30% of each song’s lyrics could be extracted. Ultimately, Genius API-https://docs.genius.com/ was called to get lyrics of all the song titles scrapped from billboards website. Lexicon-based  approach was used to calculate sentiment analysis for lyrics, where set of positive, negative and neutral words were used to identify polarity for each word in lyrics. Sentiment Analysis was visualized using Tableau Public, where positive and negative value for each song is displayed.

Our Team
--------
Sanchit Kumar | Dilasha Jain | Naman Sehgal

How to make this project work
-----------------------------
1. Install BeautifulSoup -
   "pip install beautifulsoup4"
2. Install lyricsgenius - 
   "pip install lyricsgenius"
3. Run the code - 
   "python3 billboard_scrape.py" - It will create a CSV called 'webscraping_data.csv' - This CSV can be used to feed tableau
4. You can also run the tableau workbook present in this repo - 'Top Song Sentiment Analysis.twbx'
