from bs4 import BeautifulSoup
import requests
from time import sleep

def get_store_info(url):

    try:
        # urlにリクエストを送る
        res = requests.get(url)
        #取得したresをパース
        soup = BeautifulSoup(res.content, "html.parser")

        store_info = {}

        # ポケパラのリンク
        # store_info["link"] = url

        # 店舗名
        # store_name = soup.find("div", class_="shop_header_top").h2.a.get_text()
        # store_info["store_name"] = store_name



        # 電話番号
        tel = soup.find("th",string="電話番号").parent.next_sibling
        print(tel)
        store_info["tel"] = tel

        # # 住所
        # address = soup.find("th", string="住所").parent.find("td").get_text()
        # store_info["address"] = address

        # # 営業時間
        # business_hours = soup.find("th", string="営業時間").parent.find("td").get_text()
        # store_info["business_hours"] = business_hours


        return store_info
    
    except:
        return []

# get_store_info("https://www.pokepara.jp/saitama/m80/a10700/shop17717/")
# https://www.pokepara.jp/saitama/m80/a10700/shop17717/