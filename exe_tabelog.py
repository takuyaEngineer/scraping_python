from search.index import get_link_list
from scrape.tabelog import get_store_info
from output.tabelog import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_TABELOG')

book_name = "小料理屋　エリア１１"

search_words = [
    "小料理屋　宇都宮",
    "小料理屋　鹿沼",
    "小料理屋　栃木",
    "小料理屋　佐野",
    "小料理屋　鬼怒川",
    "小料理屋　日光",
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