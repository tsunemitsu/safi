import requests

# 楽天アプリケーションID（Rakuten Web Serviceで取得したもの）
application_id = "1096250315764700280"  # ← ここに自分のIDを入れる

# 検索キーワード
keyword = "ノートパソコン"

# APIエンドポイント
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

# パラメータ設定
params = {
    "format": "json",
    "applicationId": application_id,
    "keyword": keyword,
    "hits": 5,  # 最大取得件数（1〜30）
    "sort": "-itemPrice"  # 高い順 / +itemPrice で安い順
}

# APIを呼び出す
response = requests.get(url, params=params)

# 結果を処理
if response.status_code == 200:
    data = response.json()
    for item in data["Items"]:
        item_info = item["Item"]
        print("商品名:", item_info["itemName"])
        print("価格:", item_info["itemPrice"], "円")
        print("商品URL:", item_info["itemUrl"])
        print("画像URL:", item_info["mediumImageUrls"][0]["imageUrl"])
        print("-" * 40)
else:
    print("APIリクエスト失敗:", response.status_code)
