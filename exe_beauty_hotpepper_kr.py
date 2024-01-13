from search.index import get_link_list
from scrape.beauty_hotpepper import get_store_info
from output.beauty_hotpepper import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_HOTPEPPER_BEAUTY_KR')

book_name = "ネイルサロン　エリア１"

search_words = [
    "ネイルサロン　大宮",
    "ネイルサロン　川口",
    "ネイルサロン　大槻",
    "ネイルサロン　浦和",
    "ネイルサロン　東大宮",
    "ネイルサロン　古河",
    "ネイルサロン　小山",
    "ネイルサロン　大山",
    "ネイルサロン　東武練馬",
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
        print("exceptionです")
