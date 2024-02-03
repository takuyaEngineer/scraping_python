from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from listData.list_data_area11 import list_Eating_and_drinking as list_data

# このアプリがどこまでの権限を持つか
SCOPES = ["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive.readonly",
          "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/spreadsheets.readonly"]

def create(genre):

  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  
  sheets = []
  values = []

  for value in genre["values"]:
    values.append(
      {
        "userEnteredValue": {
          "stringValue": value,
        }
      },
    )

  for sheet in genre["sheets"]:
    sheets.append(
      {
        "properties": {
          "title": sheet,
        },
        "data": [
          {
              "startRow": 0,
              "startColumn": 0,
              "rowData": [
                {
                  "values": values
                }
              ],
          }
        ]
      }
    )

  try:
    service = build("sheets", "v4", credentials=creds)
    spreadsheet = {
      "properties": {"title": genre["spreadsheet_name"]},
      "sheets": sheets
    }
    spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet, fields="spreadsheetId")
        .execute()
    )
    print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
    return spreadsheet.get("spreadsheetId")
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error


if __name__ == "__main__":
  for genre in list_data:
    create(genre)