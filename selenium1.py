from selenium import webdriver
from selenium.webdriver.common.by import By

from drugs import drugs_A_lotin

driver = webdriver.Chrome(executable_path="/home/ulugbek/PycharmProjects/gipokrat/chromedriver")

# driver.get("https://www.rlsnet.ru/drugs/ukazatel/c0")  # ishlaydi
# driver.get("https://www.vidal.ru/drugs/products/p/rus-a")
driver.get("https://illness.docdoc.ru/alphabet/a")
# driver.get("https://www.lsgeotar.ru/abadzhio-13499.html")
# driver.maximize_window()
for i in drugs_A_lotin:
    driver.get(f"https://illness.docdoc.ru/{i}")
    if True:
        # if 'Стаж' in
        a = driver.find_element(By.CLASS_NAME, 'best-doctors__title').text
        # print(a)
        if 'Лучшие врачи по лечению' in a:

            kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                         "p").text
            print(kasallik_haqida)
            print('1--------')
            if driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                          'h2').text == 'Причины':
                kasallik_sabablari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[1].text
                kasallik_sabablari1 = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                    By.TAG_NAME, 'ul').text
                kasallik_sabablari2 = kasallik_sabablari + ' ' + kasallik_sabablari1
                print(kasallik_sabablari2)
                print('2-------')
            if 'Симптомы ' in driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                          'h2')[1].text:
                kasallik_asoratlari = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[2].text
                kasallik_asoratlari1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[1].text
                kasallik_asoratlari2 = kasallik_asoratlari + '\n' + kasallik_asoratlari1
                print(kasallik_asoratlari2)
                print('3--------')
            if "Диагностика" in \
                    driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'h2')[2].text:
                diagnostika = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
                diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
                diagnostika2 = diagnostika + '\n' + diagnostika1
                print(diagnostika2)
                print('4----------')
                # break
        try:
            kasallik_haqida = driver.find_element(By.CLASS_NAME, 'illnes-short-description').text
            print(kasallik_haqida)
            print('1----------')
            kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(By.TAG_NAME,
                                                                                                            'ul').text
            print(kasallik_sabablari)
            print('2----------')

            asoratlari = \
                (driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul'))[
                    1].text
            print(asoratlari)
            print('3--------')
            diagnostika = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[4].text
            diagnostika1 = \
                driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[2].text
            diagnostika2 = diagnostika + '\n' + diagnostika1
            print(diagnostika2)
            print('4----------')

            # break
        except:
            try:
                kasallik_haqida = driver.find_element(By.CLASS_NAME, 'MsoNormal').text
                print(kasallik_haqida)
                print('1---------')
                kasallik_sabablari = \
                    driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                'ul')[2].text
                print(kasallik_sabablari)
                print('2---------')
                asoratlari = \
                    driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                        1].text
                print(asoratlari)
                print('3----------')
                diagnostika = \
                    driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                        4].text
                diagnostika1 = \
                    driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                        2].text
                diagnostika2 = diagnostika + '\n' + diagnostika1
                print(diagnostika2)
                print('4----------')

            except:
                try:
                    kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').text
                    print(kasallik_haqida)
                    print('1---------')
                    kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                        By.TAG_NAME,
                        'ul').text
                    print(kasallik_sabablari)
                    print('2----------')
                    asoratlari = \
                        driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                            5].text
                    print(asoratlari)
                    print('3---------')
                    diagnostika = \
                        driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'p')[
                            4].text
                    diagnostika1 = \
                        driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME, 'ul')[
                            2].text
                    diagnostika2 = diagnostika + '\n' + diagnostika1
                    print(diagnostika2)
                    print('4----------')
                except:
                    try:
                        kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                            By.CLASS_NAME, 'illnes-short-description').text
                        print(kasallik_haqida)
                        print('1---------')
                        kasallik_sabablari = driver.find_element(By.ID, 'illnes-short-description').find_element(
                            By.TAG_NAME, 'ul').text
                        print(kasallik_sabablari)
                        print('2---------')
                        asoratlari = \
                            driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                        'ul')[
                                1].text
                        print(asoratlari)
                        print('3---------')
                        diagnostika = \
                            driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                        'p')[4].text
                        diagnostika1 = \
                            driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                        'ul')[2].text
                        diagnostika2 = diagnostika + '\n' + diagnostika1
                        print(diagnostika2)
                        print('4----------')
                    except:
                        kasallik_haqida = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                            By.TAG_NAME, 'p')[0:2].text
                        print(kasallik_haqida)
                        print('1----------')
                        kasallik_sabablari = driver.find_element(By.ID, 'diseases_article_static_content').find_element(
                            By.TAG_NAME, 'ul')[3:5].text
                        print(kasallik_sabablari)
                        print('2--------')
                        kasallik_asoratlari = \
                            driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                        'ul')[
                                1].text
                        print(kasallik_asoratlari)
                        print('3-----------')
                        diagnostika = \
                            driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                        'p')[4].text
                        diagnostika1 = \
                            driver.find_element(By.ID, 'diseases_article_static_content').find_elements(By.TAG_NAME,
                                                                                                        'ul')[2].text
                        diagnostika2 = diagnostika + '\n' + diagnostika1
                        print(diagnostika2)
                        print('4----------')

driver.close()
