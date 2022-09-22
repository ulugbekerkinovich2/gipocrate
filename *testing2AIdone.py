from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# print('starting connect to database>>...')
# connect = psycopg2.connect(
#     dbname="gippokrat", user="postgres", password="root123", host="165.232.186.199",
#     port="5432")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")

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
# print('starting connect to database>>...')
# connect = psycopg2.connect(
#     dbname="gippokrat", user="postgres", password="root123", host="165.232.186.199",
#     port="5432")
# connect.autocommit = True
# cursor = connect.cursor()

for i in list_links:
    driver.get(f'{i}')
    if i == 'https://illness.docdoc.ru/alopetsiia' or i=='https://illness.docdoc.ru/epididimit' or i=='https://illness.docdoc.ru/jenterit_hronicheskij' or i=='https://illness.docdoc.ru/shepelyavost' or i=='https://illness.docdoc.ru/shankroid' or i=='https://illness.docdoc.ru/stenoz_pishhevoda' or i=='https://illness.docdoc.ru/skleroma' or i == 'https://illness.docdoc.ru/rinit_allergicheskij' or i == 'https://illness.docdoc.ru/mastit' or i == 'https://illness.docdoc.ru/koklush' or i == 'https://illness.docdoc.ru/dizenteriya' or i == 'https://illness.docdoc.ru/pelenochnyi_dermatit' or i == 'https://illness.docdoc.ru/daltonizm' or i == 'https://illness.docdoc.ru/gonoreia' or i == 'https://illness.docdoc.ru/bolezn_hantingtona' or i == 'https://illness.docdoc.ru/amnesia' or i == 'https://illness.docdoc.ru/allergia_inseknaya' or i == 'https://illness.docdoc.ru/slepota' or i == 'https://illness.docdoc.ru/Diabeticheskay_stopa' or i == 'https://illness.docdoc.ru/diabeticheskaja_nejropatija' or i == 'https://illness.docdoc.ru/dakriocistit' or i == 'https://illness.docdoc.ru/giperaktivnyj_mochevoj_puzyr' or i == 'https://illness.docdoc.ru/vertebro_baziljarnaja_nedostatochnost' or i == 'https://illness.docdoc.ru/virilnyj_sindrom' or i == 'https://illness.docdoc.ru/vezikulit' or i == 'https://illness.docdoc.ru/bolezn_bouena' or i == 'https://illness.docdoc.ru/Blefarit' or i == 'https://illness.docdoc.ru/atonija_mochevogo_puzyrja' or i == 'https://illness.docdoc.ru/astenopija' or i == 'https://illness.docdoc.ru/ambliopija' or i == 'https://medihost.ru/glossary/diseases/borodavki_71' or i == 'https://illness.docdoc.ru/panicheskaja_ataka' or i == 'https://illness.docdoc.ru/pnevmonia_atipichnaya' or i == 'https://illness.docdoc.ru/toksidermija' or i == 'https://illness.docdoc.ru/feochromotsitoma' or i == 'https://illness.docdoc.ru/iazvennyi_kolit' or i == 'https://illness.docdoc.ru/tseliakiia' or i == 'https://illness.docdoc.ru/pnevmonia_atipichnaya' or i == 'https://illness.docdoc.ru/psihoz' or i == 'https://illness.docdoc.ru/poslerodovaya_depressiya' or i == 'https://illness.docdoc.ru/poliomielit' or i == 'https://illness.docdoc.ru/nejrosifilis' or i == 'https://illness.docdoc.ru/nevinashivanie_beremennosti' or i == 'https://illness.docdoc.ru/meteorizm' or i == 'https://illness.docdoc.ru/kartavost' or i == 'https://illness.docdoc.ru/jododeficit' or i == 'https://illness.docdoc.ru/displazija_shejki_matki' or i == 'https://illness.docdoc.ru/giperkaltsiemiya' or i == 'https://illness.docdoc.ru/allergicheslii_dermatit' or i == 'https://illness.docdoc.ru/kontaktnyi_dermatit' or i == 'https://illness.docdoc.ru/atroficheskij_gastrit' or i == 'https://illness.docdoc.ru/difteriya' or i == 'https://illness.docdoc.ru/gipokaltsiemiya' or i == 'https://illness.docdoc.ru/Gigroma' or i == 'https://illness.docdoc.ru/vykidysh' or i == 'https://illness.docdoc.ru/evstahiit' or i == 'https://illness.docdoc.ru/artrit' or i == 'https://illness.docdoc.ru/gepatit_e' or i == 'https://illness.docdoc.ru/ateroskleroz':
        continue
    else:
        hammasi = driver.find_element(By.XPATH, '//*[@id="diseases_article_static_content"]').text
        data0 = hammasi.split(' ')
        data0[3] = '$'
        data = list(data0)
        data1 = data.index('совет') + 1
        data[data1] = '$$'
        data2 = data0[4:data1]
        data4 = ' '.join(map(str, data2))
        data5 = data4.split('\n')
        data5_1 = data4.split('-')
        # print(data5_1)
        title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text

        title_litle = title.casefold()
        title1 = title.split(' ')
        title2 = len(title1)
        data_str = ' '.join(map(str, data5))
        all_data = driver.find_element(By.XPATH, '//*[@id="diseases_article_static_content"]').text
        all_data1 = all_data.split('\n')
        all_data2 = ' '.join(map(str, all_data1))
        all_data3 = all_data2.split(' ')

        for i in data5:
            if i == "Причины":
                try:
                    kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                                                     'h1').text
                    print('1--------', kasallik_nomi)
                    index = data5.index('Причины')
                    data6 = data5[1:index]
                    k_haqida1 = ' '.join(map(str, data6))
                    k_haqida2 = k_haqida1.split('–')
                    k_haqida = k_haqida2[1]

                    print('2------', k_haqida)
                    try:

                        data_str = ' '.join(map(str, data5))
                        dataX = data_str.split(' ')
                        # print(dataX)
                        index3 = dataX.index('Симптомы')
                        index33 = dataX.index('Причины') + 1
                        data8 = dataX[index33:index3]
                        data_str1 = ' '.join(map(str, data8))
                        k_sabablari = data_str1
                        print('3------', k_sabablari)
                    except:
                        try:
                            dataX = data_str.split(' ')
                            data_p = dataX.index('Причины')
                            data_r = dataX.index('Симптомы')
                            data_alls = dataX[data_r] + title_litle
                            data_m = dataX.index(data_alls)
                            data_k = ' '.join(map(str, data_m))
                            k_sabablari = data_k
                            print('3.1------', k_sabablari)
                        except:
                            dataX = data_str.split(' ')
                            data_p = dataX.index('Причины')
                            data_r = dataX.index('Симптомы')
                            if data_r > data_p:
                                data_lv = dataX.index('Лучшие')
                                data_m1 = dataX[data_p:data_lv]
                                data_m2 = ' '.join(map(str, data_m1))
                                k_sabablari = data_m2
                                print('3.2-----', k_sabablari)

                    try:
                        index_data = all_data3.index('Симптомы') + title2 + 1
                        index_data_end = all_data3.index('последствиями.') - 17
                        data_get = all_data3[index_data:index_data_end]
                        k_asoratlari1 = ' '.join(map(str, data_get))
                        all_new_data = []
                        for h in range(0, 2, 1):
                            new_data = \
                                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                            'ul')[
                                    h].find_elements(By.TAG_NAME, 'li')[0].text
                            new_data1 = new_data.split(' ')
                            # new_data2 = ' '.join(map(str, new_data1))
                            all_new_data.append(new_data1)
                            # print(new_data1)

                        # k_asoratlari = ' '.join(map(str, all_new_data[1]))
                        try:
                            if 'Cтаж' not in all_new_data[2]:
                                k_asoratlari = list(all_new_data[2])
                                print('4.1.1-------', k_asoratlari)

                        except:
                            try:
                                if 'Стаж' not in all_new_data[1]:
                                    k_asoratlari = list(all_new_data[1])
                                    print("4.1.0-------", all_new_data[1])
                            except:
                                if 'Стаж' not in all_new_data[
                                    0] or title == 'Болезнь Хантингтона' or 'Аллергия инсектная' or 'Эпидидимит' or 'Энтеробиоз' or 'Склерома' or 'Шанкроид' or 'Стенокардия' or 'Коклюш' or 'Ринит аллергический' or 'Дисбактериоз кишечника у детей' or 'Дизентерия' or 'Дальтонизм' or 'Дерматит пеленочный':
                                    k_asoratlari = list(all_new_data[0])
                                    print('4.1-------', all_new_data[0])

                    except:
                        try:
                            index_data = all_data3.index('Признаки') + title2 + 1
                            index_data_end = all_data3.index('последствиями.') - 17
                            data_get = all_data3[index_data:index_data_end]
                            k_asoratlari1 = ' '.join(map(str, data_get))

                            all_new_data = []
                            for h in range(0, 2, 1):
                                new_data = \
                                    driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                                        By.TAG_NAME,
                                        'ul')[
                                        h].find_elements(By.TAG_NAME, 'li')[0].text
                                new_data1 = new_data.split(' ')
                                new_data2 = ' '.join(map(str, new_data1))
                                all_new_data.append(new_data1)

                            # if title == 'Болезнь Хантингтона' or 'Аллергия инсектная' or 'Эпидидимит' or 'Энтеробиоз' or 'Склерома' or 'Шанкроид' or 'Стенокардия' or 'Коклюш' or 'Ринит аллергический' or 'Дисбактериоз кишечника у детей' or 'Дизентерия' or 'Дальтонизм' or 'Дерматит пеленочный':
                            #     k_asoratlari = ' '.join(map(str, all_new_data[0]))
                            #     print('4.4-------', k_asoratlari)

                            k_asoratlari = ' '.join(map(str, all_new_data[1]))
                            try:
                                if 'Стаж' not in k_asoratlari:
                                    k_asoratlari = ' '.join(map(str, all_new_data[1]))
                                    print("4.2.0-------", k_asoratlari)
                            except:
                                k_asoratlari = ' '.join(map(str, all_new_data[0]))
                                print('4.2-------', k_asoratlari)


                        except:
                            index3 = dataX.index('Симптомы')
                            index44 = dataX.index('обнаружили')
                            title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                                                     'h1').text
                            title1 = title.split(' ')
                            title2 = len(title1)
                            index55 = index3 + title2 + 1
                            index45 = index44 - 2
                            data_k_asoratlari = dataX[index55:index45]
                            data_k_asoratlari_str = ' '.join(map(str, data_k_asoratlari))
                            k_asoratlari1 = data_k_asoratlari_str

                            all_new_data = []
                            for h in range(0, 2, 1):
                                new_data = \
                                    driver.find_element(By.ID, 'diseases_article_static_content').find_elements(
                                        By.TAG_NAME,
                                        'ul')[
                                        h].find_elements(By.TAG_NAME, 'li')[0].text
                                new_data1 = new_data.split(' ')
                                new_data2 = ' '.join(map(str, new_data1))
                                all_new_data.append(new_data1)

                            k_asoratlari = ' '.join(map(str, all_new_data[1]))
                            try:
                                if 'Стаж' not in k_asoratlari:
                                    k_asoratlari = ' '.join(map(str, all_new_data[1]))
                                    print("4.3.0-------", k_asoratlari)
                            except:
                                k_asoratlari = ' '.join(map(str, all_new_data[0]))
                                print('4.3-------', k_asoratlari)

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
                    data_l1 = all_data3.index('Лечение') + title2 + 1
                    index_lecheniye1 = dataX.index('Лечение')
                    data_l = all_data3.index('Лечение') + title2
                    data_a = all_data3.index('Профилактика')
                    try:
                        if title == 'Аноргазмия':
                            data_b = all_data3.index('Лечение') + title2 + 1
                            data_c = all_data3.index('Профилактика')
                            data_3 = all_data3[data_b:data_c]
                            k_davolanish = ' '.join(map(str, data_3))
                            print('6.0.1--------', k_davolanish, '\n')

                        indexA = dataX.index('Нужен')
                        index_lecheniye = dataX.index('Лечение')
                        if index_lecheniye > dataX.index('Диагностика'):
                            index_lecheniye_text = index_lecheniye + title2 + 1
                            index_text = dataX[index_lecheniye_text:indexA]
                            # index_text1 = dataX[dataX[index_lecheniye_text:indexA]:indexB]
                            if 'Стаж' not in index_text:
                                k_davolanish = ' '.join(map(str, index_text))
                                print('6-----------', k_davolanish, '\n')

                                data_l = all_data3.index('Лечение') + title2
                                indexA = dataX.index('Нужен')
                                index_lecheniye1 = dataX.index('Лечение')
                            elif index_lecheniye1 > dataX.index('Диагностика'):
                                data_o = all_data3.index('Опасность')
                                data_l1 = all_data3.index('Лечение') + title2 + 1
                                data_ll = all_data3[data_l1:data_o]
                                k_davolanish = ' '.join(map(str, data_ll))
                                print('6.1-------', k_davolanish, '\n')

                            elif all_data3.index('Диета') > all_data3.index('Лечение') or all_data3.index(
                                    'Профилактика') > all_data3.index('Лечение'):
                                try:
                                    data_d = all_data3.index('Диета')
                                    all_datas = all_data3[data_l1:data_d]
                                    k_davolanish = ' '.join(map(str, all_datas))
                                    print('6.2--------', k_davolanish, '\n')
                                except:
                                    data_d1 = all_data3.index('Профилактика')
                                    all_datas1 = all_data3[data_l1:data_d1]
                                    k_davolanish = ' '.join(map(str, all_datas1))
                                    print('6.3--------', k_davolanish, '\n')

                    except:
                        print('not found data!!!', '\n')
                    # cursor.execute(
                    #     "INSERT INTO illnesses (title, description,reasons,diagnoses,symptoms,treatments) VALUES (%s,%s,%s,%s,%s,%s)",
                    #     (kasallik_nomi, k_haqida, k_sabablari, k_diagnostika, k_asoratlari, k_davolanish))
                    # connect.commit()
                    # a = cursor.execute('SELECT * FROM illnesses').fetchone()
                    # print(a)
                    # cursor.execute(
                    #     "Update illnesses set created_at= %s, updated_at = %s, published_at = %s",
                    #     ("2022-09-06T05:25:41.666Z", "2022-09-06T05:25:41.666Z",
                    #      "2022-09-06T05:25:41.113Z"))
                    # connect.commit()

                except:
                    continue
driver.close()
