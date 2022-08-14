import sqlite3

from selenium import webdriver
from selenium.webdriver.common.by import By

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
driver = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")

driver.get("https://www.vidal.ru/")
links = driver.find_elements(By.TAG_NAME, 'a')
list_links = []
i = 0
for lnk in links:
    # print(lnk.get_attribute("href"), i)
    a = lnk.get_attribute('href')

    if 19 <= i < 321:
        list_links.append(a)
    i += 1

list_all_links = []
print(list_links)
for lnk1 in list_links:
    drivers = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")
    drivers.get(f"{lnk1}")
    linkks1 = drivers.find_elements(By.TAG_NAME, 'a')
    for j in linkks1:
        c = j.get_attribute('href')

        list_all_links.append(c)
    print(list_all_links)

#     b = lnk1.get_attribute('href')
#     # print(b)
#     driver.implicitly_wait(10)
    # driver.find_element(By.XPATH, '')


driver.close()
