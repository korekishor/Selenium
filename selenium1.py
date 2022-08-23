
 
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")

# driver.get("https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/")
# title_name= driver.find_element(By.CLASS_NAME, "darkMode-wrap")

# # print("----------------",title_name)
# by_class_name=driver.find_elements_by_class_name("darkMode-wrap")

# print(by_class_name)

# # assert "multithreading" in title_name

# driver.quit() 


""" 

import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
driver=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")
 
driver.get("https://play.google.com/store/apps/details?id=com.king.candycrushsaga")
 
# print(driver.find_element(By.CLASS_NAME,"VfPpkd-EScbFb-JIbuQc UVEnyf"))

# web_data=driver.find_element_by_class_name("oVnAB")
# print("--------------------------------")

print("-----------",driver.title)
serch=driver.find_element_by_class_name("f0UV3d")
print("--------------------2")
serch.send_keys("candu crash saga")
print("--------------------3")

serch.send_keys(Keys.RETURN)

# print("--------------------4",driver.page_source)

time.sleep(5)

driver.quit()
"""


  
""" 
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import workbook
import re
 
driver=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")
 
driver.get("https://play.google.com/store/apps/collection/cluster?gsr=SjxqGGhsanhqMUROaGI3dUFpOTZQV04wclE9PcICHwobChdjb20ua2luZy5jYW5keWNydXNoc2FnYRAHGAg%3D:S:ANO1ljJ54YA")
print("----------------------------2")

# print(driver.page_source)
# link=driver.find_element_by_class_name("ftgkle")
# print("----------------------------3")
# print(link.find_element_by_class_name(""))
# print("----------------------------4")

# continue_link = driver.find_element_by_tag_name('a')
# print(continue_link)
links = driver.find_elements_by_xpath("//*[@href]")
rating= driver.find_elements_by_xpath("//*[@aria-label]")
app_name=driver.find_element_by_xpath("//*[@class]")
c=0



for r in rating:
    rating=r.get_attribute("Text")
    # print("----------",rating)

    match=re.findall("\d{1}\.\d{1}",rating)

    print("---------------",match)
    c+=1

#x = str(continue_link)
#print(continue_link)
# print("3---------------------------",elem)
c,j=0,0
for i in links:
    if c>0 :

        j+=1
        # print(j,"__________",i.get_attribute("href"))
    # print(c,"__________",i.get_attribute("href"))
    c=c+1

# time.sleep(5)
driver.quit()
 
"""



"""
from inspect import findsource
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
driver=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")
 
driver.get("https://play.google.com/store/apps/details?id=com.king.candycrushsaga")

# print(driver.page_source)
# link=driver.find_element_by_class_name("ftgkle")
# print("----------------------------3")
# print(link.find_element_by_class_name(""))
# print("----------------------------4")

continue_link = driver.find_element_by_tag_name('a')
elem = driver.find_elements_by_xpath("//*[@href]")

#x = str(continue_link)
#print(continue_link)


print("lenght :",len(elem))
c,j,list_of_link=0,0,[]
for i in elem:
    
    href=i.get_attribute("href")
    if c > 148: 
        if "details?id=com" in href:
            print(c,"----------------------",href)
            driver1=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")

            driver1.get(href)
            print("----------",href)
            continue_link1 = driver.find_element_by_tag_name('a')
            elem1 = driver1.find_elements_by_xpath("//*[@href]")

            
            for i in elem1:
                href1=i.get_attribute("href")
                # if href not in list_of_link:
                #     list_of_link.append(href)
                print(j,"------------",href1)
                j+=1
            
            driver1.close()
    c=c+1

#https://play.google.com/store/apps/collection/cluster?gsr=SjxqGFNPK1VoL2FYUkRuSWUrRmUwUWhQTlE9PcICHwobChdjb20ua2luZy5jYW5keWNydXNoc2FnYRAHGAg%3D:S:ANO1ljIVsU4

# time.sleep(5)
driver.quit()
s=0
for link1 in list_of_link:
    print(s,"-----$$------",link1)
    s+=1

"""



import pathlib
from inspect import findsource
from pydoc import text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import requests
from bs4 import BeautifulSoup
 
driver=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://play.google.com/store/games?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-in-1003227-med-hasem-py-Evergreen-Oct0121-Text_Search_BKWS-BKWS%7CONSEM_kwid_43700065205026376_creativeid_535350509651_device_c&gclid=EAIaIQobChMIpvWVsPy5-QIVD6-WCh18VArtEAAYASAAEgJUyvD_BwE&gclsrc=aw.ds")

SCROLL_PAUSE_TIME = 0.5
c=0
# Get scroll height

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    continue_link = driver.find_element_by_tag_name('a')
    
    # Scroll down to bottom
    elem = driver.find_elements_by_xpath("//*[@href]")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

