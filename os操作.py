#1.カレントディレクトリ内のすべての情報を取得せよ。
import os
for curDir,dird,files in os.walk("."):
    for file in files:
        print(file)

#2.カレントディレクトリ内のファイル情報を取得せよ。
lists=os.listdir(".")
print(lists)

#3.1で取得したファイルの絶対パスを出力せよ。
print(os.path.abspath("例外処理.py"))

#4.1で取得したファイルのファイル名のみを出力せよ。
print(os.path.basename("例外処理.py"))

#5.カレントディレクトリ内にxyzディレクトリが存在するか確認せよ。
#また、3で出力したファイルが存在するか確認せよ。
print(os.path.exists("xyz"))
print(os.path.exists("例外処理.py"))

#6.別の方法で、5で確認したディレクトリの存在を確認せよ。
print(os.path.isdir("xyz"))

#7.別の方法で５で確認したファイルの存在を確認せよ。
print(os.path.isfile("例外処理.py"))