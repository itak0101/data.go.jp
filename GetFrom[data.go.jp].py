#-------------------------------------------------------------------------------
# オープンデータカタログサイト data.go.jp からデータを取得する
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
fOutput.writelines("# keys\n")

nLine = 0
for key in keyList:
	nLine+=1
	fOutput.write(str(nLine) + ": " + key + "\n")
	
fOutput.write("\n# Values\n")
nLine = 0
for key in keyList:
	nLine+=1
	fOutput.write(str(nLine) + ": " + key +"\n\t"+ str(data[key]) + "\n")
	if str(data[key]) == "result":
		for value in str(data[key]):
			fOutput.write("\n\t"+ str(value) + "\n")

fOutput.close()


#print("Result: ", req.text)
#fOutput.writelines("Result: ", req.text)
#
#package_list
#for key in keyList:
#	with open("..\keys.txt", mode='a') as f1:
#		f1.write(key)
#    
#fOutput = open("..\output.txt", "w")
#json.dump(data, fOutput)


#print('json_dict:{}'.format(type(data)))
#print("Result: ", req.text)
#-------------------------------------------------------------------------------