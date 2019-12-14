from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import urlopen 
import re
from datetime import datetime
now = datetime.now() 


book_name = []
author_name = []
book_genre = []
book_ranking = []
dates = []
hour = []
minute = []


url = 'https://ridibooks.com/?genre=general'
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')

book = book_name.extend([soup.find_all('h3','popular_list_title')[n].text.replace('\n썸딜 도서\n\n','').replace(',','')
                         .strip() for n in range(0,12)])
author = author_name.extend([soup.find_all('span','description_author')[n].text.replace(', ','/') for n in range(0,12)])
genre = book_genre.extend([soup.find_all('span','description_tag')[n].text.strip() for n in range(0,12)])
rank = book_ranking.extend(n+1 for n in range(0,12))
for n in range(0,12):
    dates.extend(['%s-%s-%s' % ( now.year, now.month, now.day)]) 
    hour.extend(['%s' % ( now.hour)])
    minute.extend(['%s' % ( now.minute)])



df = pd.DataFrame({ 'dates' : dates,'rank' : book_ranking,'book_name':book_name,'author':author_name, 'genre':book_genre, 'hour' : hour,'minute' : minute })
df = df.reset_index(drop=True)


#df.to_csv('ridibooks_data.csv', mode='w',encoding='utf-8-sig')
df.to_csv('C:\\Users\\jiuu0\\ridibooks_data.csv', mode='a', header=False, encoding='utf-8-sig')
print('%s-%s-%s %s:%s complete.' % ( now.year, now.month, now.day, now.hour, now.minute))