#<リスト>
#1.次のリストの中から、先頭から２つ目の値と最後の値をそれぞれ出力せよ。また２をリストの一番最後に追加せよ
#numbers=[0,3,8,-4,9,1]
numbers=[0,3,8,-4,9,1]
print(numbers[1])
print(numbers[-1])
numbers.append(2)

#2.問題10のnumbersリストの先頭に5を挿入せよ。また最後から１つ手前に-3を挿入せよ。
numbers=[0,3,8,-4,9,1]
numbers.insert(0,5)
numbers.insert(-1,-3)
print(numbers)

#3.リストから１つ目の５と最後から３番目の要素を削除せよ。
numbers=[5,0,3,8,-4,9,1,5,2]
numbers.remove(5)
numbers.pop(-3)
print(numbers)

#4.次の偶数のみを返す関数とfilter()を用いてnumbersリストから偶数のみを取り出したリストを作成せよ。
def isEven(number):
    if number%2==0:
        print(f"This number,{number} is even!")
        return True
    else:
        print(f"This number,{number} is odd!")
        return False
numbers=[5,0,3,8,-4,9,1,5,2]
print(list(filter(isEven,numbers)))

#5.numbersリストの中から要素が-4のインデックスを取得せよ。
numbers=[5,0,3,8,-4,9,1,5,2]
print(numbers.index(-4))

#6.numbersリストの順序を昇順/降順にそれぞれ並び替えよ。
numbers=[5,0,3,8,-4,9,1,5,2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)