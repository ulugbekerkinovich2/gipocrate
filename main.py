import sqlite3

# from selenium2 import kasallik_nomi

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
for i in range(1, 9):
    i = input('nimadir yoz!... ')
    cursor.execute("INSERT INTO basic_app_kasallik_nomi (kasallik_nomi) VALUES (?)", (i,))
    connect.commit()
a = cursor.execute('SELECT * FROM basic_app_kasallik_nomi')
print(a)
# connect.commit()
# row = cursor.execute('SELECT * FROM basic_app_kasallik_nomi ').fetchall()
# cursor.execute('INSERT INTO * FROM basic_app_kasllik_nomi (kasallik_nomi) VALUES (?)', ('anvar'))
# print(row)hhh
# cursor.execute("INSERT INTO basic_app_kasallik_nomi (kasallik_nomi) VALUES ('testing')")
# connect.commit()
# row = cursor.execute('SELECT * FROM basic_app_kasallik_nomi').fetchall()
# print(row)
# cursor.execute('DELETE FROM basic_app_kasallik_nomi')
# # print(cursor.execute('SELECT * FROM basic_app_kasallik_nomi').fetchall())
# connect.commit()
connect.close()

# connect.close()
# row = cursor.execute('SELECT * FROM basic_app_kasallik_nomi ').fetchall()
# print(row)
# row1 = cur.execute('SELECT * FROM basic_app_kasallik_nomi').fetchall()
# print(row1)a




# print(list_links)
# print(len(list_links))
# text = driver.find_element(By.XPATH, '//*[@id="inner_main"]/div[2]/div').text
# for a in list_links:
#     print(a)
#     driver.get(f'{a}')
#     if not a == 'https://medihost.ru/glossary/diseases/abscess_golovnogo_mozga_149' or i=='https://illness.docdoc.ru/displazija_shejki_matki' or i=='https://illness.docdoc.ru/allergicheslii_dermatit' or i=='https://illness.docdoc.ru/giperkaltsiemiya' or a=='https://medihost.ru/glossary/diseases/adenoma_schitovidnoy_zhelezy_570' or a=='https://medihost.ru/glossary/diseases/akromegaliya_569' or a == 'https://medihost.ru/glossary/diseases/adenoidy_gipertrofiya_glotochnoy_mindaliny__195':
#         print(text, '\n\n')
#         continue

# print(text)
# data = text.split(' ')
# data1 = ' '.join(map(str, data))
# data2 = data1.split('\n')
# data3 = ' '.join(map(str, data2))
# data4 = data3.split(' ')
#
# # print(data4)
#
# data_index = data4.index('Причины')
# data5 = data4[:data_index]
# k_haqida = ' '.join(map(str, data5))
# print(k_haqida)
#
# data_index1 = data4.index('Симптомы')
# data6 = data4[data_index + 1: data_index1]
# k_sabablari = ' '.join(map(str, data6))
# print(k_sabablari)
#
# data_index2 = data4.index('Диагностика')
# data7 = data4[data_index1 + 1: data_index2]
# k_asoratlari = ' '.join(map(str, data7))
# print(k_asoratlari)
#
# data_index3 = data4.index('Лечение')
# data8 = data4[data_index2 + 1:data_index3]
# diagnostika = ' '.join(map(str, data8))
# print(diagnostika)
#
# data_index4 = data4.index('Порекомендуйте')
# data9 = data4[data_index3 + 1: data_index4]
# davolanish = ' '.join(map(str, data9))
# print(davolanish)
