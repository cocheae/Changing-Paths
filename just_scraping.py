# # import requests
# import time
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
#
#
# driver = webdriver.Chrome(executable_path='/Users/erickcochea/Desktop/Changing-Paths/chromedriver-2')
# driver.get('https://lsa.umich.edu/lsa/academics/majors-minors.html')
#
# # This so that the filters are applied
# x_path_soc = '//*[@id="gridparlsa_gridwrapper_gridclass"]/section/section/div/div/div[2]/div/div[1]/ul[1]/li[3]/button'
# btn_soc = driver.find_element_by_xpath(x_path_soc)
# btn_soc.click()
#
# x_path_major = '//*[@id="gridparlsa_gridwrapper_gridclass"]/section/section/div/div/div[2]/div/div[1]/ul[2]/li[1]/button'
# btn_major = driver.find_element_by_xpath(x_path_major)
# btn_major.click()
#
# # x_path_open_major = "//*[@id=\"anthropology-maj\"]/td[1]/a"
# # open_btn_major = driver.find_element_by_xpath(x_path_open_major)
# # open_btn_major.click()
#
#
# time.sleep(5)  # It needs to wait so that the html file updates
#
# # This looks for the majors-and-minors table
# soup = BeautifulSoup(driver.page_source, "html.parser").table
#
# # # close browser
# # driver.close()
#
# # This looks for all the href values and stores them in a list
# name_of_majors = []
# for i in soup.find_all('a'):
#     name_of_majors.append(i.text)
#
# # the url to "open the major"
# url_with_text = []
# for a in soup.find_all('a', href=True):
#     if a.text:
#         url_with_text.append(a['href'])
#
#
# # url_of_major for button
# on_click_buttons = []
# for i in url_with_text:
#     on_click_buttons.append(i.split('#')[1])
#
# # pressing all major tabs
# for i in on_click_buttons:
#     x_path_majors = "//*[@id=\"{}\"]/td[1]/a".format(i)
#     open_major_btn = driver.find_element_by_xpath(x_path_majors)
#     open_major_btn.click()
#
# time.sleep(5)
#
# new_soup = BeautifulSoup(driver.page_source, "html.parser")
#
# url_tails = []
# for a in new_soup.find_all('a', href=True, text='REQUIREMENTS'):
#     url_tails.append(a['href'])
