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

# continue
# print(list_links)


for i in list_links:
    driver.get(f"{i}")
    if i == "https://illness.docdoc.ru/pnevmonia_atipichnaya" or i == 'https://illness.docdoc.ru/mialgija' or i == 'https://illness.docdoc.ru/narkomania' or i == 'https://illness.docdoc.ru/nevrit' or i == 'https://illness.docdoc.ru/ozhirenie' or i == 'https://illness.docdoc.ru/otomikoz' or i == 'https://illness.docdoc.ru/paranoiya' or i == 'https://illness.docdoc.ru/rozatsea' or i == 'https://illness.docdoc.ru/rozha' or i == 'https://illness.docdoc.ru/perikardit' or i == 'https://illness.docdoc.ru/periodontit' or i == 'https://illness.docdoc.ru/sarkoidoz' or i == 'https://illness.docdoc.ru/takhikardiya' or i == 'https://illness.docdoc.ru/holera' or i == 'https://illness.docdoc.ru/kista_meniska' or i == 'https://illness.docdoc.ru/ekhinokokkoz' or i == 'https://illness.docdoc.ru/iazvennyi_kolit' or i == 'https://illness.docdoc.ru/yachmen' or i == 'https://illness.docdoc.ru/jashhur' or i == 'https://illness.docdoc.ru/Gigroma' or i == 'https://illness.docdoc.ru/girsutizm' or i == 'https://illness.docdoc.ru/depression' or i == 'https://illness.docdoc.ru/cinga' or i == 'https://illness.docdoc.ru/giperplazija_jendometrija' or i == 'https://illness.docdoc.ru/vrosshij_nogot':
        continue
        # kasallik_nomlari
    kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
    cursor.execute("INSERT INTO basic_app_ (kasallik_nomi) VALUES (?)", (kasallik_nomi,))
    connect.commit()
    print(kasallik_nomi)
    a = cursor.execute('SELECT * FROM basic_app_kasallik_nomi')
    print(a)
    # break

    # break

    # break
    # except:
    #     print('not -------')

    try:

        kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
        print('--------', kasallik_haqida)
        cursor.execute("INSERT INTO basic_app_kasallik_haqida (kasallik_haqida) VALUES (?)", (kasallik_haqida,))
        connect.commit()
        print(kasallik_nomi)
        a = cursor.execute('SELECT * FROM basic_app_kasallik_haqida')
        print(a)


    except:
        if driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                            'h1').text == '???????????????? ??????????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print('4', kasallik_haqida3)

        if driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                            'h1').text == '?????????????? ????????????-??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME, 'p').text
            print(kasallik_haqida, )

        if driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.CLASS_NAME,
                'illnes-short-description').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????? ????????????':
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    0].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    1].text
            kasallik_haqida3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                By.TAG_NAME,
                'ul').text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    2].text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    3].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    5].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    6].text
            kasallik_haqida8 = kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7
            print(kasallik_haqida8)

        elif (driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                               'h1').text) == '??????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    2].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    3].text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)

        elif (driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                               'h1').text) == '???????????????? ??????????????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    0].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                    1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '????????-????????':

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

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '???????????????? ??????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????????? ????????????????????':
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

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '????????????????-???????????????????? ?????????????????????????????? (??????)':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????????????? ??????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)
        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '???????????? (????????????????????)':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida4 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3
            print(kasallik_haqida4)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '???????????? ????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida5 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_haqida9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_haqida11 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8 + '\n' + kasallik_haqida9 + '\n' + kasallik_haqida10
            print(kasallik_haqida11)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida3)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '???????????????? ??????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????? ???????????????? ????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida4 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3
            print(kasallik_haqida4)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida5 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4
            print(kasallik_haqida5)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '???????????????????????? ?????????????? (?????????????????????? ????????????????????)':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_haqida4 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_haqida11 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_haqida12 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_haqida13 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_haqida14 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8 + '\n' + kasallik_haqida9 + '\n' + kasallik_haqida10 + '\n' + kasallik_haqida11 + '\n' + kasallik_haqida12 + '\n' + kasallik_haqida13
            print(kasallik_haqida14)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida5 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4
            print(kasallik_haqida5)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '??????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '????????????????????':
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
            kasallik_haqida5 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_haqida10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida11 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_haqida12 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_haqida13 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_haqida14 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            kasallik_haqida15 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[11].text
            kasallik_haqida16 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[12].text
            kasallik_haqida17 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[13].text
            kasallik_haqida18 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[14].text
            kasallik_haqida19 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[15].text
            kasallik_haqida20 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[16].text
            kasallik_haqida21 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[17].text
            kasallik_haqida22 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[18].text
            kasallik_haqida23 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            kasallik_haqida24 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            kasallik_haqida25 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[21].text
            kasallik_haqida26 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[22].text
            kasallik_haqida27 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[23].text
            kasallik_haqida28 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[24].text
            kasallik_haqida29 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            kasallik_haqida30 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8 + '\n' + kasallik_haqida9 + '\n' + kasallik_haqida10 + '\n' + kasallik_haqida11 + '\n' + kasallik_haqida12 + '\n' + kasallik_haqida13 + '\n' + kasallik_haqida14 + '\n' + kasallik_haqida15 + '\n' + kasallik_haqida16 + '\n' + kasallik_haqida17 + '\n' + kasallik_haqida18 + '\n' + kasallik_haqida19 + '\n' + kasallik_haqida20 + '\n' + kasallik_haqida21 + '\n' + kasallik_haqida22 + '\n' + kasallik_haqida23 + '\n' + kasallik_haqida24 + '\n' + kasallik_haqida25 + '\n' + kasallik_haqida26 + '\n' + kasallik_haqida27 + '\n' + kasallik_haqida28 + '\n' + kasallik_haqida29
            print(kasallik_haqida30)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            print(kasallik_haqida)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????????????':
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
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida7 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_haqida10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_haqida11 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida12 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_haqida13 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_haqida14 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[11].text
            kasallik_haqida15 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            kasallik_haqida16 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[12].text
            kasallik_haqida17 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[13].text
            kasallik_haqida18 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            kasallik_haqida19 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[14].text
            kasallik_haqida20 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[5].text
            kasallik_haqida21 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[15].text
            kasallik_haqida22 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[6].text
            kasallik_haqida23 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[16].text
            kasallik_haqida24 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8 + '\n' + kasallik_haqida9 + '\n' + kasallik_haqida10 + '\n' + kasallik_haqida11 + '\n' + kasallik_haqida12 + '\n' + kasallik_haqida13 + '\n' + kasallik_haqida14 + '\n' + kasallik_haqida15 + '\n' + kasallik_haqida16 + '\n' + kasallik_haqida17 + '\n' + kasallik_haqida18 + '\n' + kasallik_haqida19 + '\n' + kasallik_haqida20 + '\n' + kasallik_haqida21 + '\n' + kasallik_haqida22 + '\n' + kasallik_haqida23
            print(kasallik_haqida24)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida5 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4
            print(kasallik_haqida5)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida7 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6
            print(kasallik_haqida7)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????????? ???????????????? ???????????????? ?? ??????????????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '???????????????????? ??????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_haqida9 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8
            print(kasallik_haqida9)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            kasallik_haqida10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida11 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida12 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_haqida13 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_haqida14 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            kasallik_haqida15 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_haqida16 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8 + '\n' + kasallik_haqida9 + '\n' + kasallik_haqida10 + '\n' + kasallik_haqida11 + '\n' + kasallik_haqida12 + '\n' + kasallik_haqida13 + '\n' + kasallik_haqida14 + '\n' + kasallik_haqida15
            print(kasallik_haqida16)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '???????????????????? (????????????????)':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida3 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida4 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3
            print(kasallik_haqida4)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida5 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4
            print(kasallik_haqida5)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????????':
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
            kasallik_haqida5 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida9 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_haqida10 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida11 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[8].text
            kasallik_haqida12 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[9].text
            kasallik_haqida13 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[10].text
            kasallik_haqida14 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[3].text
            kasallik_haqida15 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[11].text
            kasallik_haqida16 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[12].text
            kasallik_haqida17 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[13].text
            kasallik_haqida18 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[14].text
            kasallik_haqida19 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[15].text
            kasallik_haqida20 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[16].text
            kasallik_haqida21 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[17].text
            kasallik_haqida22 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[18].text
            kasallik_haqida23 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[19].text
            kasallik_haqida24 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[20].text
            kasallik_haqida25 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[21].text
            kasallik_haqida26 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[22].text
            kasallik_haqida27 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[23].text
            kasallik_haqida28 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[24].text
            kasallik_haqida29 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[4].text
            kasallik_haqida30 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8 + '\n' + kasallik_haqida9 + '\n' + kasallik_haqida10 + '\n' + kasallik_haqida11 + '\n' + kasallik_haqida12 + '\n' + kasallik_haqida13 + '\n' + kasallik_haqida14 + '\n' + kasallik_haqida15 + '\n' + kasallik_haqida16 + '\n' + kasallik_haqida17 + '\n' + kasallik_haqida18 + '\n' + kasallik_haqida19 + '\n' + kasallik_haqida20 + '\n' + kasallik_haqida21 + '\n' + kasallik_haqida22 + '\n' + kasallik_haqida23 + '\n' + kasallik_haqida24 + '\n' + kasallik_haqida25 + '\n' + kasallik_haqida26 + '\n' + kasallik_haqida27 + '\n' + kasallik_haqida28 + '\n' + kasallik_haqida29
            print(kasallik_haqida30)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida2 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[3].text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida7 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6
            print(kasallik_haqida7)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????????????':
            kasallik_haqida = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            kasallik_haqida4 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[5].text
            kasallik_haqida5 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[6].text
            kasallik_haqida6 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
            kasallik_haqida7 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[7].text
            kasallik_haqida8 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            kasallik_haqida9 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3 + '\n' + kasallik_haqida4 + '\n' + kasallik_haqida5 + '\n' + kasallik_haqida6 + '\n' + kasallik_haqida7 + '\n' + kasallik_haqida8
            print(kasallik_haqida9)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????? ??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '???????? ??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '???????????????? ??????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
            kasallik_haqida4 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2 + '\n' + kasallik_haqida3
            print(kasallik_haqida4)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????????????????????? ?????????????? ????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)


        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                          'ul').text
            kasallik_haqida3 = kasallik_haqida + '\n' + kasallik_haqida1 + '\n' + kasallik_haqida2
            print(kasallik_haqida3)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)




        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text == '??????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            print(kasallik_haqida)



        elif driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                              'h1').text == '?????????????????????? ????????????????????':
            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         'p').text
            kasallik_haqida1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
            kasallik_haqida2 = kasallik_haqida + '\n' + kasallik_haqida1
            print(kasallik_haqida2)

# except:
#     print("topilmadi")

driver.close()

# row = cur.execute('SELECT * FROM basic_app_kasallik_nomi ').fetchall()
# print(row, 'database')
