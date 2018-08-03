#-------------------------------------------------------------------------------
# data.go.jp から PackageListを取得する (WebAPI)を利用
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
fOutput = open("..\[data.go.jp]package_list.txt", "w")

# 受信データをそのまま出力
fOutput.write("#---- Request ----\n\n")
fOutput.write(url + "\n\n\n")

# 受信データをそのまま出力
fOutput.write("#---- Response (RowData) ----\n\n")
fOutput.write(req.text + "\n\n")

# 受信データのKey項目とそれに対応するValue項目を出力
fOutput.write("\n#---- Responce (Keys & Values) ----\n")
nLine = 0
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
