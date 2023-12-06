import gspread
from gspread.exceptions import *
from oauth2client.service_account import ServiceAccountCredentials
import sys,os
from dotenv import load_dotenv

# envファイルの読み込み
load_dotenv()


def output_spreadsheet(store_info):
    
    if not store_info:
        return
    
    secret_key = os.environ.get('SECRET_KEY')
    book_name = '食べログスクレイピング'
    sheet_name = 'シート1'
    try:
        sheet = get_gspread_book(secret_key, book_name).worksheet(sheet_name)
    except SpreadsheetNotFound:
        print('Spreadsheet: ' + book_name + 'が見つかりませんでした')
        sys.exit()
    except WorksheetNotFound:
        print('Worksheet: ' + sheet_name + 'が見つかりませんでした')
        sys.exit()
    
    row = next_available_row(sheet)
    print(row)
    sheet.update_acell('A' + str(row), store_info["link"])
    sheet.update_acell('B' + str(row), store_info["store_name"])
    sheet.update_acell('C' + str(row), store_info["Genre"])
    sheet.update_acell('D' + str(row), store_info["tel"])
    sheet.update_acell('E' + str(row), store_info["address"])


def get_gspread_book(secret_key, book_name):
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(secret_key, scope)
    gc = gspread.authorize(credentials)
    book = gc.open(book_name)
    return book


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))  # fastest
    return str(len(str_list) + 1)