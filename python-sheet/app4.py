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
worksheet = workbook.worksheet("発注管理表")

print(worksheet.acell("A1").value)

workbook.add_worksheet(title = "NEW SHEET", rows = 100, cols = 10)

new_worksheet = workbook.worksheet("NEW SHEET")

new_worksheet.update_acell('A1', worksheet.acell("A1").value)