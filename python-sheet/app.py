import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('planar-compass-320306-11318c65ca88.json', scope)

gs = gspread.authorize(credentials)

spread_sheet_key = '1jBpWb4iNwAdimPlmS_-FwRFjnHzIyTUCrtf1qNDQ69E'
workbook = gs.open_by_key(spread_sheet_key)
worksheet = workbook.worksheet("発注管理表")

print(worksheet.acell("G2").value)
print(workbook.title)
print(workbook.id)
print(worksheet)

df = pd.DataFrame(worksheet.get_all_values())
print(df.head())

df.columns = df.iloc[0]
print(df.head())

df = df.drop(df.index[0])
print(df.head())

print(df.dtypes)

df['発注金額'] = df['発注金額'].str.replace(",", "")
print(df.head())

df['発注金額'] = df['発注金額'].astype(int)

print(df.dtypes)

df_sum = df[['会社名', '発注金額']].groupby('会社名').sum()
print(df_sum.head())