import sqlite3

from selenium import webdriver
from selenium.webdriver.common.by import By

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
driver = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")

driver.get("https://medihost.ru/zabolevanya")
links = driver.find_elements(By.TAG_NAME, 'a')
list_links = []
i = 0
for lnk in links:
    # print(lnk.get_attribute("href"), i)
    a = lnk.get_attribute('href')

    if 80 <= i < 743:
        list_links.append(a)
    i += 1

# print(len(list_links), list_links)

for f in list_links:
    if f == 'https://medihost.ru/glossary/diseases/bolezn_bouena_557' or f == 'https://medihost.ru/glossary/diseases/yazvennyy_gingivit_275' or f == 'https://medihost.ru/glossary/diseases/epitelioma_647' or f == 'https://medihost.ru/glossary/diseases/enurez_287' or f == 'https://medihost.ru/glossary/diseases/hondroma_410' or f == 'https://medihost.ru/glossary/diseases/hrap_431' or f == 'https://medihost.ru/glossary/diseases/tendovaginit_684' or f == 'https://medihost.ru/glossary/diseases/sinehiya_626' or f == 'https://medihost.ru/glossary/diseases/pupochnaya_gryzha_551' or f == 'https://medihost.ru/glossary/diseases/piodermiya_699' or f == 'https://medihost.ru/glossary/diseases/pigmentnye_pyatna_609' or f == 'https://medihost.ru/glossary/diseases/periodontit_623' or f == 'https://medihost.ru/glossary/diseases/otit_166' or f == 'https://medihost.ru/glossary/diseases/otsloyka_setchatki_703' or f == 'https://medihost.ru/glossary/diseases/otomikoz_661' or f == 'https://medihost.ru/glossary/diseases/meteorizm_612' or f == 'https://medihost.ru/glossary/diseases/nederzhanie_mochi_u_zhenschin_504' or f == 'https://medihost.ru/glossary/diseases/narusheniya_menstrualnogo_cikla_536' or f == 'https://medihost.ru/glossary/diseases/myshechnyy_spazm_533' or f == 'https://medihost.ru/glossary/diseases/mochekamennaya_bolezn_532' or f == 'https://medihost.ru/glossary/diseases/mitralnyy_stenoz_510' or f == 'https://medihost.ru/glossary/diseases/lipoma_250' or f == 'https://medihost.ru/glossary/diseases/koksartroz_sustavov_601' or f == 'https://medihost.ru/glossary/diseases/leykemiya_538' or f == 'https://medihost.ru/glossary/diseases/apatiya_638' or f == 'https://medihost.ru/glossary/diseases/bolezn_gyuntera_558' or f == 'https://medihost.ru/glossary/diseases/bolezn_pika_562' or f == 'https://medihost.ru/glossary/diseases/bolezn_uippla_561' or f == 'https://medihost.ru/glossary/diseases/vaskulit_312' or f == 'https://medihost.ru/glossary/diseases/vegeto_sosudistaya_distoniya_107' or f == 'https://medihost.ru/glossary/diseases/vitiligo_73' or f == 'https://medihost.ru/glossary/diseases/vnutrennyaya_gryzha_132' or f == 'https://medihost.ru/glossary/diseases/dakriocistit_228' or f == 'https://medihost.ru/glossary/diseases/vulvovaginit_584' or f == 'https://medihost.ru/glossary/diseases/zaglotochnyy_abscess_232' or f == 'https://medihost.ru/glossary/diseases/gestoz_369' or f == 'https://medihost.ru/glossary/diseases/gidradenit_531' or f == 'https://medihost.ru/glossary/diseases/giperkeratoz_706' or f == 'https://medihost.ru/glossary/diseases/gipertonicheskiy_kriz_548' or f == 'https://medihost.ru/glossary/diseases/diabeticheskaya_retinopatiya_226' or f == 'https://medihost.ru/glossary/diseases/disbakterioz_540':
        continue
    driver.get(f"{f}")
    all_data = driver.find_element(By.CLASS_NAME, 'one_disease_container').text
    title = driver.find_element(By.ID, 'content_header').find_element(By.TAG_NAME, 'h1').text

    data_split = all_data.split('\n')
    # print(data_split)
    data_split_list = ' '.join(map(str, data_split))
    data_split1 = data_split_list.split(' ')
    try:
        if ('Причины' and 'Симптомы' and 'Диагностика' and 'Лечение') in data_split1:
            # print(title + "\n")
            kasallik_nomi = driver.find_element(By.ID, 'content_header').find_element(By.TAG_NAME, 'h1').text
            print('1--------', kasallik_nomi)
            try:
                data0 = data_split1.index('Причины')
                data = data_split1[:data0]
                data1 = ' '.join(map(str, data))
                k_haqida = data1
                print('1---', k_haqida)
            except:
                data0 = data_split1.index('ПРИЧИНЫ,')
                data = data_split1[:data0]
                data1 = ' '.join(map(str, data))
                k_haqida = data1
                print('1.1---', k_haqida)

            try:
                data2 = data_split1.index('Симптомы')
                data3 = data_split1[data0 + 1:data2]
                k_sabablari = ' '.join(map(str, data3))
                er_data = k_sabablari.split(' ')
                if er_data[0] == 'и':
                    k_sabablari = er_data[0].replace('и', ' ')
                    k_sabablari = ' '.join(map(str, k_sabablari))
                    print('2---', k_sabablari)
                else:
                    print('2---', k_sabablari)
            except:
                try:
                    data2 = data_split1.index('Проявления')
                    data3 = data_split1[data0 + 1:data2]
                    k_sabablari = ' '.join(map(str, data3))
                    er_data = k_sabablari.split(' ')
                    if er_data[0] == 'и':
                        k_sabablari = er_data[0].replace('и', ' ')
                        k_sabablari = ' '.join(map(str, k_sabablari))
                        print('2.1---', k_sabablari)
                    else:
                        print('2.1---', k_sabablari)
                except:
                    try:
                        data2 = data_split1.index('Симптомы')
                        data3 = data_split1[data0 + 1:data2]
                        k_sabablari = ' '.join(map(str, data3))
                        er_data = k_sabablari.split(' ')
                        if er_data[0] == 'и':
                            k_sabablari = er_data[0].replace('и', ' ')
                            k_sabablari = ' '.join(map(str, k_sabablari))
                            print('2.2---', k_sabablari)
                        else:
                            print('2.2---', k_sabablari)

                    except:
                        data2 = data_split1.index('СИМПТОМЫ')
                        data3 = data_split1[data0 + 1:data2]
                        k_sabablari = ' '.join(map(str, data3))
                        er_data = k_sabablari.split(' ')
                        if er_data[0] == 'и':
                            k_sabablari = er_data[0].replace('и', ' ')
                            k_sabablari = ' '.join(map(str, k_sabablari))
                            print('2.2---', k_sabablari)
                        else:
                            print('2.2---', k_sabablari)

            try:
                data2 = data_split1.index('Симптомы')
                data02 = data_split1.index('Диагностика')
                data4 = data_split1[data2 + 1:data02]
                k_asoratlari = ' '.join(map(str, data4))
                print('3----', k_asoratlari)
            except:
                data02 = data_split1.index('ДИАГНОСТИЧЕСКАЯ')
                data4 = data_split1[data2 + 1:data02]
                k_asoratlari = ' '.join(map(str, data4))
                er_data = k_asoratlari.split(' ')
                if er_data[0] == 'и':
                    k_asoratlari = er_data[0].replace('и', ' ')
                    k_asoratlari = ' '.join(map(str, k_asoratlari))
                    print('3.1----', k_asoratlari)
                else:
                    print('3.1----', k_asoratlari)
            try:
                data02 = data_split1.index('Диагностика')
                data03 = data_split1.index('Лечение')
                data5 = data_split1[data02 + 1:data03]
                k_diagnostika = ' '.join(map(str, data5))
                er_data = k_diagnostika.split(' ')
                if er_data[0] == 'и':
                    k_diagnostika = er_data[0].replace('и', ' ')
                    k_diagnostika = ' '.join(map(str, k_diagnostika))
                    print('4----', k_diagnostika)
                else:
                    print('4----', k_diagnostika)
            except:
                data03 = data_split1.index('ЛЕЧЕБНАЯ')
                data5 = data_split1[data02 + 1:data03]
                k_diagnostika = ' '.join(map(str, data5))
                er_data = k_diagnostika.split(' ')
                if er_data[0] == 'и':
                    k_diagnostika = er_data[0].replace('и', ' ')
                    k_diagnostika = ' '.join(map(str, k_diagnostika))
                    print('4.1----', k_diagnostika)
                else:
                    print('4.1----', k_diagnostika)
            data04 = data_split1[data03 + 1:]
            k_davolanish = ' '.join(map(str, data04))
            print('5----', k_davolanish, '\n')

            cursor.execute(
                "INSERT INTO basic_app_болезни (title, description,description1,description2,description3,description4) VALUES (?,?,?,?,?,?)",
                (kasallik_nomi, k_haqida, k_sabablari, k_asoratlari, k_diagnostika, k_davolanish))
            connect.commit()
            a = cursor.execute('SELECT * FROM basic_app_болезни1')
            print(a)


        else:
            continue


    except:
        continue

driver.close()
