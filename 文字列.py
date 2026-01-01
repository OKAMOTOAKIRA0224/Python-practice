#<文字列>
#1.以下の文章の「〇〇」に対して、format()とf-stringsを使って文字列を代入。
#「私は〇〇です。〇〇出身です。」
a="岡本明"
b="鳥取県"
print(f"私は{a}です。{b}出身です。")

#2.次の文字列を句読点で改行しましょう。
#「いつもの帰り道とは違うルートで帰ってみようかな。迷子にならないか心配だけど。」
print("いつもの帰り道とは違うルートで帰ってみようかな。\n迷子にならないか心配だけど。")

#3.16.0という値を符号つ付き10進数、符号付き16進数、10進浮動小数点の書式で表示せよ。
print("10進数=%d.16進数=%x.10進浮動小数点=%f" % (16,16,16))

#4.以下の文字列に対して小文字から大文字、大文字から小文字に変換せよ。
#good GOOD
print("good".upper())
print("GOOD".lower())

#5.下記の文字列を改行部分で分割し、リストに格納せよ。
#「こんにちは。\n私は岡本明です。」
a="こんにちは。\n私は岡本明です。"
print(a.split("\n"))

#6.以下のリストに入っている文字列を結合して１つの文にせよ。
#['こんにちは。', '私は岡本明です。']
a=['こんにちは。', '私は岡本明です。']
print("".join(a))

#7.下記の文のはじめと最後にある空白を除去せよ
#「 いつも食べるここのケーキはおししいね。 」
x=" いつも食べるここのケーキはおししいね。 "
print(x.strip())

#8.以下の文の晴れを雨に置換してください。
#「今日は晴れですね」
x="今日は晴れですね"
print(x.replace("晴れ","雨"))

#9.以下のフレーズの中から「夜空」を検索し、その位置を出力せよ。
#「今日はとても夜空がきれい。」
x="今日はとても夜空がきれい。"
print(x.find("夜空"))

#10.以下のデータ型を文字列型に変換せよ。
#int:x=1,float:x=1.52,list:x=[1,2,3],dict:x=dict(name="john",birth="US")
a=1
b=1.52
c=[1,2,3]
d=dict(name="john",birth="US")
a=str(a)
b=str(b)
c=str(c)
d=str(d)

#11.以下の文字列Aが文字列Bに含まれているか調べよ。
#A:"sba",B"gasba"
print(a in b)

#<リスト>
#10.次のリストの中から、先頭から２つ目の値と最後の値をそれぞれ出力せよ。また２をリストの一番最後に追加せよ
#numbers=[0,3,8,-4,9,1]
numbers=[0,3,8,-4,9,1]
print(numbers[1])
print(numbers[-1])
numbers.append(2)

#11.問題10のnumbersリストの先頭に5を挿入せよ。また最後から１つ手前に-3を挿入せよ。
numbers=[0,3,8,-4,9,1]
numbers.insert(0,5)
numbers.insert(-1,-3)
print(numbers)

#12.リストから１つ目の５と最後から３番目の要素を削除せよ。
numbers=[5,0,3,8,-4,9,1,5,2]
numbers.remove(5)
numbers.pop(-3)
print(numbers)

#13.次の偶数のみを返す関数とfilter()を用いてnumbersリストから偶数のみを取り出したリストを作成せよ。
def isEven(number):
    if number%2==0:
        print(f"This number,{number} is even!")
        return True
    else:
        print(f"This number,{number} is odd!")
        return False
numbers=[5,0,3,8,-4,9,1,5,2]
print(list(filter(isEven,numbers)))

#14.numbersリストの中から要素が-4のインデックスを取得せよ。
numbers=[5,0,3,8,-4,9,1,5,2]
print(numbers.index(-4))

#15.numbersリストの順序を昇順/降順にそれぞれ並び替えよ。
numbers=[5,0,3,8,-4,9,1,5,2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)