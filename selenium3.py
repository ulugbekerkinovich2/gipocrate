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
        if i == 140:
            break

# continue
# print(list_links)
for i in list_links:
    driver.get(f'{i}')
    if i == 'https://illness.docdoc.ru/beshenstvo' or i == 'https://illness.docdoc.ru/bolezn_gjuntera' or i == 'https://illness.docdoc.ru/bolezn_uippla' or i == 'https://illness.docdoc.ru/borodavki' or i == 'https://illness.docdoc.ru/bolezn_hantingtona' or i == 'https://illness.docdoc.ru/bolezn_Shljattera':
        continue
    # if i in list_links:
    #     continue
    try:
        if driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Абсцесс':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + "\n" + kasallik_sabablari1
            print(1, kasallik_sabablari2)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(1.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                4].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(1.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                5].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                6].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(1.3, davolanish3)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Авитаминоз':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(2, kasallik_sabablari2)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(2.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                4].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(2.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                7].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                8].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(2.3, davolanish3)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аденовирус':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(3, kasallik_sabablari3)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(3.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                5].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(3.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                7].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                8].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(3.3, davolanish3)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == "Аденома гипофиза":
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(4, kasallik_sabablari3)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[12].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_sabablari1 + '\n' + kasallik_asoratlari2
            print(4.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                28].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[20].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[29].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[21].text
            diagnostika4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[30].text
            diagnostika5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[31].text
            diagnostika6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[32].text
            diagnostika7 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6
            print(4.2, diagnostika7)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                33].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[22].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                34].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                35].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                36].text
            davolanish5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[23].text
            davolanish6 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5
            print(4.3, davolanish6)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == "Аденома простаты":
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(5, kasallik_sabablari4)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[10].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_asoratlari7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_asoratlari8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[12].text
            kasallik_asoratlari10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari11 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari12 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari13 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8 + '\n' + kasallik_asoratlari9 + '\n' + kasallik_asoratlari10 + '\n' + kasallik_asoratlari11 + '\n' + kasallik_asoratlari12
            print(5.1, kasallik_asoratlari13)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                17].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[18].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(5.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                21].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                22].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                23].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                23].text
            davolanish4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                24].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                25].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(5.3, davolanish7)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == "Аденома щитовидной железы":
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME, 'ul').text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = kasallik_sabablari + "\n" + kasallik_sabablari1
            print(6, kasallik_sabablari2)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(6.1, kasallik_asoratlari3)

            diagnostika = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[12].text
            print(6.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                13].text
            print(6.3, davolanish)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аденомиоз':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            print(7, kasallik_sabablari)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(7.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                4].text
            print(7.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                5].text
            print(7.3, davolanish)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аднексит':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_sabablari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_sabablari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_sabablari7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            kasallik_sabablari8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_sabablari9 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6 + '\n' + kasallik_sabablari7 + '\n' + kasallik_sabablari8
            print(8, kasallik_sabablari9)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(8.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                17].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[18].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            diagnostika4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[21].text
            diagnostika5 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4
            print(8.2, diagnostika5)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                23].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                24].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                25].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                26].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                27].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                28].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                29].text
            davolanish7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            davolanish8 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7
            print(8.3, davolanish8)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Акромегалия':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME, 'ul').text
            print(9, kasallik_sabablari)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            print(9.1, kasallik_asoratlari)

            diagnostika = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            print(9.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                3].text
            print(9.3, davolanish)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Алалия':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_sabablari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_sabablari5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[8].text
            kasallik_sabablari6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_sabablari7 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + kasallik_sabablari6
            print(10, kasallik_sabablari7)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[17].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[14].text
            kasallik_asoratlari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            kasallik_asoratlari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[21].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(10.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                31].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                      'ol').text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[32].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[7].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(10.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                34].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                35].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                36].text
            davolanish3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[8].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                37].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                38].text
            davolanish6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[9].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(10.2, davolanish7)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Алкоголизм':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_sabablari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_sabablari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_sabablari5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_sabablari6 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5
            print(11, kasallik_sabablari6)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(11.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                16].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[17].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(11.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                18].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                19].text
            davolanish3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                20].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                21].text
            davolanish6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(11.3, davolanish7)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аллергия':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            kasallik_sabablari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_sabablari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[5].text
            kasallik_sabablari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[11].text
            kasallik_sabablari5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[6].text
            kasallik_sabablari6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[12].text
            kasallik_sabablari7 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6
            print(12, kasallik_sabablari7)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[7].text
            kasallik_asoratlari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[8].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(12.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                17].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[18].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[9].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(12.2, diagnostika4)

            davolanish = kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[10].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                21].text
            davolanish3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                22].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                23].text
            davolanish6 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5
            print(12.3, davolanish6)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аллергия инсектная':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            print(13, kasallik_sabablari)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(13.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                7].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(13.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                8].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                10].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(13.3, davolanish3)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аллергия лекарственная':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(14, kasallik_sabablari3)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(14.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                7].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[5].text
            diagnostika4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            diagnostika5 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4
            print(14.2, diagnostika5)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                10].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[6].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                11].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(14.3, davolanish3)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аллергия пищевая':
            kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'p').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(15, kasallik_sabablari3)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(15.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                5].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(15.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                7].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                8].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                9].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(15.3, davolanish4)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Алопеция':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(16, kasallik_sabablari2)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(16.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            print(16.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish5 = davolanish + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4
            print(16.3, davolanish5)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Алопеция андрогенная':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(17, kasallik_sabablari4)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(17.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(17.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(17.3, davolanish3)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Алопеция очаговая':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(18, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_sabablari1 + '\n' + kasallik_asoratlari2
            print(18.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(18.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(18.3, davolanish2)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Альвеолит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(19, kasallik_sabablari4)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(19.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(19.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[6].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(19.3, davolanish3)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Альгоменорея':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(20, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_sabablari1
            print(20.1, kasallik_sabablari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(20.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(20.3, davolanish2)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Амблиопия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(21, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(21.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            print(21.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(21.3, davolanish2)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аменорея':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4
            print(22, kasallik_sabablari5)

            kasallik_asoratlari = kasallik_sabablari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                    By.TAG_NAME, 'p')[5].text
            print(22.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            print(22.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(22.3, davolanish3)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Амилоидоз':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(23, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(23.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(23.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(23.3, davolanish3)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Амнезия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(24, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(24.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(24.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(24.3, davolanish2)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анальная трещина':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(25, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(25.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(25.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(25.3, davolanish4)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Анальный зуд':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(26, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_sabablari1
            print(26.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(26.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(26.3, davolanish3)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анафилактический шок':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(27, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_sabablari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(27.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(27.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(27.3, davolanish4)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Ангина':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(28, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_sabablari2
            print(28.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            print(28.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(28.3, davolanish2)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Ангиома':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(29, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_asoratlari9 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8
            print(29.1, kasallik_asoratlari9)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            diagnostika6 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5
            print(29.2, diagnostika6)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[6].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[7].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[8].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish8 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7
            print(29.3, davolanish8)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анемия (низкий гемоглобин)':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_sabablari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_sabablari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_sabablari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            kasallik_sabablari9 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6 + '\n' + kasallik_sabablari7 + '\n' + kasallik_sabablari8
            print(30, kasallik_sabablari9)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[9].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[10].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            kasallik_asoratlari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            kasallik_asoratlari11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            kasallik_asoratlari13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            kasallik_asoratlari14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            kasallik_asoratlari15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            kasallik_asoratlari16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            kasallik_asoratlari17 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            kasallik_asoratlari18 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            kasallik_asoratlari19 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            kasallik_asoratlari20 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            kasallik_asoratlari21 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            kasallik_asoratlari22 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            kasallik_asoratlari23 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            kasallik_asoratlari24 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            kasallik_asoratlari25 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[37].text
            kasallik_asoratlari26 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            kasallik_asoratlari27 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8 + '\n' + kasallik_asoratlari9 + '\n' + kasallik_asoratlari10 + '\n' + kasallik_asoratlari11 + '\n' + kasallik_asoratlari12 + '\n' + kasallik_asoratlari13 + '\n' + kasallik_asoratlari14 + '\n' + kasallik_asoratlari15 + '\n' + kasallik_asoratlari16 + '\n' + kasallik_asoratlari17 + '\n' + kasallik_asoratlari18 + '\n' + kasallik_asoratlari19 + '\n' + kasallik_asoratlari20 + '\n' + kasallik_asoratlari20 + '\n' + kasallik_asoratlari21 + '\n' + kasallik_asoratlari22 + '\n' + kasallik_asoratlari23 + '\n' + kasallik_asoratlari24 + '\n' + kasallik_asoratlari25 + '\n' + kasallik_asoratlari26
            print(30.1, kasallik_asoratlari27)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[39].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[40].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[41].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[42].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[43].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[21].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[44].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[45].text
            diagnostika9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[22].text
            diagnostika10 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8 + '\n' + diagnostika9
            print(30.2, diagnostika10)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[46].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[47].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[32].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[48].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[49].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[50].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[51].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[52].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[53].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[54].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[24].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[55].text
            davolanish12 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11
            print(30.3, davolanish12)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анемия железодефицитная':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(31, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(31.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(31.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(31.2, davolanish2)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аномалия Кимерли':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(32, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(32.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika8 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7
            print(32.2, diagnostika8)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[6].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[7].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[8].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(32.3, davolanish7)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аноргазмия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(33, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(33.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            print(33.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(33.3, davolanish3)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Анорексия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(34, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(34.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[6].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika6 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5
            print(34.2, diagnostika6)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text

            davolanish6 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4
            print(34.3, davolanish6)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Апатия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(35, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(35.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            print(35.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(35.3, davolanish4)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Апноэ':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(36, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(36.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(36.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[7].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(36.3, davolanish3)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аппендицит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(37, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(37.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            diagnostika8 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7
            print(37.2, diagnostika8)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[6].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanis4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish5 = davolanish +'\n'+ davolanish1 +'\n'+ davolanish2 +'\n'+ davolanish3 +'\n'+ davolanish4
            print(37.3, davolanish5)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Апраксия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            print(38, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari +'\n'+ kasallik_asoratlari1
            print(38.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika2 = diagnostika +'\n'+ diagnostika1
            print(38.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = davolanish +'\n'+ davolanish1 +'\n'+ davolanish2
            print(38.3, davolanish2)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аритмия дыхания':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(39, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari3 = kasallik_asoratlari +'\n'+ kasallik_asoratlari1 +'\n'+ kasallik_asoratlari2
            print(39.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika3 = diagnostika +'\n'+ diagnostika1 +'\n'+ diagnostika2
            print(39.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish2 = davolanish +'\n'+davolanish1
            print(39.3, davolanish2)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аритмия сердца':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(40, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari +'\n'+ kasallik_asoratlari1
            print(40.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika2 = diagnostika +'\n'+ diagnostika1
            print(40.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = davolanish +'\n'+ davolanish1
            print(40.3, davolanish2)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артериальная гипертензия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(41, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari +'\n'+ kasallik_asoratlari1
            print(41.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika2 = diagnostika +'\n'+ diagnostika1
            print(41.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = davolanish +'\n'+ davolanish1
            print(41.3, davolanish2)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артериальная гипертония':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[8].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[9].text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(42, kasallik_sabablari4)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari4 = kasallik_asoratlari +'\n'+ kasallik_asoratlari1 +'\n'+ kasallik_asoratlari2 +'\n'+ kasallik_asoratlari3
            print(42.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            diagnostika9 = diagnostika +'\n'+ diagnostika1 +'\n'+ diagnostika2 +'\n'+ diagnostika3 +'\n'+ diagnostika4 +'\n'+ diagnostika5 +'\n'+ diagnostika6 +'\n'+ diagnostika7 +'\n'+ diagnostika8
            print(42.3, diagnostika9)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text









        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артериальная гипотензия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_sabablari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_sabablari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_sabablari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_sabablari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text

            kasallik_sabablari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            kasallik_sabablari11 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6 + '\n' + kasallik_sabablari7 + '\n' + kasallik_sabablari8 + '\n' + kasallik_sabablari9 + '\n' + kasallik_sabablari10
            print(43, kasallik_sabablari11)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артрит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(44, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Астения (астенический синдром)':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(45, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Астенопия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            print(46, kasallik_sabablari)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Астигматизм':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(47, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Асцит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4
            print(48, kasallik_sabablari5)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атаксия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(49, kasallik_sabablari4)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атерома':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(50, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атеросклероз':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[0].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(51, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атония мочевого пузыря':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(52, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аутизм':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(53, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аутоиммунный тиреоидит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(54, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Афазия':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4
            print(55, kasallik_sabablari5)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аэроотит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(56, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Базалиома':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(57, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Базедова болезнь':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(58, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Баланит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(59, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Белая горячка':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(60, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бери-бери':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(61, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бесплодие у женщин':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari6 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5
            print(62, kasallik_sabablari6)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бесплодие у мужчин':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(63, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бессонница':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(64, kasallik_sabablari)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Блефарит':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            print(65, kasallik_sabablari)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Близорукость':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_sabablari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_sabablari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_sabablari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_sabablari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_sabablari12 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6 + '\n' + kasallik_sabablari7 + '\n' + kasallik_sabablari8 + '\n' + kasallik_sabablari9 + '\n' + kasallik_sabablari10 + '\n' + kasallik_sabablari11
            print(66, kasallik_sabablari12)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Блокада ножки пучка Гиса':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari7 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6
            print(67, kasallik_sabablari7)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Аддисона':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(68, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Альцгеймера':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(69, kasallik_sabablari4)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Боуэна':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(70, kasallik_sabablari)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Виллебранда':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(80, kasallik_sabablari2)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Иценко-Кушинга':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(81, kasallik_sabablari)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Крона':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(82, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Паркинсона':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[6].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4
            print(83, kasallik_sabablari5)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Пейрони':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(84, kasallik_sabablari3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Пика':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(85, kasallik_sabablari4)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Симмондса':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4
            print(86, kasallik_sabablari5)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бородавки подошвенные':
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6:19].text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(87, kasallik_sabablari4)




    except:
        print('topilmadi-----------')
driver.close()
