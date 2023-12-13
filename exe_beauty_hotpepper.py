from search.beauty_hotpepper import get_link_list
from scrape.beauty_hotpepper import get_store_info
from output.beauty_hotpepper import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_HOTPEPPER_BEAUTY')

search_words = [
    "ヘアサロン　大宮",
    "ヘアサロン　川口",
    "ヘアサロン　大槻",
    "ヘアサロン　浦和",
    "ヘアサロン　東大宮",
    "ヘアサロン　古河",
    "ヘアサロン　小山",
    "ヘアサロン　大山　東武練馬",
    "ヘアサロン　成増　和光市",
    "ヘアサロン　志木",
]

for search_word in search_words:
    link_list = get_link_list(CSE_ID,search_word)
    print(link_list)

    for link in link_list:
        store_info = get_store_info(link)
        output_spreadsheet(store_info,search_word)
        sleep(10)
