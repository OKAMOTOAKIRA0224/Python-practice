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

#8.パス名の出力をos.path.join()で結合せよ
for curDir,dird,files in os.walk("."):
    for file in files:
        print(os.path.join(curDir,file))

#8.カレントディレクトリにakiraディレクトリを作成せよ。
#o.mkdir("akira")
#カレントディレクトリにあるsample.txtを削除せよ。
#os.remove("sample.txt")

#9.カレントディレクトリにあるakiraフォルダの名前を自分の名前に変更せよ。
#os.rename("akira","岡本明")

#10.環境変数であるPATHの確認せよ。
os.environ["PATH"]

#11.os.system()でUnixコマンドを使ってみましょう
print(os.popen('ls -a').read())