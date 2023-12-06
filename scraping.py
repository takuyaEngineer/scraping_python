from bs4 import BeautifulSoup
import requests
import bs4

def get_store_info(url):

    try:
        # urlにリクエストを送る
        res = requests.get(url)
        #取得したresをパース
        soup = BeautifulSoup(res.content, "html.parser")

        store_info = {}

        # 食べログのリンク
        store_info["link"] = url

        # 店舗名
        store_name = soup.find('div', class_='rstinfo-table__name-wrap').contents[1].contents[0]
        # print(store_name)
        store_info["store_name"] = store_name

        # ジャンル
        Genre = soup.find('th', string="ジャンル", class_='').next_sibling.next_sibling.contents[1].contents[0]
        # print(Genre)
        store_info["Genre"] = Genre

        # 電話番号
        tel_arr = soup.find_all('strong', class_='rstinfo-table__tel-num')
        tel = ""
        for tel_item in tel_arr:
            if tel_item.contents[0].startswith("03-"):
                tel = tel_item.contents[0]
                break
            else:
                tel = tel_item.contents[0]
        # print(tel)
        store_info["tel"] = tel

        # 住所
        address_arr = soup.find('p', class_='rstinfo-table__address').contents
        address = ""
        for address_parts in address_arr:
            if not type(address_parts) is bs4.element.NavigableString:
                for address_parts_item in address_parts.contents:
                    if not type(address_parts_item) is bs4.element.NavigableString:
                        address += address_parts_item.contents[0]
                    else:
                        address += address_parts_item
            else:
                address += address_parts
        # print(address)
        store_info["address"] = address

        return store_info
    
    except:
        return False