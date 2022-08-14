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

for i in list_links:
    driver.get(f'{i}')
    if i == 'https://illness.docdoc.ru/alopetsiia' or i == 'https://illness.docdoc.ru/panicheskaja_ataka' or i == 'https://illness.docdoc.ru/pnevmonia_atipichnaya' or i == 'https://illness.docdoc.ru/toksidermija' or i == 'https://illness.docdoc.ru/feochromotsitoma' or i == 'https://illness.docdoc.ru/iazvennyi_kolit' or i == 'https://illness.docdoc.ru/tseliakiia' or i == 'https://illness.docdoc.ru/pnevmonia_atipichnaya' or i == 'https://illness.docdoc.ru/psihoz' or i == 'https://illness.docdoc.ru/poslerodovaya_depressiya' or i == 'https://illness.docdoc.ru/poliomielit' or i == 'https://illness.docdoc.ru/nejrosifilis' or i == 'https://illness.docdoc.ru/nevinashivanie_beremennosti' or i == 'https://illness.docdoc.ru/meteorizm' or i == 'https://illness.docdoc.ru/kartavost' or i == 'https://illness.docdoc.ru/jododeficit' or i == 'https://illness.docdoc.ru/displazija_shejki_matki' or i == 'https://illness.docdoc.ru/giperkaltsiemiya' or i == 'https://illness.docdoc.ru/allergicheslii_dermatit' or i == 'https://illness.docdoc.ru/kontaktnyi_dermatit' or i == 'https://illness.docdoc.ru/atroficheskij_gastrit' or i == 'https://illness.docdoc.ru/difteriya' or i == 'https://illness.docdoc.ru/gipokaltsiemiya' or i == 'https://illness.docdoc.ru/Gigroma' or i == 'https://illness.docdoc.ru/vykidysh' or i == 'https://illness.docdoc.ru/evstahiit' or i == 'https://illness.docdoc.ru/artrit' or i == 'https://illness.docdoc.ru/gepatit_e' or i == 'https://illness.docdoc.ru/ateroskleroz':
        continue

    hammasi = driver.find_element(By.XPATH,
                                  '/html/body/section[1]/section/div[1]/div[1]/div[3]/div[3]/div/div[2]/div[3]/div').text
    data0 = hammasi.split(' ')
    data0[3] = '$'
    data = list(data0)
    data1 = data.index('совет') + 1
    data[data1] = '$$'
    #
    data2 = data0[4:data1]
    data4 = ' '.join(map(str, data2))
    data5 = data4.split('\n')
    title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
    title_litle = title.casefold()
    title1 = title.split(' ')
    title2 = len(title1)
    for i in data5:
        if i == "Причины":
            try:
                kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                                                 'h1').text
                print('1--------', kasallik_nomi)
                # cursor.execute("INSERT INTO basic_app_болезни1 (title) VALUES (?)", (kasallik_nomi,))
                # connect.commit()
                # a = cursor.execute('SELECT * FROM basic_app_kasallik_haqida')
                # print(a)

                # print(data5)
                index = data5.index('Причины')
                data6 = data5[1:index]
                k_haqida = ' '.join(map(str, data6))
                print('2------', k_haqida)

                try:

                    data_str = ' '.join(map(str, data5))
                    dataX = data_str.split(' ')
                    index3 = dataX.index('Симптомы')
                    index33 = dataX.index('Причины') + 1
                    data8 = dataX[index33:index3]
                    data_str1 = ' '.join(map(str, data8))
                    k_sabablari = data_str1
                    print('3------', k_sabablari)
                except:
                    try:
                        data_p = dataX.index('Причины')
                        data_r = dataX.index('Симптомы')
                        data_alls = dataX[data_r] + title_litle
                        data_m = dataX.index(data_alls)
                        data_k = ' '.join(map(str, data_m))
                        k_sabablari = data_k
                        print('3.1------', k_sabablari)
                    except:
                        data_p = dataX.index('Причины')
                        data_r = dataX.index('Симптомы')
                        if data_r > data_p:
                            data_lv = dataX.index('Лучшие')
                            data_m1 = dataX[data_p:data_lv]
                            data_m2 = ' '.join(map(str, data_m1))
                            k_sabablari = data_m2
                            print('3.2-----', k_sabablari)


                title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
                title1 = title.split(' ')
                title2 = len(title1)
                all_data = driver.find_element(By.XPATH, '//*[@id="diseases_article_static_content"]').text
                all_data1 = all_data.split('\n')
                all_data2 = ' '.join(map(str, all_data1))
                all_data3 = all_data2.split(' ')

                try:
                    index_data = all_data3.index('Симптомы') + title2 + 1
                    index_data_end = all_data3.index('последствиями.') - 17
                    data_get = all_data3[index_data:index_data_end]
                    k_asoratlari = ' '.join(map(str, data_get))
                    print('4.1-------', k_asoratlari)




                except:
                    try:
                        index_data = all_data3.index('Признаки') + title2 + 1
                        index_data_end = all_data3.index('последствиями.') - 17
                        data_get = all_data3[index_data:index_data_end]
                        k_asoratlari = ' '.join(map(str, data_get))
                        print('4.2---------', k_asoratlari)



                    except:
                        index44 = dataX.index('обнаружили')
                        title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                                                 'h1').text
                        title1 = title.split(' ')
                        title2 = len(title1)
                        index55 = index3 + title2 + 1
                        index45 = index44 - 2
                        data_k_asoratlari = dataX[index55:index45]
                        data_k_asoratlari_str = ' '.join(map(str, data_k_asoratlari))
                        k_asoratlari = data_k_asoratlari_str
                        print('4------', k_asoratlari)

                try:
                    index66 = dataX.index('Диагностика')
                    index67 = index66 + 1
                    index77 = dataX.index('Лечение')
                    data_k_diagnostika = dataX[index67:index77]
                    data_k_diagnostika_str = ' '.join(map(str, data_k_diagnostika))
                    k_diagnostika = data_k_diagnostika_str
                    print('5------', k_diagnostika)
                except:
                    try:
                        if (dataX.index('последствиями.') + 1) == 'Диагностика':
                            data_lu = dataX.index('Лучшие')
                            data_ke = dataX.index('последствиями.')
                            data_m3 = dataX[data_ke + 2:data_lu]
                            data_m4 = ' '.join(map(str, data_m3))
                            k_diagnostika = data_m4
                            print('5.1------', k_diagnostika)
                    except:
                        print('ishlamadi')

                try:

                    indexA = dataX.index('Нужен')
                    index_lecheniye = dataX.index('Лечение')
                    if index_lecheniye > dataX.index('Диагностика'):
                        index_lecheniye_text = index_lecheniye + title2 + 1
                        index_text = dataX[index_lecheniye_text:indexA]
                        k_davolanish = ' '.join(map(str, index_text))
                        print('6-----------', k_davolanish, '\n')

                except:
                    try:
                        data_o = all_data3.index('Опасность')
                        data_l = all_data3.index('Лечение') + title2

                        data_ll = all_data3[data_o:data_l]

                        k_davolanish = ' '.join(map(str, data_ll))
                        print('6.1-------', k_davolanish)
                    except:
                        data_d = all_data3.index('Диета')
                        all_datas = all_data3[data_l:data_d]
                        k_davolanish = ' '.join(map(str, all_datas))
                        print(k_davolanish)
                cursor.execute(
                    "INSERT INTO basic_app_болезни (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                    (kasallik_nomi, k_haqida, k_sabablari, k_asoratlari, k_diagnostika, k_davolanish))
                connect.commit()
                a = cursor.execute('SELECT * FROM basic_app_болезни1')
                print(a)

            except:
                continue

driver.close()
