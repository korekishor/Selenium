from bs4 import BeautifulSoup
import requests
url=""
response=requests.get("https://play.google.com/store/apps/details?id=com.imangi.templerun2")
# print(response)

data=BeautifulSoup(response.text,'html.parser')

# print(data)
# link=data.find_all('a',class_="Si6A0c ZD8Cqc")

value=data.find('h1',class_="Fd93Bb ynrBgc xwcR9d").text
ratin=data.find('div',class_="TT9eCd").text
down=data.find('div',class_="wVqUob").text
ot=data.find('div',class_="g1rdde").text

print(value)
print(ratin)
print(down)
print(ot)

