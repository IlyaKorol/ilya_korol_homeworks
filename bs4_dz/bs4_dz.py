import requests
from bs4 import BeautifulSoup
import fake_useragent
import csv
from itertools import zip_longest

url = 'https://www.21vek.by/mobile/iphone_15/'
user = fake_useragent.UserAgent().random
headers = {'user-agent':user}
response = requests.get(url,headers=headers)
page_html = response.text

soup = BeautifulSoup(page_html, 'lxml')
all_ph = soup.find('div',{'class':'style_container__TFmIX'})
name = all_ph.find_all('p',{'data-testid':'card-info'})
price = all_ph.find_all('p',{'data-testid':'card-current-price'})
list_name = []
list_gb = []
list_price = []
for i in name:
    a = i.text.split(' ')
    del a[4]
    b = ' '.join(a)
    list_name.append(b)
    new_list_name = list_name[:-3]
    for j in i.text.split(' '):
        if j == '128GB' or j == '256GB' or j == '512GB':
            list_gb.append(int(j[:-2]))
            new_list_gb = list_gb[:-3]
for i in price:
    list_price.append(float(i.text[:-3].replace(' ','').replace(',','.')))

data = [new_list_name,new_list_gb,list_price]
export_data = zip_longest(*data, fillvalue = '')
with open('table.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(("name", "GB", "price"))
    write.writerows(export_data)

import pandas as pd
df = pd.read_csv('table.csv')
mob1 = df[df['GB']==128]
mob1_min = mob1.min()
mob2 = df[df['GB']==256]
mob2_min =mob2.min()
print(mob1_min,mob2_min)


