# web scrapping 

'''
try working
try:
    a= 1/0
    print(a)
except Exception as e:
    print("pleachage change the value by 0")
    print(e)'
'''

import time
import sys
from bs4 import BeautifulSoup
import requests

'''
try:
    page=requests.get('https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database/2022')

except Exception as e:
         print(e)'''
    
time.sleep(2)

soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div',attrs={'class' :'arrowed-link'})

page


soup

links

data_link=soup.find_all('div',attrs={'class' :'arrowed-link'})

links[0]

links[0].text


links[0].a

data_link=links[0].a['href']

data_link

import pandas as pd


'https://www.who.int' + data_link

soup2=BeautifulSoup(page.text,'html.parser')
#links1=soup.find_all('div',attrs={'class' :'sf-content-block content-block'})
links2=soup2.find_all('p',attrs={'class' :''})

print(soup2.prettify())

links2

path=links2[7].p.a['href']

path

r = requests.get(path)

r

  #C:\Users\hp\Desktop
f_name='air_quality'

with open(f'C:/Users/hp/Desktop/Data_Science_Internship/New_Web/{f_name}.xlsx', 'wb') as f:
    f.write(r.content)

    
import pandas as pd

Air=pd.read_excel('New_Web/air_quality.xlsx' ,sheet_name=1)


Air


