"""
this is a selenium bot to take MBTI test
from : https://esanj.ir/tag/psychology-test
for persian users (it's based on persian language)
                   
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


google_url='https://www.google.com/'
driver=webdriver.Chrome()
driver.get(google_url)

# enter your personal information
personal_info={'gender':'male',
               'birthdat':'1378'}


search_info={'google_search':'تست روانشناسی',
             'site_main_XPATH':'//*[@id="rso"]/div/div[1]/div/div/div[1]/a',
             'test_selector':'#first-test > div > div.col-lg-9.col-md-9.col-sm-9 > h3 > a',
             'start_test_1_XPATH':'/html/body/section[2]/div/div[3]/div[2]/a[1]',
             'gender_XPATH':'//*[@id="sex"]',
             'birthday_XPATH':'//*[@id="year_birth"]',
             'start_test_2_XPATH':'/html/body/section[2]/div/div/div/div/div[1]/div/form/button',
             'question_XPATH':'/html/body/div/div/div[3]/p',
             'answer_1_XPATH':'/html/body/div/div/div[3]/div/div[1]/label',
             'answer_2_XPATH':'/html/body/div/div/div[3]/div/div[2]/label',
             'end_test_XPATH':'/html/body/div/div/div[4]/button[4]',
             'result_XPATH':'/html/body/div/div/div[4]/button[3]',
             'exit_1_XPATH':'//*[@id="BoxSaveToProfile"]/div/div/div[1]/button',
             'showing_result_1':'//*[@id="sec_3"]/div/div'}



search_keys=list(search_info.keys())
search_values=list(search_info.values())

personal_keys=list(personal_info.keys())
personal_values=list(personal_info.values())


# define a webdriver wait to use explicit wait in next steps
defined_wait=WebDriverWait(driver, 15)
google_search_box=defined_wait.until(EC.element_to_be_clickable((By.NAME, 'q')))

# search for psychological testing
google_search_box.send_keys(search_values[search_keys.index('google_search')]+Keys.ENTER)
click_on_site=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             search_values[search_keys.index('site_main_XPATH')]))).click()

# select MBTI test
MBTI_test=defined_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                         search_values[search_keys.index('test_selector')]))).click()
start_test_1=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            search_values[search_keys.index('start_test_1_XPATH')]))).click()

#fill the gender and birthday box
gender_box=defined_wait.until(EC.element_to_be_clickable((By.XPATH, search_values[search_keys.index('gender_XPATH')])))
drop_gender=Select(gender_box)
drop_gender.select_by_value(personal_values[personal_keys.index('gender')])
birthday_box=defined_wait.until(EC.element_to_be_clickable((By.XPATH, search_values[search_keys.index('birthday_XPATH')])))
drop_birthday=Select(birthday_box)
drop_birthday.select_by_value(personal_values[personal_keys.index('birthdat')])

start_test_2=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            search_values[search_keys.index('start_test_2_XPATH')]))).click()

# complete 87 questions
for number in range(1, 88):
    question_text=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                search_values[search_keys.index('question_XPATH')])))    
    answer_1=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            search_values[search_keys.index('answer_1_XPATH')])))
    answer_2=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            search_values[search_keys.index('answer_2_XPATH')])))
    print(question_text.text)
    print('1-'+answer_1.text)
    print('2-'+answer_2.text)
    
    answer=input('پاسخ ؟')
    
    if int(answer)==1:
        answer_1.click()
    elif int(answer)==2:
        answer_2.click()
    else:
        print('پاسخ صحیح نیست')

    
ending_test=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           search_values[search_keys.index('end_test_XPATH')]))).click()
result=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                      search_values[search_keys.index('result_XPATH')]))).click()
exit_1=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                      search_values[search_keys.index('exit_1_XPATH')]))).click()
info=defined_wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     search_values[search_keys.index('showing_result')])))

# print a part of results
print(info.text)