klist=[]
for i in elem:
    # print("---------------------------3",i.get_attribute("href"))
    href1=i.get_attribute("href")
    if "details?id" in href1:
        print("+++++++++++++++++++++++++++++++",href1)
        r = requests.get("{}".format(href1))
        data = r.content  
        soup = BeautifulSoup(data, "html.parser")
        
        for link in soup.find_all('a', attrs={'href': re.compile("^/store/apps/collection/cluster")}):
            similar_app_link = "https://play.google.com" + link.get('href')
            break

        driver1=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")
        
        driver1.get("{}".format(similar_app_link))

        SCROLL_PAUSE_TIME = 3
        last_height = driver1.execute_script("return document.body.scrollHeight")


        while True:
            continue_link = driver1.find_element_by_tag_name('a')
            
            # Scroll down to bottom
            elem1 = driver1.find_elements_by_xpath("//*[@href]")
            driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        for link in elem1:
            link3=link.get_attribute("href")
            if "details?id" in link3:
                print(c,"-------------",link.get_attribute("href"))
                klist.append(link.get_attribute("href"))
                r1 = requests.get("{}".format(link3))
                data1 = r1.content  
                soup1 = BeautifulSoup(data1, "html.parser")
                try:
                    print("**************")
                    ot=soup1.find('div',class_="g1rdde").text
                    value=soup1.find('h1',class_="Fd93Bb ynrBgc xwcR9d").text
                    print(ot)
                    print(value)
                except:
                    try:
                        print(")))))))))")
                        ot=soup1.find('div',class_="g1rdde").text
                        print("$$$$$$")
                        value=soup1.find('h1',class_="Fd93Bb F5UCq xwcR9d").text
                        print(ot)
                        print(value)
                    except:
                        pass
                # for data in soup1.find_all('div',class_="P9KVBf"):

                #     Movie_name1=data.find('h1',class_="Fd93Bb F5UCq xwcR9d")
                    # print(Movie_name1.find("span"))
                    # price=data.find_all('div',class_="ClM7O")
                    # rating=data.find_all('div',class_="TT9eCd")
                    # print(str(Movie_name1))
                    # print(str(price.text))
                    # print(str(rating))
                c+=1
                
            
        driver1.close()


driver.close()





# for i in list:
#     print(i)
# import requests  
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# import re

# first_page_link=[]

# driver=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver.get("https://play.google.com/store/apps/collection/cluster?gsr=Sjk6HQobChdjb20ua2luZy5jYW5keWNydXNoc2FnYRAHahhPVHBvWHpTTEc0V0xkYXp4V016MGdnPT0%3D:S:ANO1ljLGiCs")

# # driver.find_element_by_class_name()
# SCROLL_PAUSE_TIME = 0.5


# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")


# while True:
#     continue_link = driver.find_element_by_tag_name('a')
    
#     # Scroll down to bottom
#     elem = driver.find_elements_by_xpath("//*[@href]")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#     print("---------------------------------1")
# for i in elem:
#     href1=i.get_attribute("href")
#     if "details?id" in href1:
#         print(href1)
#         first_page_link.append(href1)
# driver.close()

# c=0
# for link1 in first_page_link:
#     # print(link)
#     c=c+1
#     if c>5:
#         break

#     response=requests.get("{}".format(link1))
#     soup=BeautifulSoup(response.text,'html.parser')
#     link=('a',soup.find(class_="WpHeLc VfPpkd-mRLv6"))

    # '''match=re.findall('href=.*"',str(link))'''
    
    # print("------------",link)

    # new_data=match[0][6:len(match[0])-7]
    # new_data="https://play.google.com/"+new_data
    # print("--------",new_data)




# import requests  
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# import re
# from selenium.webdriver.common.by import By

# driver1=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")
# href1="https://play.google.com/store/apps/details?id=com.king.candycrush4"
# driver1.get("{}".format(href1))
 
# driver1.maximize_window()
 
# element = driver1.find_element_by_xpath("//a[@aria-label='See more information on Similar games']")
# es=driver1.find_element_by_partial_link_text(element)
# print("-------------------------------------------",es)


# SCROLL_PAUSE_TIME = 0.5
# driver1.close()


# import re
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://play.google.com/store/apps/details?id=com.blackout.word")
# data = r.content  # Content of response
# soup = BeautifulSoup(data, "html.parser")

# # link=soup.find(class_='WpHeLc VfPpkd-mRLv6')
# for link in soup.find_all('a', attrs={'href': re.compile("^/store/apps/collection/cluster")}):
#             link_of_similar_app_page = "https://play.google.com" + link.get('href')
#             # print("https://play.google.com",link.get('href'))
#             print(link_of_similar_app_page)
# # print(link)

# for i in soup.find_all('div',{'class':'VfPpkd-Bz112c-J1Ukfc-LhBDec'}):
#    link = i.find('a',href=True)
#    print(link)
#    if link is None:
#        continue
    # print(i.href)
  