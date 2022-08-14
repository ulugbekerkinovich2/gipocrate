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
    if i == 'https://illness.docdoc.ru/tsitomegalovirus' or i == 'https://illness.docdoc.ru/evstahiit' or i == 'https://illness.docdoc.ru/beshenstvo' or i == 'https://illness.docdoc.ru/jododeficit' or i == 'https://illness.docdoc.ru/alopetsiia' or i == 'https://illness.docdoc.ru/ishemicheskaiia_bolezn_serdtsa' or i == 'https://illness.docdoc.ru/pnevmonia_atipichnaya' or i == 'https://illness.docdoc.ru/poliomielit' or i == "https://illness.docdoc.ru/pnevmonia_atipichnaya" or i == 'https://illness.docdoc.ru/mialgija' or i == 'https://illness.docdoc.ru/narkomania' or i == 'https://illness.docdoc.ru/nevrit' or i == 'https://illness.docdoc.ru/ozhirenie' or i == 'https://illness.docdoc.ru/otomikoz' or i == 'https://illness.docdoc.ru/paranoiya' or i == 'https://illness.docdoc.ru/rozatsea' or i == 'https://illness.docdoc.ru/rozha' or i == 'https://illness.docdoc.ru/perikardit' or i == 'https://illness.docdoc.ru/periodontit' or i == 'https://illness.docdoc.ru/sarkoidoz' or i == 'https://illness.docdoc.ru/takhikardiya' or i == 'https://illness.docdoc.ru/holera' or i == 'https://illness.docdoc.ru/kista_meniska' or i == 'https://illness.docdoc.ru/ekhinokokkoz' or i == 'https://illness.docdoc.ru/iazvennyi_kolit' or i == 'https://illness.docdoc.ru/yachmen' or i == 'https://illness.docdoc.ru/jashhur' or i == 'https://illness.docdoc.ru/Gigroma' or i == 'https://illness.docdoc.ru/girsutizm' or i == 'https://illness.docdoc.ru/depression' or i == 'https://illness.docdoc.ru/cinga' or i == 'https://illness.docdoc.ru/giperplazija_jendometrija' or i == 'https://illness.docdoc.ru/vrosshij_nogot':
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
# print(data)
data1 = data.index('совет') + 1
# print(data1)
data[data1] = '$$'
#
data2 = data0[4:]
# print(data2)
data4 = ' '.join(map(str, data2))
# print(data4)
data5 = data4.split('\n')
# print('++++++', data5)
# break
title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
title1 = title.split(' ')
title2 = len(title1)
for i in data5:
    if i == "Причины":
        try:
            kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                                             'h1').text
            print('--------', kasallik_nomi)
            # cursor.execute("INSERT INTO basic_app_болезни1 (title) VALUES (?)", (kasallik_nomi,))
            # connect.commit()
            # a = cursor.execute('SELECT * FROM basic_app_kasallik_haqida')
            # print(a)

            # print(data5)
            index = data5.index('Причины')
            data6 = data5[1:index]
            k_haqida = ' '.join(map(str, data6))
            print('------', k_haqida)

            data_str = ' '.join(map(str, data5))
            # print(data_str)
            dataX = data_str.split(' ')
            # print('0000',dataX)
            index3 = dataX.index('Симптомы')
            index33 = dataX.index('Причины') + 1
            data8 = dataX[index33:index3]
            # print(data8)
            data_str1 = ' '.join(map(str, data8))
            k_sabablari = data_str1
            print('------', k_sabablari)

            # print(dataX)
            if dataX.index('Лучшие') > dataX.index('Если'):
                index44 = dataX.index('Если')
                title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME,
                                                                                         'h1').text
                title1 = title.split(' ')
                title2 = len(title1)
                index55 = index3 + title2 + 1
                data_k_asoratlari = dataX[index55:index44]
                data_k_asoratlari_str = ' '.join(map(str, data_k_asoratlari))
                k_asoratlari = data_k_asoratlari_str
                print('------', k_asoratlari)


                word1 = dataX.index('Диагностика')
                word = dataX.index('Лечение') + title2 + 1
                word2 = list(dataX[word])
            try:
                counter = 0
                array = []

                for a in dataX:
                    if a == 'Лечение':
                        counter +=1
                        array.append(dataX.index(a))

                array = [index for index, element in enumerate(dataX) if element == 'Лечение']

                for i in range(0, counter):

                    if 1040 <= ord(word2[0]) < 1071:
                        word2 = dataX[array[i]]
                        print(word2)
                    else:
                        yjj = array[i]

                if 1040 <= ord(word2[0]) < 1071:
                    print('ishladi')
                index66 = dataX.index('Диагностика')
                # print(index66)
                index67 = index66 + 1
                index77 = dataX.index('Лечение')
                data_k_diagnostika = dataX[index67:yjj]
                data_k_diagnostika_str = ' '.join(map(str, data_k_diagnostika))
                k_diagnostika = data_k_diagnostika_str
                print('+-----', k_diagnostika)
            except:


                if dataX[dataX.index('Лечение') +3] == title2:


                    indexA = dataX.index('Нужен')
                    index_lecheniye = dataX.index('Лечение')
                    if index_lecheniye_text != dataX.index('Диагностика')+1:
                        index_lecheniye_text = index_lecheniye + title2 + 1
                        index_text = dataX[index_lecheniye_text:indexA]
                        k_davolanish = ' '.join(map(str, index_text))
                        print('++---------', k_davolanish)

            # cursor.execute(
            #     "INSERT INTO basic_app_болезни1 (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
            #     (kasallik_nomi, k_haqida, k_sabablari, k_asoratlari, k_diagnostika, k_davolanish))
            # connect.commit()
            # a = cursor.execute('SELECT * FROM basic_app_болезни1')
            # print(a)

        except:
            continue

driver.close()
