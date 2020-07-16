import time
from firebase import firebase
from selenium import webdriver
from just_scraping import *

db_cursor = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/', None)

db_cursor.put('/', 'Social_Studies_open_major_url', None)

for i in range(len(name_of_majors)):
    db_cursor.put('/Social_Studies_open_major_url', name_of_majors[i], url_with_text[i])

db_cursor.put('/', 'Major_and_Reqs', None)
# db_cursor.put('/Major_and_Reqs', requirements_soup.h1.text.strip(), requirements_soup.select("div.reqs"))


major_n_req = {}
for i in url_tails:
    driver.get('https://lsa.umich.edu{}'.format(i))
    requirements_soup = BeautifulSoup(driver.page_source, "html.parser")
    target = requirements_soup.select('div.reqs ul li')
    names = [n.text for n in target]
    key = ''
    value = ''
    keys = '/Major_and_Reqs/{}'.format(requirements_soup.h1.text.strip())
    db_cursor.put('/', keys, None)
    for j in range(len(names)):
        names[j] = names[j].split(':')[0]
        key = names[j].split()[0]
        value = names[j].split()[1]
        db_cursor.put(keys, key, value)




    # time.sleep(5)
