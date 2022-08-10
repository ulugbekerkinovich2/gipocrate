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
    # kasallik_nomi = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
    # kasallik_nomi1 = kasallik_nomi.capitalize()

    # print(kasallik_nomi1)
    # if not i == "https://illness.docdoc.ru/pnevmonia_atipichnaya" or i == 'https://illness.docdoc.ru/mialgija' or i == 'https://illness.docdoc.ru/narkomania' or i == 'https://illness.docdoc.ru/nevrit' or i == 'https://illness.docdoc.ru/ozhirenie' or i == 'https://illness.docdoc.ru/otomikoz' or i == 'https://illness.docdoc.ru/paranoiya' or i == 'https://illness.docdoc.ru/rozatsea' or i == 'https://illness.docdoc.ru/rozha' or i == 'https://illness.docdoc.ru/perikardit' or i == 'https://illness.docdoc.ru/periodontit' or i == 'https://illness.docdoc.ru/sarkoidoz' or i == 'https://illness.docdoc.ru/takhikardiya' or i == 'https://illness.docdoc.ru/holera' or i == 'https://illness.docdoc.ru/kista_meniska' or i == 'https://illness.docdoc.ru/ekhinokokkoz' or i == 'https://illness.docdoc.ru/iazvennyi_kolit' or i == 'https://illness.docdoc.ru/yachmen' or i == 'https://illness.docdoc.ru/jashhur' or i == 'https://illness.docdoc.ru/Gigroma' or i == 'https://illness.docdoc.ru/girsutizm' or i == 'https://illness.docdoc.ru/depression' or i == 'https://illness.docdoc.ru/cinga' or i == 'https://illness.docdoc.ru/giperplazija_jendometrija':
    # nomi = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.CLASS_NAME,
    #                                                                                   'illnes-short-description').text
    # print(nomi)
    #
    # if driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h2').text == 'Причины':
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
    # break
    for i in data5:
        # print(i)

        # break
        if i == "Причины":
            try:
                print(data5)
                index = data5.index('Причины')
                data6 = data5[1:index]
                k_haqida = ' '.join(map(str, data6))
                # print(k_haqida)


                data_str = ' '.join(map(str, data5))
                # print(data_str)
                dataX = data_str.split(' ')
                # print(dataX)
                index3 = dataX.index('Симптомы')
                index33 = dataX.index('Причины') + 1
                data8 = dataX[index33:index3]
                # print(data8)
                data_str1 = ' '.join(map(str, data8))
                k_sabablari = data_str1
                # print(k_sabablari)

                # print(dataX)
                index44 = dataX.index('Если')
                title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
                title1 = title.split(' ')
                title2 = len(title1)
                index55 = index3 + title2 + 1
                data_k_asoratlari = dataX[index55:index44]
                data_k_asoratlari_str = ' '.join(map(str, data_k_asoratlari))
                k_asoratlari = data_k_asoratlari_str
                # print(k_asoratlari)
                index66 = dataX.index('Диагностика')
                # print(index66)
                index67 = index66 + 1
                index77 = dataX.index('Лечение')
                data_k_diagnostika = dataX[index67:index77]
                data_k_diagnostika_str = ' '.join(map(str, data_k_diagnostika))
                k_diagnostika = data_k_diagnostika_str
                print(k_diagnostika)
            except:
                continue
                # index = data5.index('Причины')
                # data6 = data5[0:index]
                # k_haqida = data6[1]
                # # print(k_haqida)
                #
                # data_str = ' '.join(map(str, data5))
                # # print(data_str)
                # dataX = data_str.split(' ')
                # # print(dataX)
                # index3 = dataX.index('Симптомы')
                # index33 = dataX.index('Причины') + 1
                # data8 = dataX[index33:index3]
                # # print(data8)
                # data_str1 = ' '.join(map(str, data8))
                # k_sabablari = data_str1
                # # print(k_sabablari)
                #
                # print(dataX)
                # index44 = dataX.index('Если')
                # title = driver.find_element(By.CLASS_NAME, 'library__ills').find_element(By.TAG_NAME, 'h1').text
                # title1 = title.split(' ')
                # title2 = len(title1)
                # index55 = index3 + title2 + 1
                # data_k_asoratlari = dataX[index55:index44]
                # data_k_asoratlari_str = ' '.join(map(str, data_k_asoratlari))
                # k_asoratlari = data_k_asoratlari_str
                # # print(k_asoratlari)
                # index66 = dataX.index('Диагностика')
                # print(index66)
                # index67 = index66 + 1
                # index77 = dataX.index('Лечение')
                # data_k_diagnostika = dataX[index67:index77]
                # data_k_diagnostika_str = ' '.join(map(str, data_k_diagnostika))
                # k_diagnostika = data_k_diagnostika_str
                # print(k_diagnostika)

        # break

    # break
# break

# print(data4)
# break
# data3 = []

driver.close()
