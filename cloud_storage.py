import gspread
from oauth2client.service_account import ServiceAccountCredentials
from firebase import firebase

db = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/')


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


sheet = client.open("Majors - Requirements").sheet1

majors = sheet.col_values(1)

for major in range(1, (1 + len(majors))):
    classes = sheet.row_values(major)
    i = major - 1
    path = '/Major_and_Reqs/{}'.format(majors[i])
    for i in range(1, len(classes)):
        db.post(path, classes[i])

sheet = client.close()
