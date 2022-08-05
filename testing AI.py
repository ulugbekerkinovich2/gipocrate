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
        # if i == 140:
        #     break
# continue
# print(list_links)
for i in list_links:
    driver.get(f'{i}')
    kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
    kasallik_nomi1 = kasallik_nomi.capitalize()

    # print(kasallik_nomi1)
    # if not i == "https://illness.docdoc.ru/pnevmonia_atipichnaya" or i == 'https://illness.docdoc.ru/mialgija' or i == 'https://illness.docdoc.ru/narkomania' or i == 'https://illness.docdoc.ru/nevrit' or i == 'https://illness.docdoc.ru/ozhirenie' or i == 'https://illness.docdoc.ru/otomikoz' or i == 'https://illness.docdoc.ru/paranoiya' or i == 'https://illness.docdoc.ru/rozatsea' or i == 'https://illness.docdoc.ru/rozha' or i == 'https://illness.docdoc.ru/perikardit' or i == 'https://illness.docdoc.ru/periodontit' or i == 'https://illness.docdoc.ru/sarkoidoz' or i == 'https://illness.docdoc.ru/takhikardiya' or i == 'https://illness.docdoc.ru/holera' or i == 'https://illness.docdoc.ru/kista_meniska' or i == 'https://illness.docdoc.ru/ekhinokokkoz' or i == 'https://illness.docdoc.ru/iazvennyi_kolit' or i == 'https://illness.docdoc.ru/yachmen' or i == 'https://illness.docdoc.ru/jashhur' or i == 'https://illness.docdoc.ru/Gigroma' or i == 'https://illness.docdoc.ru/girsutizm' or i == 'https://illness.docdoc.ru/depression' or i == 'https://illness.docdoc.ru/cinga' or i == 'https://illness.docdoc.ru/giperplazija_jendometrija':
    # nomi = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.CLASS_NAME,
    #                                                                                   'illnes-short-description').text
    # print(nomi)

    hammasi = driver.find_element(By.XPATH, '//*[@id="diseases_article_static_content"]').text
    banner = driver.find_element(By.CLASS_NAME, 'banner-view-all-doctors').text
    print(banner)

    hammasi1 = hammasi.split('.')
    # print(colored(hammasi, 'cyan'))
    # print(hammasi1[0])

    # break
    gacha = []
    a = ""

    for i in range(0, len(hammasi1)):
        a = hammasi1[i]
        b = a.split()
        for j in range(1, len(b)):
            if '\n' in b:
                b.replace('\n', ' ')
        prichina = "Причины"
        print("b",b)
        print(len(hammasi1))
    for k in range(0, len(hammasi1)):
        gacha.append(b[k])
        print("bita",b[k])
        if prichina == b[k][0]:
            break

        a = " ".join(gacha)
    hammasi1[i] = a
    print(gacha)
    print(a)
    break

driver.close()
