#-------------------------------------------------------------------------------
# data.go.jp から PackageListを取得する (WebAPIを利用)
#-------------------------------------------------------------------------------
# API仕様書
# http://www.data.go.jp/for-developer/for-developer/
#-------------------------------------------------------------------------------

#ライブラリ類のインポート
import requests # Apache2 Licensed HTTP library 要インストール(pip install requests)
import json     # Data Format

# URLの設定
url = "http://www.data.go.jp/data/api/action/package_list"

# APIにリクエストを送信する(実行結果・応答データがreqの中に格納される)
req = requests.get(url)

# APIからの受信データはJSON形式のためデコードする
data = json.loads(req.text)

# 受信データからキー項目を抽出する
keyList = data.keys()
sorted(keyList)

# 出力ファイルのオープン
fOutput = open("[data.go.jp]_PackageList.txt", "w")

# 送信データをそのまま出力
fOutput.write("#---- Request ----\n\n")
fOutput.write(url + "\n\n\n")

# 受信データをそのまま出力
fOutput.write("#---- Response (RawData) ----\n\n")
fOutput.write(req.text + "\n\n")

# 受信データのKey項目とそれに対応するValue項目を出力
fOutput.write("\n#---- Responce (Keys & Values) ----\n")
nLine = 0

# 配列の内容を順に出力する (パターン1)
# しかしdata.go.jpが配列の要素数を返してくれないため何件あるか不明
# 以下では仮に10番まで取り出す形にしている
#for i in range(10):
#	fOutput.write("\n" + data["result"][i])
	
# 配列の内容を順に出力する (パターン2)
# 文字列処理によって前件出力する
for key in keyList:
	nLine+=1
	fOutput.write("\n")
	fOutput.write("   No: " + str(nLine) +"\n")
	fOutput.write("  Key: " + str(key) + "\n")
	sLine = str(data[key])
	sLine = sLine.replace("[","")
	sLine = sLine.replace("]","")
	valuelist = sLine.split(', ')
	for value in valuelist:
		value = value.replace("'","")
		fOutput.write("Value: " + value + "\n")

# 出力ファイルのクローズ
fOutput.close()

#-------------------------------------------------------------------------------
