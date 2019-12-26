# Data Wrangling
import pandas as pd
# Google Sheets API
import os
import pickle
from gspread_pandas import Spread
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Gsheet Parameters
spread_name = "trackingcodemonitoring"
sheet_name = "base"

SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/spreadsheets']

# Building Credentials
credentials = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        credentials = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(credentials, token)

spread = Spread(spread=spread_name,
                sheet=sheet_name,
                scope=SCOPES,
                creds=credentials)

# Reading Spreadsheet into Pandas DataFrame
df = spread.sheet_to_df(index=0)
print(isinstance(df, pd.DataFrame))

# Writing Pandas DataFrame into Google Spreadsheet
spread.df_to_sheet(df, index=False, sheet=sheet_name, start='A1', replace=True)
