from search.pokepara import get_link_list
from scrape.pokepara import get_store_info
from output.pokepara import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_POKEPARA')

search_words = [
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
