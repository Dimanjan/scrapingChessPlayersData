from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time


link="http://ratings.fide.com/advaction.phtml?birthday=&country=NEP&erating=3000&idcode=&line=desc&name=&other_title=&radio=rating&sex=&srating=0&title="

r=requests.get(link)
data=r.text
soup = BeautifulSoup(data, 'html.parser')



long_list=[]
for elements in soup.find_all('tr')[8:-3]:
	column=[]
	for td in elements.find_all('td'):
		val=td.get_text()
		column.append(val)

	long_list.append(column)


link="http://ratings.fide.com/advaction.phtml?idcode=&name=&title=&other_title=&country=NEP&sex=&srating=0&erating=3000&birthday=&radio=rating&ex_rated=&line=desc&inactiv=&offset=100"

for i in range(1,8):
	link=link[:-3] + str(i*100)
	r=requests.get(link)
	data=r.text
	soup = BeautifulSoup(data, 'html.parser')
	time.sleep(1)

	for elements in soup.find_all('tr')[8:-3]:
		column=[]
		for td in elements.find_all('td'):
			val=td.get_text()
			column.append(val)
		long_list.append(column)

df=pd.DataFrame(long_list)
df.to_csv('E:/datasets/nepali_chess_players.csv')
print(df.tail())


