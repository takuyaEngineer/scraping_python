from search.beauty_hotpepper import get_link_list
from scrape.beauty_hotpepper import get_store_info
from output.beauty_hotpepper import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_HOTPEPPER_BEAUTY')

link_list = get_link_list(CSE_ID)
print(link_list)

for link in link_list:
    store_info = get_store_info(link)
    output_spreadsheet(store_info)
    sleep(5)
