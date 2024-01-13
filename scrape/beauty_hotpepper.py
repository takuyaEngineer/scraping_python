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

        # ホットペッパービューティーのリンク
        store_info["link"] = url

        # 店舗名
        store_name = soup.find("p", class_="detailTitle").a.get_text()
        store_info["store_name"] = store_name

        # 電話番号
        tel_url = soup.find(string="番号を表示").parent.attrs["href"]
        sleep(5)
        res_tel = requests.get(tel_url)
        soup_tel = BeautifulSoup(res_tel.content, "html.parser")
        tel_number = soup_tel.find("td").get_text()
        store_info["tel"] = tel_number

        # 住所
        address = soup.find("th", string="住所").parent.find("td").get_text()
        store_info["address"] = address

        # 営業時間
        business_hours = soup.find("th", string="営業時間").parent.find("td").get_text()
        store_info["business_hours"] = business_hours


        return store_info
    
    except:
        return False