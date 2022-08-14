# from selenium.webdriver.common.by import By
#
# from drugs import drugs
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")
# driver.implicitly_wait(1)
# driver.get("https://www.google.com/")
#
#
#
#
#
#


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#set chromodriver.exe path
from drugs import drugs

driver = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.google.com/")
#identify search box
m = driver.find_element(By.NAME,"q")
#enter search text
m.send_keys("Aбилифй описание ")
# driver.find_element(By.CLASS_NAME , 'Tg7LZd').click()
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)


# driver.close(3)