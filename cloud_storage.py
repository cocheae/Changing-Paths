import time
from firebase import firebase
from selenium import webdriver
from just_scraping import *

db_cursor = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/', None)

db_cursor.put('/', 'Social_Studies_open_major_url', None)

for i in range(len(name_of_majors)):
    db_cursor.put('/Social_Studies_open_major_url', name_of_majors[i], url_with_text[i])

db_cursor.put('/', 'Major_and_Reqs', None)


# major_n_req = {}
for i in url_tails:
    driver.get('https://lsa.umich.edu{}'.format(i))      # visits page of major
    requirements_soup = BeautifulSoup(driver.page_source, "html.parser")  #creates new soup
    target = requirements_soup.select('div.reqs ul li')  #Only looks for the classes (ideally, this is broken)
    names = [n.text for n in target]  #strips the text from the li tags
    key = ''
    value = ''

    keys = '/Major_and_Reqs/{}'.format(requirements_soup.h1.text.strip())  #updates according to the new major
    db_cursor.put('/', keys, None)  #creates new level for each major
    #logs into the database the classes required for the major
    for j in range(len(names)):
        #splits the li element into the class number and the description
        names[j] = names[j].split(':')[0]
        #splits the class again into subject and number
        key = names[j].split()[0]
        value = names[j].split()[1]
        db_cursor.put(keys, key, value)




    # time.sleep(5)
