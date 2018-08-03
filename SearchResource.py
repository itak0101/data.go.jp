#-------------------------------------------------------------------------------
# data.go.jp の リソースを検索する (WebAPIを利用)
#-------------------------------------------------------------------------------
# API仕様書
# http://www.data.go.jp/for-developer/for-developer/
#-------------------------------------------------------------------------------

#ライブラリ類のインポート
import requests # Apache2 Licensed HTTP library 要インストール(pip install requests)
import json     # Data Format

# ユーザー設定値
SearchWord = "統計" #検索文字列
SearchCount = "20"  #検索件数

# APIの設定
api = "http://www.data.go.jp/data/api/action/resource_search?query={query}&limit={limit}"
url = api.format(query="name:" + SearchWord, limit=SearchCount)
print (url)

# APIにリクエストを送信する(実行結果・応答データがreqの中に格納される)
req = requests.get(url)

# APIからの受信データはJSON形式のためデコードする
data = json.loads(req.text)

## 出力ファイルのオープン
fOutput = open("[data.go.jp]_SearchResource.txt", "w")

# 受信データをそのまま出力
fOutput.write("#---- Request ----\n\n")
fOutput.write(url + "\n\n\n")

# 受信データをそのまま出力
fOutput.write("#---- Response (RawData) ----\n\n")
fOutput.write(req.text + "\n\n")

## 受信データのKey項目とそれに対応するValue項目を出力
fOutput.write("\n#---- Responce (Keys & Values) ----\n")
nLine = 0
for key in data.keys():
	nLine+=1
	fOutput.write("\n")
	fOutput.write("   No: " + str(nLine) +"\n")
	fOutput.write("  Key: " + str(key) + "\n")
	fOutput.write("Value: " + str(data[key]) + "\n")
	if str(key) == "result":
		count = str(data["result"]["count"])
		for i in range(int(SearchCount)):
			fOutput.write("result:results:name: " + str(data["result"]["results"][int(i)]["name"]) + "\n")

# 出力ファイルのクローズ
fOutput.close()

#デバッグ用
#print(str(data["result"]["count"]))
#print(str(data["result"]["results"][0]["name"]))

#-------------------------------------------------------------------------------
