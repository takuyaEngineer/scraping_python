from googleapiclient.discovery import build
import sys,os
from dotenv import load_dotenv

# envファイルの読み込み
load_dotenv()

# Google Custom Search API KEY
API_KEY = os.environ.get('API_KEY')

def get_search_results(query, start_index, cse_id):				
    # Google Custom Search API				
    service = build("customsearch",				
                    "v1",				
                    cache_discovery=False,				
                    developerKey=API_KEY)				
    # CSEの検索結果を取得				
    result = service.cse().list(q=query,				
                                cx=cse_id,
                                num=10,
                                start=start_index).execute()				
    # 検索結果(JSON形式)				
    return result


def get_link_list(cse_id,search_word):

    # 検索結果を格納する配列
    results_arr = []

    try:
        # 10件ずつしか検索できないので、100件取得するためのインデックスの配列（1~10、11~20、、、というように10回に分けて取得する）
        # index_arr = [1,11,21,31,41,51,61,71,81,91]
        index_arr = [1,11,21]

        for index in index_arr:
            result_search = get_search_results(search_word,index,cse_id)
            if result_search:
                print("検索結果があります")
                for item in result_search["items"]:
                    results_arr.append(item["link"])
            else:
                print("検索結果がないです")
                return results_arr

        return results_arr
    except:
        return results_arr
	