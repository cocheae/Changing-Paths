import gspread
from oauth2client.service_account import ServiceAccountCredentials
from firebase import firebase
from just_scraping import url_tails

db = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/')


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


sheet = client.open("Majors - Requirements").worksheet("Sheet3")

# majors = sheet.col_values(1)
#
# for major in range(1, (1 + len(majors))):
#     classes = sheet.row_values(major)
#     i = major - 1
#     path = '/Major_and_Reqs/{}'.format(majors[i])
#     for i in range(1, len(classes)):
#         db.post(path, classes[i])

# links = [*db.get('/open_major_url', None).values()]

j = 0
for i in range(2, 2 + len(url_tails)):
    sheet.update_cell(i, 2, 'https://lsa.umich.edu{}'.format(url_tails[j]))
    j += 1
