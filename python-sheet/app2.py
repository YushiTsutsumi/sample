import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

from gspread_dataframe import set_with_dataframe

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('planar-compass-320306-11318c65ca88.json', scope)
gs = gspread.authorize(credentials)
spread_sheet_key = '1jBpWb4iNwAdimPlmS_-FwRFjnHzIyTUCrtf1qNDQ69E'
workbook = gs.open_by_key(spread_sheet_key)
worksheet = workbook.worksheet("発注管理表")

df = pd.DataFrame(worksheet.get_all_values())
df.columns = df.iloc[0]
df = df.drop(df.index[0])
df['発注金額'] = df['発注金額'].str.replace(",", "")
df['発注金額'] = df['発注金額'].astype(int)
df_sum = df[['会社名', '発注金額']].groupby('会社名').sum()

set_with_dataframe(workbook.worksheet("会社別発注"), df_sum, include_index = True)