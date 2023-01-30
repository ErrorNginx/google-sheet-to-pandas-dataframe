import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# authenticate with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 
        'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']
creds = ServiceAccountCredentials.from_json_keyfile_name('file.json', scope)
client = gspread.authorize(creds)

# open Google Sheet
sheet = client.open('sheet_test').sheet1

# convert Google Sheet data into Pandas DataFrame
df = pd.DataFrame(sheet.get_all_values())

print(df)

df.to_csv('output/file_name.csv',sep='\t', header=False )