#<辞書>
#1.以下のデータからメソッドを使って、要素Aと要素Bを削除せよ。またclearメソッドを使ってすべての要素を削除せよ。
dictionary={"A":"岡本","B":"明","C":"男性","D":"鳥取県","E":"海外旅"}
dictionary.pop("A")
dictionary.pop("B")
print(dictionary)
dictionary.clear()
print(dictionary)

#2.以下の辞書から・キーのみを表示。・値の中に男性という文字列が存在するか。・すべてのキーと値を表示。
dictionary={"A":"岡本","B":"明","C":"男性","D":"鳥取県","E":"海外旅"}
print(dictionary.keys())
print("男性" in dictionary.values())
for a,b in dictionary.items():
    print(f"キーは{a}でバリューは{b}です")

#3.以下の辞書からCとEに対応する値を表示せよ。
dictionary={"A":"岡本","B":"明","C":"男性","D":"鳥取県","E":"海外旅"}
print(dictionary["C"])
print(dictionary.get("E"))