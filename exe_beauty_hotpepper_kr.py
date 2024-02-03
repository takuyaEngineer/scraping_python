from search.index import get_link_list
from scrape.beauty_hotpepper import get_store_info
from output.beauty_hotpepper import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_HOTPEPPER_BEAUTY_KR')

book_name = "ヘッドスパ　エリア２"

search_words = [
    "ヘッドスパ　成増",
    "ヘッドスパ　和光市",
    "ヘッドスパ　志木",
    "ヘッドスパ　鶴瀬",
    "ヘッドスパ　上福岡",
    "ヘッドスパ　川越",
    "ヘッドスパ　鶴ヶ島",
    "ヘッドスパ　若葉",
    "ヘッドスパ　坂戸",
]

for search_word in search_words:

    try:
        link_list = get_link_list(CSE_ID,search_word)
        print(link_list)
        
        if link_list:
            for link in link_list:
                store_info = get_store_info(link)
                output_spreadsheet(store_info,search_word,book_name)
                sleep(10)

    except:
        print("exeでエクセプションです")
