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
    if i == 'https://illness.docdoc.ru/tsitomegalovirus' or i == 'https://illness.docdoc.ru/feochromotsitoma' or i == 'https://illness.docdoc.ru/kuperoz' or i == 'https://illness.docdoc.ru/kolpit' or i == 'https://illness.docdoc.ru/Kandidoz' or i == 'https://illness.docdoc.ru/Cianoz' or i == 'https://illness.docdoc.ru/Andocervicit' or i == 'https://illness.docdoc.ru/chasto_boleushie_deti' or i == 'https://illness.docdoc.ru/trombocitopenija_purpura' or i == 'https://illness.docdoc.ru/Rak_shitovidnoy_zhelezy' or i == 'https://illness.docdoc.ru/infarkt_miokarda' or i == 'https://illness.docdoc.ru/gepatit_d' or i == 'https://illness.docdoc.ru/ateroskleroz' or i == 'https://illness.docdoc.ru/Natoptyshi' or i == 'https://illness.docdoc.ru/evstahiit' or i == 'https://illness.docdoc.ru/beshenstvo' or i == 'https://illness.docdoc.ru/jododeficit' or i == 'https://illness.docdoc.ru/alopetsiia' or i == 'https://illness.docdoc.ru/ishemicheskaiia_bolezn_serdtsa' or i == 'https://illness.docdoc.ru/pnevmonia_atipichnaya' or i == 'https://illness.docdoc.ru/poliomielit' or i == "https://illness.docdoc.ru/pnevmonia_atipichnaya" or i == 'https://illness.docdoc.ru/mialgija' or i == 'https://illness.docdoc.ru/narkomania' or i == 'https://illness.docdoc.ru/nevrit' or i == 'https://illness.docdoc.ru/ozhirenie' or i == 'https://illness.docdoc.ru/otomikoz' or i == 'https://illness.docdoc.ru/paranoiya' or i == 'https://illness.docdoc.ru/rozatsea' or i == 'https://illness.docdoc.ru/rozha' or i == 'https://illness.docdoc.ru/perikardit' or i == 'https://illness.docdoc.ru/periodontit' or i == 'https://illness.docdoc.ru/sarkoidoz' or i == 'https://illness.docdoc.ru/takhikardiya' or i == 'https://illness.docdoc.ru/holera' or i == 'https://illness.docdoc.ru/kista_meniska' or i == 'https://illness.docdoc.ru/ekhinokokkoz' or i == 'https://illness.docdoc.ru/iazvennyi_kolit' or i == 'https://illness.docdoc.ru/yachmen' or i == 'https://illness.docdoc.ru/jashhur' or i == 'https://illness.docdoc.ru/Gigroma' or i == 'https://illness.docdoc.ru/girsutizm' or i == 'https://illness.docdoc.ru/depression' or i == 'https://illness.docdoc.ru/cinga' or i == 'https://illness.docdoc.ru/giperplazija_jendometrija' or i == 'https://illness.docdoc.ru/vrosshij_nogot':
        continue
    hammasi = driver.find_element(By.XPATH,
                                  '/html/body/section[1]/section/div[1]/div[1]/div[3]/div[3]/div/div[2]/div[3]/div').text

    # print(hammasi.split(' '))
    #
    # hammasi2 = driver.find_element(By.XPATH, '//*[@id="id="diseases_article_static_content"]').text
    data0 = hammasi.split(' ')
    # print(data0)
    data0[3] = '$'
    data = list(data0)
    data1 = data.index('совет') + 1
    # print(data1)
    data[data1] = '$$'
    #
    data2 = data0[4:data1]
    data4 = ' '.join(map(str, data2))
    data5 = data4.split('\n')
    # print('++++++', data5)
    # print()
    # break
    title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
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

                data_str = ' '.join(map(str, data5))
                dataX = data_str.split(' ')
                # print(dataX)
                index3 = dataX.index('Симптомы')
                index33 = dataX.index('Причины') + 1
                data8 = dataX[index33:index3]
                data_str1 = ' '.join(map(str, data8))
                k_sabablari = data_str1
                print('3------', k_sabablari)

                # print(dataX.index('Лучшие'))
                # print(dataX.index('обнаружили'))

                if dataX.index('Лучшие') - dataX.index('обнаружили') == 16:
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


                index66 = dataX.index('Диагностика')
                index67 = index66 + 1
                index77 = dataX.index('Лечение')
                data_k_diagnostika = dataX[index67:index77]
                data_k_diagnostika_str = ' '.join(map(str, data_k_diagnostika))
                k_diagnostika = data_k_diagnostika_str
                print('5------', k_diagnostika)

                indexA = dataX.index('Нужен')
                index_lecheniye = dataX.index('Лечение')
                index_lecheniye_text = index_lecheniye + title2 + 1
                index_text = dataX[index_lecheniye_text:indexA]
                k_davolanish = ' '.join(map(str, index_text))
                print('6-----------', k_davolanish + '\n')

        # cursor.execute(
        #     "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
        #     (kasallik_nomi, k_haqida, k_sabablari, k_asoratlari, k_diagnostika, k_davolanish))
        # connect.commit()
        # a = cursor.execute('SELECT * FROM basic_app_болезни1')
        # print(a+'\n')

            except:
                continue

driver.close()
