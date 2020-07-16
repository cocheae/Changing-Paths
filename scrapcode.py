
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
