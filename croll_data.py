from lib2to3.pgen2 import driver
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\Kishor Kore\\Downloads\\chromedriver_win32\\chromedriver.exe")


driver.get("https://play.google.com/store/apps/collection/cluster?gsr=SjxqGEZiN2pXZE0wY1IrbUNXUjM3VFFJQ0E9PcICHwobChdjb20ua2luZy5jYW5keWNydXNoc2FnYRAHGAg%3D:S:ANO1ljIdRk0&hl=en_IN&gl=US")

driver.maximize_window()

# driver.execute_script("window.scrollBy(0,1000)","")

#  scroll dowon till end
flag=driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz[3]/div/div/c-wiz/div/c-wiz/c-wiz/c-wiz/section/div/div/div/div/div/div[141]/div/div/a/div[1]/img")

driver.execute_script("arguments[0].scrollIntoView();",flag)