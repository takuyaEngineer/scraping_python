from search.tabelog import get_link_list
from scrape.tabelog import get_store_info
from output.tabelog import output_spreadsheet
from time import sleep
import os

CSE_ID = os.environ.get('CSE_ID_TABELOG')

link_list = get_link_list(CSE_ID)

for link in link_list:
    store_info = get_store_info(link)
    output_spreadsheet(store_info)
    sleep(5)
