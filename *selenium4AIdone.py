# import sqlite3

import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from links_all_pills import list_alphabet_all2

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print('ornatildi')
# connect = sqlite3.connect('db.sqlite3')
# driver.get("https://www.lsgeotar.ru/pages/abc-pharma_tn.html")
# links = driver.find_elements(By.TAG_NAME, 'a')
# # print("Opened database successfully")
# list_links = []
# my_links = []
# ettdb_links = []
# a = 0
#
# for link in links:
#     link_l = link.get_attribute('href')
#     # print(link.get_attribute('href'), a)
#     a += 1
#
#     if 24 <= a < 57:
#         my_links.append(link_l)z
#
#     if 59 <= a < 110:
#         if a % 2 == 0:
#             list_links.append(link_l)
#
# list_alphabet = []
# list_alphabet_all = []
# list_letters = ['a', 'b', 'v', 'g', 'ye', 'zh', 'za', 'ia', 'ib', 'yo', 'ka', 've', 'de', 'ma', 'op', 'la', 'ii', 'al',
#                 'at', 'na', 'ob', 'ov', 'pa', 'ra', 'sa', 'ta', 'ub', 'uq', 'uz', 'uk', 'ul', 'fa', 'kh', 'ts', 'cha',
#                 'sha', 'eb', 'ev', 'yu', 'ya', 'vq', 'si', '10', 'ft', 'me', 'ig', 'li', 'ti']
# b = 0
# big_links = []
# for all_link in my_links:
#     driver.get(f"{all_link}")
#     links1 = driver.find_elements(By.TAG_NAME, 'a')
#     for i in links1:
#         link_l1 = i.get_attribute('href')
#         # print(link_l1, b)
#         b += 1
#         if 107 <= b < 146 or 270 <= b < 303 or 427 <= b < 467 or 591 <= b < 633 or 746 <= b < 779 or 954 <= b < 965 or 1083 <= b < 1106 or 1225 <= b < 1229 or 1340 <= b < 1403 or 1507 <= b < 1543 or 1650 <= b < 1784 or 1819 <= b < 1851 or 1981 <= b < 2002 or 2113 <= b < 2166 or 2268 <= b < 2303 or 2426 <= b < 2469 or 2580 <= b < 2626 or 2761 <= b < 2769 or 2880 <= b < 2914 or 3053 <= b < 3062 or 3198 <= b < 3223 or 3358 <= b < 3391 or 3475 <= b < 3508 or 3621 <= b < 3653:
#             try:
#                 if link_l1.startswith('https://www.lsgeotar.ru/abc'):
#                     big_links.append(link_l1)
#             except:
#                 continue
#         try:
#             for letter in list_letters:
#                 if not (link_l1.startswith('https://www.lsgeotar.ru/abc') or link_l1.startswith(
#                         'https://www.lsgeotar.ru/pages/')):
#                     if link_l1.startswith(f'https://www.lsgeotar.ru/{letter}'):
#                         list_alphabet.append(link_l1)
#
#
#
#
#         except:
#             continue
#
# # print(len(list_alphabet), list_alphabet + list_links)
# # print(len(big_links), big_links)
#
# for all_link1 in big_links:
#     driver.get(f"{all_link1}")
#     links1 = driver.find_elements(By.TAG_NAME, 'a')
#     for i in links1:
#         link_l11 = i.get_attribute('href')
#         # print(link_l1, b)
#         b += 1
#         try:
#             for letter1 in list_letters:
#                 if not (link_l11.startswith('https://www.lsgeotar.ru/abc') or link_l11.startswith(
#                         'https://www.lsgeotar.ru/pages/')):
#                     if link_l11.startswith(f'https://www.lsgeotar.ru/{letter1}'):
#                         list_alphabet_all.append(link_l11)
#         except:
#             continue
#
# # print(len(list_alphabet_all), list_alphabet_all)
#
# driver.close()

list_alphabet_all1 = list(list_alphabet_all2)
# print(len(list_alphabet_all1))
# print('starting connect to database>>...')
# connect = psycopg2.connect(
#     dbname="gippokrat", user="postgres", password="root123", host="165.232.186.199",
#     port="5432")
# connect.autocommit = True
#
# cursor = connect.cursor()
# print('connect to database.../')
for link3 in list_alphabet_all1:
    driver.get(f"{link3}")
    try:
        all_data = driver.find_element(By.XPATH,
                                       '/html/body/form[2]/div[6]/div[1]/div/main/div/div/div/div[3]/div').text
        data = all_data.split('\n')
        data1 = ' '.join(map(str, data))
        data2 = data1.split(':')
        data3 = ' '.join(map(str, data2))
        data4 = data3.split(' ')
        data5 = data4.index('препараты')
        index5_1 = data4.index('Раскрыть')

        try:
            if not (len(data4) == 1 or len(data4) == 2 or len(data4) == 3 or len(data4) == 4 or len(data4) == 5 or len(
                    data4) == 6):
                if 'Противопоказания' in data4:
                    title = driver.find_element(By.CLASS_NAME, 'value').text
                    index5_2 = data4.index('Противопоказания')
                    data7 = data4[:data5]
                    data8 = data4[index5_1 + 1:index5_2]
                    data_opisaniye = data7 + data8
                    real_data_1 = ' '.join(map(str, data_opisaniye))
                    print(title, '\n')
                    print(real_data_1)
                    if 'Способ' in data4:
                        index5_3 = data4.index('Способ')
                        data9 = data4[index5_2 + 1:index5_3]
                        real_data_2 = ' '.join(map(str, data9))
                        print(real_data_2)
                        if 'Срок' in data4:
                            index5_4 = data4.index('Срок')
                            data10 = data4[index5_3 + 1: index5_4]
                            real_data_3 = ' '.join(map(str, data10))
                            print(real_data_3)
                            if 'Показания' in data4:
                                data11 = data4.index('Показания')
                                data12 = data4[data11 + 1: index5_2]
                                real_data_4 = ' '.join(map(str, data12))
                                print(real_data_4)
                                data13 = data4.index('Производитель') - 1
                                real_data_5 = data4[data13]
                                print(real_data_5)

                                print('\n')
                                # cursor.execute(
                                #     "INSERT INTO public.pillqs  (title, description, character,  instruction, views, country) VALUES (%s,%s,%s,%s,%s,%s)",
                                #     (title, real_data_1, real_data_2, real_data_3, real_data_4, real_data_5))
                                # connect.commit()
                                # #
                                # cursor.execute(
                                #     "Update public.pillqs set created_at= %s, updated_at = %s, published_at = %s",
                                #     ("2022-09-06T05:25:41.666Z", "2022-09-06T05:25:41.666Z",
                                #      "2022-09-06T05:25:41.113Z"))
                                # connect.commit()

                                # sleep(0.5)
                                # driver.refresh()
        except:
            continue


    except:
        continue
