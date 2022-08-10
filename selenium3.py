import sqlite3

from selenium import webdriver
from selenium.webdriver.common.by import By

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
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
    if i == 'https://illness.docdoc.ru/astigmatizm ' or i == 'https://illness.docdoc.ru/beshenstvo' or i == 'https://illness.docdoc.ru/bolezn_gjuntera' or i == 'https://illness.docdoc.ru/bolezn_uippla' or i == 'https://illness.docdoc.ru/borodavki' or i == 'https://illness.docdoc.ru/bolezn_hantingtona' or i == 'https://illness.docdoc.ru/bolezn_Shljattera' or i == 'https://illness.docdoc.ru/blokada_nozhki_puchka_Gisa' or i == 'https://illness.docdoc.ru/virus_pappilomi_cheloveka':
        continue
    # if i in list_links:
    #     continue
    try:
        if driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Абсцесс':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Авитаминоз':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аденовирус':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika3, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == "Аденома гипофиза":

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari3, diagnostika7, davolanish6))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == "Аденома простаты":
            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
            davolanish3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                    13].text
            davolanish4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[24].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                25].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                26].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(5.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari4, kasallik_asoratlari13, diagnostika4, davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == "Аденома щитовидной железы":

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari3, diagnostika, davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аденомиоз':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari2, diagnostika, davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аднексит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.CLASS_NAME,
                'illnes-short-description').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

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
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
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
                30].text
            davolanish7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[31].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                32].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                33].text
            davolanish10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[34].text
            davolanish11 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10
            print(8.3, davolanish11)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (
                    kasallik_nomi, kasallik_haqida2, kasallik_sabablari9, kasallik_asoratlari5, diagnostika5,
                    davolanish11))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Акромегалия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                5].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                    12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(9.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika, davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Алалия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            kasallik_sabablari6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_sabablari7 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6
            print(10, kasallik_sabablari7)

            kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[18].text
            kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            kasallik_asoratlari2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[14].text
            kasallik_asoratlari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            kasallik_asoratlari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[21].text
            kasallik_asoratlari5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[22].text
            kasallik_asoratlari6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[23].text
            kasallik_asoratlari7 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6
            print(10.1, kasallik_asoratlari7)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                31].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                      'ol').text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[32].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[16].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(10.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                33].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                34].text
            davolanish2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                    17].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                36].text
            davolanish4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[37].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                38].text
            davolanish6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                    18].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                39].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                40].text
            davolanish9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[19].text
            davolanish10 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7
            print(10.3, davolanish10)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari7, kasallik_asoratlari7, diagnostika4, davolanish10))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Алкоголизм':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[10].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[17].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(11.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                18].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                19].text
            davolanish3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[12].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                20].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                21].text
            davolanish6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[13].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(11.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari6, kasallik_asoratlari2, diagnostika3, davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аллергия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[16].text
            kasallik_asoratlari3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[17].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(12.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                17].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[18].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[18].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(12.2, diagnostika4)

            davolanish = kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[19].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                21].text
            davolanish3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[20].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                22].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                23].text
            davolanish6 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5
            print(12.3, davolanish6)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari7, kasallik_asoratlari5, diagnostika4, davolanish6))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аллергия инсектная':
            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[10].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(13.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                8].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                10].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(13.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari3, diagnostika2, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аллергия лекарственная':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print('4', kasallik_haqida3)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida3, kasallik_sabablari3, kasallik_asoratlari4, diagnostika5, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аллергия пищевая':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[11].text
            diagnostika2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            diagnostika3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[12].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(15.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                7].text
            davolanish1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                8].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                9].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(15.3, davolanish4)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika4, davolanish4))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Алопеция':
            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[11].text
            print(16.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish5 = davolanish + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4
            print(16.3, davolanish5)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari3, diagnostika, davolanish5))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Алопеция андрогенная':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    0].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida2, kasallik_sabablari4, kasallik_asoratlari3, diagnostika3, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Алопеция очаговая':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari3, diagnostika2, davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Альвеолит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[13].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(19.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(19.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari4, kasallik_asoratlari2, diagnostika3, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Альгоменорея':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
            print(20.1, kasallik_asoratlari2)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika3, davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Амблиопия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[11].text
            print(21.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(21.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari2, diagnostika, davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аменорея':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(22.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari5, kasallik_asoratlari, diagnostika, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Амилоидоз':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Амнезия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika2, davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анальная трещина':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[11].text
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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari3, diagnostika2, davolanish4))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Анальный зуд':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika3, davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анафилактический шок':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari4, diagnostika2, davolanish4))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Ангина':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(28.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari3, diagnostika, davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Ангиома':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
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
                By.TAG_NAME, 'ul')[15].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish8 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7
            print(29.3, davolanish8)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari9, diagnostika6, davolanish8))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анемия (низкий гемоглобин)':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[8].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[9].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[10].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            kasallik_asoratlari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            kasallik_asoratlari11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            kasallik_asoratlari13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            kasallik_asoratlari15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            kasallik_asoratlari16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            kasallik_asoratlari17 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            kasallik_asoratlari18 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            kasallik_asoratlari19 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            kasallik_asoratlari20 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            kasallik_asoratlari21 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            kasallik_asoratlari22 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            kasallik_asoratlari23 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            kasallik_asoratlari24 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            kasallik_asoratlari25 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[37].text
            kasallik_asoratlari26 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            kasallik_asoratlari27 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8 + '\n' + kasallik_asoratlari9 + '\n' + kasallik_asoratlari10 + '\n' + kasallik_asoratlari11 + '\n' + kasallik_asoratlari12 + '\n' + kasallik_asoratlari13 + '\n' + kasallik_asoratlari14 + '\n' + kasallik_asoratlari15 + '\n' + kasallik_asoratlari16 + '\n' + kasallik_asoratlari17 + '\n' + kasallik_asoratlari18 + '\n' + kasallik_asoratlari19 + '\n' + kasallik_asoratlari20 + '\n' + kasallik_asoratlari20 + '\n' + kasallik_asoratlari21 + '\n' + kasallik_asoratlari22 + '\n' + kasallik_asoratlari23 + '\n' + kasallik_asoratlari24 + '\n' + kasallik_asoratlari25 + '\n' + kasallik_asoratlari26
            print(30.1, kasallik_asoratlari27)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[39].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[29].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[40].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[41].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[42].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[43].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[30].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[44].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[45].text
            diagnostika9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[31].text
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
                By.TAG_NAME, 'ul')[33].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[55].text
            davolanish12 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11
            print(30.3, davolanish12)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari9, kasallik_asoratlari27, diagnostika10,
                 davolanish12))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Анемия железодефицитная':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(31, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(31.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(31.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(31.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika4,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аномалия Кимерли':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(32.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika8 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7
            print(32.2, diagnostika8)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(32.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari5, diagnostika8,
                 davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аноргазмия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(33, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(33.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            print(33.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(33.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Анорексия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[14].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
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

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari, diagnostika6,
                 davolanish6))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Апатия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(35.3, davolanish4)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari4, diagnostika,
                 davolanish4))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Апноэ':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)

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
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(36.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(36.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida3, kasallik_sabablari2, kasallik_asoratlari2, diagnostika4,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Аппендицит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text

            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(37, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(37.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
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
                By.TAG_NAME, 'ul')[15].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish5 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4
            print(37.3, davolanish5)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika8,
                 davolanish5))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Апраксия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            print(38, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(38.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(38.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(38.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari2, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аритмия дыхания':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[10].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(39.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(39.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(39.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari3, diagnostika3,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аритмия сердца':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(40.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(40.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(40.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артериальная гипертензия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'p').text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(41, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(41.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(41.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(41.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артериальная гипертония':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'ul')[20].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[21].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(42.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[22].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[23].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[24].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[25].text
            diagnostika9 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8
            print(42.2, diagnostika9)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[26].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[27].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[28].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[29].text
            davolanish10 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9
            print(42.3, davolanish10)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari4, kasallik_asoratlari4, diagnostika9,
                 davolanish10))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артериальная гипотензия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            kasallik_sabablari11 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6 + '\n' + kasallik_sabablari7 + '\n' + kasallik_sabablari8 + '\n' + kasallik_sabablari9 + '\n' + kasallik_sabablari10
            print(43, kasallik_sabablari11)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            kasallik_asoratlari7 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6
            print(43.1, kasallik_asoratlari7)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(43.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(43.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari11, kasallik_asoratlari7, diagnostika4,
                 davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Артрит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(44, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(44.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(44.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(44.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika2,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Астения (астенический синдром)':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(45, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ol').text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(45.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            diagnostika6 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5
            print(45.2, diagnostika6)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[37].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[38].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[39].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[40].text
            davolanish15 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14
            print(45.3, davolanish15)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari4, diagnostika6,
                 davolanish15))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Астенопия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            print(46, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            print(46.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            print(46.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            print(46.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Астигматизм':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(47, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(47.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika5 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4
            print(47.2, diagnostika5)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[22].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish16 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14 + '\n' + davolanish15
            print(47.3, davolanish16)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari4, diagnostika5,
                 davolanish16))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)







        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Асцит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(48.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[9].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(48.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(48.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari5, kasallik_asoratlari2, diagnostika4,
                 davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атаксия':
            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            kasallik_asoratlari8 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7
            print(49.1, kasallik_asoratlari8)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(49.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish6 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5
            print(49.3, davolanish6)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari4, kasallik_asoratlari8, diagnostika3,
                 davolanish6))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атерома':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(50, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(50.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            print(50.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(50.3, davolanish4)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari4, diagnostika,
                 davolanish4))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атеросклероз':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[0].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(51, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(51.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(51.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(51.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Атония мочевого пузыря':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(52, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(52.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(52.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(52.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika3,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аутизм':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(53, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            kasallik_asoratlari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            kasallik_asoratlari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            kasallik_asoratlari11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            kasallik_asoratlari12 = kasallik_sabablari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + "\n" + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8 + '\n' + kasallik_asoratlari9 + '\n' + kasallik_asoratlari10 + '\n' + kasallik_asoratlari11

            print(53.1, kasallik_asoratlari12)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[21].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(53.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[22].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(53.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari12, diagnostika3,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аутоиммунный тиреоидит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(54, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(54.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika4 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3
            print(54.2, diagnostika4)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish13 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + "\n" + davolanish8 + '\n' + davolanish9 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12
            print(54.3, davolanish13)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari5, diagnostika4,
                 davolanish13))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Афазия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(55.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(55.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(55.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari5, kasallik_asoratlari2, diagnostika3,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Аэроотит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(56, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            print(56.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            print(56.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            print(56.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari, diagnostika,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Базалиома':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(57, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(57.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            diagnostika7 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6
            print(57.2, diagnostika7)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(57.3, davolanish6)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari4, diagnostika7,
                 davolanish6))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Базедова болезнь':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(58, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(58.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(58.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(58.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika3,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Баланит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(59, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_asoratlari3
            print(59.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(59.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            davolanish2 = diagnostika + '\n' + diagnostika1
            print(59.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari4, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Белая горячка':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(60, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(60.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            print(60.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(60.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari4, diagnostika,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бери-бери':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    0].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    2].text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    3].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                    0].text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    4].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                    1].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    5].text
            kasallik_haqida8 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7
            print(kasallik_haqida8)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(61, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(61.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(61.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            print(61.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida8, kasallik_sabablari2, kasallik_asoratlari2, diagnostika3,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бесплодие у женщин':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            print(62.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika7 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6
            print(62.2, diagnostika7)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[37].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[38].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            davolanish16 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14
            print(62.3, davolanish16)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari6, kasallik_asoratlari, diagnostika7,
                 davolanish16))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бесплодие у мужчин':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(63, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            print(63.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            diagnostika11 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8 + '\n' + diagnostika9 + '\n' + diagnostika10
            print(63.2, diagnostika11)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish18 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14 + '\n' + davolanish15 + '\n' + davolanish16
            print(63.3, davolanish18)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari, diagnostika11,
                 davolanish18))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бессонница':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(64, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            print(64.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(64.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(64.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Блефарит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            print(65, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            print(65.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            print(65.2, diagnostika)

            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish3 = davolanish1 + '\n' + davolanish2
            print(65.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Близорукость':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(66.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(66.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(66.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari12, kasallik_asoratlari3, diagnostika2,
                 davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        # elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
        #                                                                       'h1').text == 'Блокада ножки пучка Гиса':
        #     kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
        #         By.TAG_NAME, 'p')[5].text
        #     kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
        #         By.TAG_NAME, 'ul').text
        #     kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
        #         By.TAG_NAME, 'p')[6].text
        #     kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
        #         By.TAG_NAME, 'p')[7].text
        #     kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
        #         By.TAG_NAME, 'ul')[1].text
        #     kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
        #         By.TAG_NAME, 'p')[8].text
        #     kasallik_sabablari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
        #         By.TAG_NAME, 'ul')[2].text
        #     kasallik_sabablari7 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6
        #     print(67, kasallik_sabablari7)
        #
        #     diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
        #         By.TAG_NAME, 'ul')[2].text

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Аддисона':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(68, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari9 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8
            print(68.1, kasallik_asoratlari9)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            diagnostika9 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8
            print(68.2, diagnostika9)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[37].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(68.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari9, diagnostika9,
                 davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Альцгеймера':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[10].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(69.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            diagnostika6 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5
            print(69.2, diagnostika6)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(69.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari4, kasallik_asoratlari4, diagnostika6,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Боуэна':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(70, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            print(70.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(70.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            print(70.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika2,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Виллебранда':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(71, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(71.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(71.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(71.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika3,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Иценко-Кушинга':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'p').text
            print(kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(72, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            print(72.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            print(72.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            print(72.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Крона':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(73, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(73.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(73.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(73.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika2,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Паркинсона':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida5 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4
            print(kasallik_haqida5)

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
            print(74, kasallik_sabablari5)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            kasallik_asoratlari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            kasallik_asoratlari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            kasallik_asoratlari11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            kasallik_asoratlari12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            kasallik_asoratlari13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            kasallik_asoratlari14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            kasallik_asoratlari15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            kasallik_asoratlari16 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8 + '\n' + kasallik_asoratlari9 + '\n' + kasallik_asoratlari10 + '\n' + kasallik_asoratlari11 + '\n' + kasallik_asoratlari12 + '\n' + kasallik_asoratlari13 + '\n' + kasallik_asoratlari14 + '\n' + kasallik_asoratlari15
            print(74.1, kasallik_asoratlari16)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[21].text
            diagnostika9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            diagnostika10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[22].text
            diagnostika11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[37].text
            diagnostika12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[38].text
            diagnostika13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[23].text
            diagnostika14 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8 + '\n' + diagnostika9 + '\n' + '\n' + diagnostika10 + '\n' + diagnostika11 + '\n' + diagnostika12 + '\n' + diagnostika13
            print(74.2, diagnostika14)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[39].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[24].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[40].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[41].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[42].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[43].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[44].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[45].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[24].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[46].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[47].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[25].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[48].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[49].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[26].text
            davolanish15 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14
            print(74.3, davolanish15)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida5, kasallik_sabablari5, kasallik_asoratlari16, diagnostika14,
                 davolanish15))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Пейрони':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(75, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(75.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(75.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(75.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari3, diagnostika3,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)





        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Пика':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(76, kasallik_sabablari4)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(76.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(76.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(76.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari4, kasallik_asoratlari3, diagnostika3,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)






        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Болезнь Симмондса':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

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
            print(77, kasallik_sabablari5)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari7 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6
            print(77.1, kasallik_asoratlari7)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(77.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            print(77.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari5, kasallik_asoratlari7, diagnostika2,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бородавки подошвенные':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_sabablari4 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3
            print(78, kasallik_sabablari4)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(78.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[10].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(78.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'h3').text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish17 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish18 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish19 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish20 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'h3')[1].text
            davolanish21 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish22 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish23 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish24 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish25 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish26 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish27 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish28 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish29 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            davolanish30 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14 + '\n' + davolanish15 + '\n' + davolanish16 + '\n' + davolanish17 + '\n' + davolanish18 + '\n' + davolanish19 + '\n' + davolanish20 + '\n' + davolanish21 + '\n' + davolanish22 + '\n' + davolanish23 + '\n' + davolanish24 + '\n' + davolanish25 + '\n' + davolanish26 + '\n' + davolanish27 + '\n' + davolanish28
            print(78.3, davolanish30)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari4, kasallik_asoratlari2, diagnostika2,
                 davolanish30))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Брадикардия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_asoratlari4
            print(79, kasallik_sabablari5)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(79.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'strong').text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'strong')[1].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            diagnostika9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            diagnostika10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            diagnostika12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'strong')[2].text
            diagnostika14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            diagnostika15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            diagnostika16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            diagnostika17 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            diagnostika18 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8 + '\n' + diagnostika9 + '\n' + '\n' + diagnostika10 + '\n' + diagnostika11 + '\n' + diagnostika12 + '\n' + diagnostika13 + '\n' + diagnostika14 + '\n' + diagnostika15 + '\n' + diagnostika16 + '\n' + diagnostika17
            print(79.2, diagnostika18)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'h3')[1].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish17 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish18 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14 + '\n' + davolanish15 + '\n' + davolanish16 + '\n' + davolanish17
            print(79.3, davolanish18)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari5, kasallik_asoratlari3, diagnostika18,
                 davolanish18))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бронхиальная астма':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(80, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(80.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(80.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(80.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бронхиолит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(81, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari4 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3
            print(81.1, kasallik_asoratlari4)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(81.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(81.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari4, diagnostika3,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бронхит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_sabablari6 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5
            print(82, kasallik_sabablari6)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[4].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(82.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                7].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[14].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(82.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(82.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari6, kasallik_asoratlari2, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бронхит обструктивный':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari6 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5
            print(83, kasallik_sabablari6)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_asoratlari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_asoratlari10 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8 + '\n' + kasallik_asoratlari9
            print(83.1, kasallik_asoratlari10)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[21].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[22].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            diagnostika9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            diagnostika10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            diagnostika11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            diagnostika12 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8 + '\n' + diagnostika9 + '\n' + '\n' + diagnostika10 + '\n' + diagnostika11
            print(83.2, diagnostika12)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[23].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[24].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[25].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[26].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[27].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[28].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[29].text
            davolanish16 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14 + '\n' + davolanish15
            print(83.3, davolanish16)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari6, kasallik_asoratlari10, diagnostika12,
                 davolanish16))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Булимия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(84, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(84.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            print(84.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(84.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Бурсит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[0].text
            print(85, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            print(85.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            print(85.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(85.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Булимия':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(86, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(86.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            print(86.2, diagnostika)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            print(86.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Вагинит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'p').text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(87, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(87.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(87.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(87.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Вальгусная деформация стопы у детей':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4
            print(88, kasallik_sabablari5)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(88.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(88.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            davolanish5 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4
            print(88.3, davolanish5)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari5, kasallik_asoratlari, diagnostika2,
                 davolanish5))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Варикозное расширение вен':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(89, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(89.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(89.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(89.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari3, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Варикоцеле':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari5 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4
            print(90, kasallik_sabablari5)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(90.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            diagnostika7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            diagnostika8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            diagnostika9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            diagnostika10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            diagnostika11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            diagnostika13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            diagnostika14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            diagnostika15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            diagnostika16 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6 + '\n' + diagnostika7 + '\n' + diagnostika8 + '\n' + diagnostika9 + '\n' + '\n' + diagnostika10 + '\n' + diagnostika11 + '\n' + diagnostika12 + '\n' + diagnostika13 + '\n' + diagnostika14 + '\n' + diagnostika15
            print(90.2, diagnostika16)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[30].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[31].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[32].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[18].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[33].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[34].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[35].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[36].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[37].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[38].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[39].text
            davolanish16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[40].text
            davolanish17 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[41].text
            davolanish18 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[19].text
            davolanish19 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[42].text
            davolanish20 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[20].text
            davolanish21 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[43].text
            davolanish22 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[44].text
            davolanish23 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[45].text
            davolanish24 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[46].text
            davolanish25 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[21].text
            davolanish26 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[47].text
            davolanish27 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[48].text
            davolanish28 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[22].text
            davolanish29 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14 + '\n' + davolanish15 + '\n' + davolanish16 + '\n' + davolanish17 + '\n' + davolanish18 + '\n' + davolanish19 + '\n' + davolanish20 + '\n' + davolanish21 + '\n' + davolanish22 + '\n' + davolanish23 + '\n' + davolanish24 + '\n' + davolanish25 + '\n' + davolanish26 + '\n' + davolanish27 + '\n' + davolanish28
            print(90.3, davolanish29)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari5, kasallik_asoratlari5, diagnostika16,
                 davolanish29))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Васкулит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[23].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(91, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[24].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(91.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[25].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(91.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[26].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[48].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(91.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Васкулит геморрагический':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(91, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(91.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[5].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(91.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[6].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(91.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika3,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == 'Вегетоневроз':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(92, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[10].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_asoratlari10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            kasallik_asoratlari11 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5 + '\n' + kasallik_asoratlari6 + '\n' + kasallik_asoratlari7 + '\n' + kasallik_asoratlari8 + '\n' + kasallik_asoratlari9 + '\n' + kasallik_asoratlari10
            print(92.1, kasallik_asoratlari11)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(92.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            davolanish7 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6
            print(92.3, davolanish7)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari11, diagnostika2,
                 davolanish7))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Вегетососудистая дистония (ВСД)':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[3].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(93, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_asoratlari3 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2
            print(93.1, kasallik_asoratlari3)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            diagnostika3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[15].text
            diagnostika4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            diagnostika5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[16].text
            diagnostika6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            diagnostika7 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2 + '\n' + diagnostika3 + '\n' + diagnostika4 + '\n' + diagnostika5 + '\n' + diagnostika6
            print(93.2, diagnostika7)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[14].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            davolanish4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            davolanish5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            davolanish6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            davolanish7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[20].text
            davolanish8 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            davolanish9 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            davolanish10 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish11 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish12 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[25].text
            davolanish13 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[26].text
            davolanish14 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[27].text
            davolanish15 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[28].text
            davolanish16 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[29].text
            davolanish17 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[17].text
            davolanish18 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3 + '\n' + davolanish4 + '\n' + davolanish5 + '\n' + davolanish6 + '\n' + davolanish7 + '\n' + davolanish8 + '\n' + davolanish9 + '\n' + davolanish10 + '\n' + davolanish11 + '\n' + davolanish12 + '\n' + davolanish13 + '\n' + davolanish14 + '\n' + davolanish15 + '\n' + davolanish16 + '\n' + davolanish17
            print(93.3, davolanish18)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari3, diagnostika7,
                 davolanish18))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Везикулит':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(94, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(94.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(94.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(94.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari2, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Венозная недостаточность':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari3 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2
            print(95, kasallik_sabablari3)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_asoratlari5 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4
            print(95.1, kasallik_asoratlari5)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(95.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[14].text
            davolanish4 = davolanish + '\n' + davolanish1 + '\n' + davolanish2 + '\n' + davolanish3
            print(95.3, davolanish4)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari3, kasallik_asoratlari5, diagnostika2,
                 davolanish4))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Вертебро-базилярная недостаточность (ВБН)':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(96, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            print(96.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(96.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            print(96.3, davolanish)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari, diagnostika2,
                 davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Ветрянка (ветряная оспа)':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[8].text
            kasallik_sabablari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            kasallik_sabablari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            kasallik_sabablari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[10].text
            kasallik_sabablari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[11].text
            kasallik_sabablari6 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[12].text
            kasallik_sabablari7 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[13].text
            kasallik_sabablari8 = kasallik_sabablari + '\n' + kasallik_sabablari1 + '\n' + kasallik_sabablari2 + '\n' + kasallik_sabablari3 + '\n' + kasallik_sabablari4 + '\n' + kasallik_sabablari5 + '\n' + kasallik_sabablari6 + '\n' + kasallik_sabablari7
            print(97, kasallik_sabablari8)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[15].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            kasallik_asoratlari2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[16].text
            kasallik_asoratlari3 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[17].text
            kasallik_asoratlari4 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[18].text
            kasallik_asoratlari5 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[19].text
            kasallik_asoratlari6 = kasallik_asoratlari + '\n' + kasallik_asoratlari1 + '\n' + kasallik_asoratlari2 + '\n' + kasallik_asoratlari3 + '\n' + kasallik_asoratlari4 + '\n' + kasallik_asoratlari5
            print(97.1, kasallik_asoratlari6)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[21].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[22].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(97.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[23].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[24].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish2
            print(97.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari8, kasallik_asoratlari6, diagnostika2,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Вирильный синдром':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(98, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[2].text
            print(98.1, kasallik_asoratlari)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(98.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[13].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[9].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(98.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Вирус Эпштейна-Барра':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            print(99, kasallik_sabablari)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[3].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(99.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(99.2, diagnostika2)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = davolanish + '\n' + davolanish1
            print(99.3, davolanish2)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari, kasallik_asoratlari2, diagnostika2,
                 davolanish2))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == 'Витилиго':

            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
            print('--------', kasallik_nomi)

            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print('--------', kasallik_haqida)

            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[1].text
            kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'ul').text
            kasallik_sabablari2 = kasallik_sabablari + '\n' + kasallik_sabablari1
            print(100, kasallik_sabablari2)

            kasallik_asoratlari = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[2].text
            kasallik_asoratlari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[1].text
            kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
            print(100.1, kasallik_asoratlari2)

            diagnostika = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[4].text
            diagnostika1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[11].text
            diagnostika2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[5].text
            diagnostika3 = diagnostika + '\n' + diagnostika1 + '\n' + diagnostika2
            print(100.2, diagnostika3)

            davolanish = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[6].text
            davolanish1 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'ul')[12].text
            davolanish2 = driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                By.TAG_NAME, 'p')[7].text
            davolanish3 = davolanish + '\n' + davolanish1 + '\n' + davolanish
            print(100.3, davolanish3)

            cursor.execute(
                "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, kasallik_haqida, kasallik_sabablari2, kasallik_asoratlari2, diagnostika2,
                 davolanish3))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)
            break


    except:
        print('topilmadi-----------')
        # continue
driver.close()
