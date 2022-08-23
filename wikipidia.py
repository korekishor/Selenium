from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/Data_science"

respons=requests.get(url)

print(respons)

soup=BeautifulSoup(respons.content,"html.parser")
print(soup.title) 
all_ancle_tag=soup.find_all('a')

for i in all_ancle_tag:
    # print(i.text)
    pass
link_list=[]
for data in soup.find_all('sup',class_="reference"):
    link=data.find_all('a')
    link_list.append(link)
    
# print(link_list)    
    # print("------------------")
    # para=data.find_all('div',class_="mw-indicators")
    # print("-----------------",para)
    
    # print(data)

for i in link_list:
    print(i)



