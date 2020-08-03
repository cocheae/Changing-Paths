import time
from firebase import firebase
from selenium import webdriver
from just_scraping import *

db_cursor = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/', None)

# db_cursor.put('/', 'open_major_url', None)

# for i in range(len(name_of_majors)):
#     db_cursor.put('/open_major_url', name_of_majors[i].replace('[', '(').replace(']', ')').replace('.', '').replace('/', '_'), url_with_text[i])
#     if name_of_majors[i] == 'Biochemistry [B.S.] (Major)':
#         db_cursor.put('/open_major_url', 'Biochemistry (B.S.) (Major)', url_with_text[i])
#     else:
#         db_cursor.put('/open_major_url', name_of_majors[i], url_with_text[i])
#
# for i in range(len(url_tails)):
#     driver.get('https://lsa.umich.edu{}'.format(url_tails[i]))      # visits page of major
#     requirements_soup = BeautifulSoup(driver.page_source, "html.parser")  #creates new soup
#     target = requirements_soup.select('div.current-program-requirements div.reqs ul li')  #Only looks for the classes (ideally, this is broken)
#     names = [n.text for n in target]  #strips the text from the li tags
#     major = requirements_soup.h1.text.strip().replace('[', '(').replace(']', ')').replace('.', '').replace('/', '_')
#     major_checker = '/scrap/{}'.format(major)  #updates according to the new major
#     # print(major)
#     if not names or major == 'History Major':
#         db_cursor.post(major_checker, 'do manually')
#         continue
#     for j in range(len(names)):
#         #splits the li element into the class number and the description
#         if major == 'Economics Major':
#             names[j] = names[j].split(',')[0]
#         else:
#             names[j] = names[j].split(':')[0]
#         db_cursor.post(major_checker, names[j])
#     time.sleep(5)
