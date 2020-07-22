
dic_majors_and_link = {}
for i in range(len(name_of_majors)):
    dic_majors_and_link[name_of_majors[i]] = url_with_text[i]





//*[@id="anthropology-maj"]/td[1]/a
//*[@id="communication_studies-maj"]/td[1]/a




print(new_soup.prettify())








def get_preview_url(title, artist):
    name = "+".join("{} {}".format(title, artist).split())
    r = requests.get("https://itunes.apple.com/search?term={}&entity=song&limit=1".format(name))
    json = r.json()
    if not json['resultCount']:
        return {"error": "Song not found"}
    else:
        return {
            "artist": artist,
            "title": title,
            "url": json['results'][0]['previewUrl']
        }





# <!-----------------scrapcode-------------------------------------------->


all_majors = soup.find("table", {"id": "lsa-programs-list"})

just_hash_links = all_majors.find_all('a').get('href')

just_hash_links = list()


for a in all_majors:
    just_hash_links.append(all_majors[a].find('a').get('href'))





for i in dic_majors_and_link.keys():
    print(i, ' ', dic_majors_and_link[i], "\n")









lsa_website = 'https://lsa.umich.edu/lsa/academics/majors-minors'
req = requests.get(lsa_website)
soup = BeautifulSoup(req.text, "html.parser")

print(soup.prettify)

print(soup.find_all('table'))








<!-------plugin lists onto the excel sheet---------->

# j = 0
# for i in range(2, (2 + len(anthro_major))):
#     sheet.update_cell(1, i, anthro_major[j])
#     j = j + 1

econ = ['ECON 401', 'ECON 402', 'STATS 250',
        'STATS 280', 'STATS 426', 'ECON 451',
        'ECON 453', 'ECON 251', 'ECON 452', 'ECON 454']

comm = ['COMM ' + str(i) for i in range(200, 500)]

his = ['HISTORY 202', 'HISTORY 497', 'HISTORY 496', 'HISTORY 499']

lin = ['LING 313', 'LING 315', 'LING 316', 'LING 497']

men = ['MENAS 493', 'HISTORY 443', 'POLSCI 351', 'POLSCI 352', 'POLSCI 353']

list_of_lists = [anthro_major, econ, comm, his, lin, men]


j = 0
k = 1
for major in list_of_lists:
    j = 0
    for i in range(2, (2 + len(major))):
        sheet.update_cell(k, i, major[j])
        j = j + 1
    k = k + 1







<!----------importing directly from the website to the database>


import time
from firebase import firebase
from selenium import webdriver
from just_scraping import *

db_cursor = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/', None)

db_cursor.put('/', 'open_major_url', None)

for i in range(len(name_of_majors)):
    db_cursor.put('/open_major_url', name_of_majors[i].replace('[', '(').replace(']', ')').replace('.', '').replace('/', '_'), url_with_text[i])
    if name_of_majors[i] == 'Biochemistry [B.S.] (Major)':
        db_cursor.put('/open_major_url', 'Biochemistry (B.S.) (Major)', url_with_text[i])
    else:
        db_cursor.put('/open_major_url', name_of_majors[i], url_with_text[i])

db_cursor.put('/', 'Major_and_Reqs', None)


for i in range(len(url_tails)):
    driver.get('https://lsa.umich.edu{}'.format(url_tails[i]))      # visits page of major
    requirements_soup = BeautifulSoup(driver.page_source, "html.parser")  #creates new soup
    target = requirements_soup.select('div.current-program-requirements div.reqs ul li')  #Only looks for the classes (ideally, this is broken)
    names = [n.text for n in target]  #strips the text from the li tags
    major = requirements_soup.h1.text.strip().replace('[', '(').replace(']', ')').replace('.', '').replace('/', '_')
    major_checker = '/Major_and_Reqs/{}'.format(major)  #updates according to the new major
    # print(major)
    if not names or major == 'History Major':
        db_cursor.post(major_checker, 'do manually')
        continue
    for j in range(len(names)):
        #splits the li element into the class number and the description
        if major == 'Economics Major':
            names[j] = names[j].split(',')[0]
        else:
            names[j] = names[j].split(':')[0]
        db_cursor.post(major_checker, names[j])
    time.sleep(5)
