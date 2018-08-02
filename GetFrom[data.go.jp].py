#-------------------------------------------------------------------------------
# data.go.jp からデータを取得する
#-------------------------------------------------------------------------------

#ライブラリ類のインポート
import requests # Apache2 Licensed HTTP library 要インストール(pip install requests)
import json     # Data Format

# APIキーの指定
apikey = "http://www.data.go.jp/data/api/action/package_list"
url = apikey

# APIにリクエストを送信する(実行結果・応答データがreqの中に格納される)
req = requests.get(url)

# APIからの受信データはJSON形式なのでデコードする
data = json.loads(req.text)

# 受信データからキー項目を取得する
keyList = data.keys()
sorted(keyList)

# 受信データを出力する
fOutput = open("..\[data.go.jp]package_list.txt", "w")

# 受信データをそのまま出力
fOutput.write("# RowData\n")
fOutput.write(req.text + "\n\n")

# 受信データのKey項目のみ出力
fOutput.write("# keys\n")
nLine = 0
for key in keyList:
	nLine+=1
	fOutput.write(str(nLine) + ": " + key + "\n")

# 受信データのKey項目と対応するValue項目を出力
fOutput.write("\n# Keys & Values\n")
nLine = 0
for key in keyList:
	nLine+=1
	fOutput.write(str(nLine) + ": " + key +"\n\t"+ str(data[key]) + "\n")
	if key == "result":
		s = str(data[key])
		s = s.replace("[","")
		s = s.replace("]","")
		l = s.split(', ')
		for ll in l:
			ll = ll.replace("'","")
			fOutput.write("\t" + ll + "\n")

fOutput.close()

#-------------------------------------------------------------------------------