#<制御構文(if文)>
#1.if文を使って以下の処理を実行せよ。
#int型の変数であるnumを用意し、numが以下の条件の時、コロン(:)右側の文字列を出力する。
#・numが正の場合:正の値です。・numが0の場合：０です。・numが負の値の場合：負の値です。
num=3
if num==0:
    print("0です")
elif num < 0:
    print("負の値です")
else:
    print("正の値です")

    #2.以下の条件分岐に対応する実装をせよ。
    #・aは整数。・aが０以上１０未満かつ偶数：一桁の偶数です。・aが０未満かつ奇数：負の奇数です。・それ以外：整数です
    a=4
    if 0<=a<10 and a%2==0:
        print("一桁の偶数です")
    elif  a<0 and a%2!=0:
        print("負の奇数です")
    else:
        print("整数です")

#<制御構文(for文)>
#1.下記リストの要素を先頭から順に出力せよ。
names=["John","Kevin","Louis"]
for i in names:
    print(i)

#2.range関数を用いて0~9を出力せよ。
for i in range(10):
    print(i)

#3.追加でi=6の時「終了！」と出力してループを抜け出すよう実装せよ。
for i in range(10):
    if i==6:
        print("終了！")
        break 
    print(i)

#4.追加でi=3の時のみ出力結果が出ないように実装せよ。
for i in range(10):
  if i!=3:
    print(i)

#5.下記２つのリストを用意し、それぞれのリストから姓名を同時に出力せよ。
lasts=["岡本","佐藤","田中"]
firsts=["明","拓哉","太郎"]
for a,b in zip(lasts,firsts):
    print(a+b)