#1.10をnumで割ったときの結果を出力せよ
#0で割った(割れない)場合に「エラー」と出力せよ
num=0
try:
    x=10/num
    print(f"結果:{x}")
except:
  print("エラー")

#2.10をある数字numで割ったときの結果を出力せよ
#エラーがZeroDivitionErrorだった場合に、エラー内容を出力せよ
num=0
try:
    x=10/num
    print(f"結果:{x}")
except ZeroDivisionError as e:
  print(e)

#3.次のdivide()関数ではa,bがそれぞれ数値の場合に正常に数値計算が行われている
#a or bが文字列の場合(数値型とは異なる場合)の例外処理(TypeError)をexceptを追加して実装せよ
def divide(a,b):
   try:
      print(f"結果:{a/b}")
   except ZeroDivisionError as e:
      print(e)
   except TypeError as g:
      print(g)
   else :
      print("正常に終了しました")
print(divide(1,"a"))

#4.上のdivide()関数で例外処理の発生の有無に限らず「すべての処理が終了しました」と表示せよ
def divide(a,b):
   try:
      print(f"結果:{a/b}")
   except ZeroDivisionError as e:
      print(e)
   except TypeError as g:
      print(g)
   finally :
      print("全ての処理が終了しました")
print(divide(1,"a"))

#5.上の関数でTypeErrorの例外処理が発生した場合、何も処理を行わずスルーせよ
def divide(a,b):
   try:
      print(f"結果:{a/b}")
   except ZeroDivisionError as e:
      print(e)
   except TypeError as g:
      pass
   finally:
      print("全ての処理が終了しました")
print(divide(1,"a"))


      
      