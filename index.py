from search import get_link_list
from scraping import get_store_info
from output import output_spreadsheet
from time import sleep

link_list = get_link_list()

for link in link_list:
    store_info = get_store_info(link)
    output_spreadsheet(store_info)
    sleep(2)
