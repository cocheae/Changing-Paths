# import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome(executable_path='/Users/erickcochea/Desktop/Changing-Paths/chromedriver-2')
driver.get('https://lsa.umich.edu/lsa/academics/majors-minors.html')

# This so that the filters are applied
x_path_soc = '//*[@id="gridparlsa_gridwrapper_gridclass"]/section/section/div/div/div[2]/div/div[1]/ul[1]/li[3]/button'
btn_soc = driver.find_element_by_xpath(x_path_soc)
btn_soc.click()

x_path_major = '//*[@id="gridparlsa_gridwrapper_gridclass"]/section/section/div/div/div[2]/div/div[1]/ul[2]/li[1]/button'
btn_major = driver.find_element_by_xpath(x_path_major)
btn_major.click()

# x_path_open_major = "//*[@id=\"anthropology-maj\"]/td[1]/a"
# open_btn_major = driver.find_element_by_xpath(x_path_open_major)
# open_btn_major.click()


time.sleep(5)  # It needs to wait so that the html file updates

# This looks for the majors-and-minors table
soup = BeautifulSoup(driver.page_source, "html.parser").table

# This looks for all the href values and stores them in a list
name_of_majors = []
for i in soup.find_all('a'):
    name_of_majors.append(i.text)

links_with_text = []
for a in soup.find_all('a', href=True):
    if a.text:
        links_with_text.append(a['href'])



dic_majors_and_link = {}


for i in range(len(name_of_majors)):
    dic_majors_and_link[name_of_majors[i]] = links_with_text[i]




# close browser
driver.close()










# <!-----------------scrapcode-------------------------------------------->


# all_majors = soup.find("table", {"id": "lsa-programs-list"})

# just_hash_links = all_majors.find_all('a').get('href')
#
# just_hash_links = list()
#
#
# for a in all_majors:
#     just_hash_links.append(all_majors[a].find('a').get('href'))
#
#



# for i in dic_majors_and_link.keys():
#     print(i, ' ', dic_majors_and_link[i], "\n")
#








# lsa_website = 'https://lsa.umich.edu/lsa/academics/majors-minors'
# req = requests.get(lsa_website)
# soup = BeautifulSoup(req.text, "html.parser")
#
# # print(soup.prettify)
#
# print(soup.find_all('table'))
