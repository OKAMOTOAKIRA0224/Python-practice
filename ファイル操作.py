#1.下記テキストファイルをよういし、テキストファイルからテキストデータを取得して出力せよ
#sample.txt
#はじめまして、こちらは岡本明です。
file = open('sample.txt',encoding="utf-8")
text=file.read()
print(text)
file.close()

#2.先ほどのテキストデータを取得する処理with構文を使って実装せよ。
with open("sample.txt","r",encoding="utf-8") as f:
    txt=f.read()
print(txt)

#3.jsonモジュールを使ってjsonファイルを読み込みましょう。
import json
with open("sample.json","r",encoding="utf-8") as f:
    data=json.load(f)
print(data["store_name"])

