from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")

driver.get("https://illness.docdoc.ru/")
links = driver.find_elements(By.TAG_NAME, 'a')
list_links = []
i = 0
while i < 700:
    for lnk in links:
        # print(lnk.get_attribute("href"), i)
        a = lnk.get_attribute('href')
        if 31 <= i < 661:
            list_links.append(a)
        i += 1
description = []
for i in list_links:
    driver.get(f'{i}')
    kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
    if kasallik_nomi in driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                   'p').text:
        kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                     'p').text
        print(kasallik_haqida)
        for i in range(1, 10):
            if driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[i].text:
                description.append(driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[i].text)



driver.close()
