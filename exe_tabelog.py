from search.index import get_link_list
from scrape.tabelog import get_store_info
from output.tabelog import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_TABELOG')

book_name = "小料理屋　エリア１"

search_words = [
    "小料理屋　大宮",
    "小料理屋　川口",
    "小料理屋　大槻",
    "小料理屋　浦和",
    "小料理屋　東大宮",
    "小料理屋　古河",
    "小料理屋　小山",
    "小料理屋　大山",
    "小料理屋　東武練馬",
]

for search_word in search_words:
    link_list = get_link_list(CSE_ID,search_word)
    print(link_list)

    if link_list:
        for link in link_list:
            store_info = get_store_info(link)
            output_spreadsheet(store_info,search_word,book_name)
            sleep(10)
