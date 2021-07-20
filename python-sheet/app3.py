import gspread
import json
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('planar-compass-320306-11318c65ca88.json', scope)
gs = gspread.authorize(credentials)
spread_sheet_key = '1jBpWb4iNwAdimPlmS_-FwRFjnHzIyTUCrtf1qNDQ69E'
workbook = gs.open_by_key(spread_sheet_key)
worksheet = workbook.worksheet("トライアル")

worksheet.update_acell('A1', 'Hello')

i = 0
for i in range(10):
    i += 1
    cell = 'A' + str(i)
    worksheet.update_acell(cell, i)

worksheet.update_acell('B1', worksheet.acell("A1").value)