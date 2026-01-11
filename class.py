#1.Personクラスを用意し、クラス変数としてnationality:"japan"、say_hello()メソッドでは
# 「こんにちは、私の国籍は〇〇です。」と出力するようにせよ。〇〇には国籍名(nationality)が入る。
class Person:
    nationality="japan"

    def say_hello(self):
        print(f"こんにちは、私の国籍は{self.nationality}です。")
Person=Person()
print(Person.say_hello())

#2.1のPersonクラスにコンストラクタを使って、引数に名前を設定してnameというインスタンス変数
# をもたせよ。またsay_my_name()という自分の名前を出力するクラスメソッドを実装せよ。

class Person:
    nationality="japan"

    def __init__(self,name):
        self.name=name

    def say_hello(self):
        print(f"こんにちは、私の国籍は{self.nationality}です。")
    
    def say_my_name(self):
        print(f"私の名前は{self.name}です")

akira=Person("akira")
print(akira.name)

#3.先ほどのPersonクラスを継承したKidクラスを作成せよ。その際に自分の年齢を出力するように
#クラスメソッドsay_hello(age)(年齢を引数)を変更せよ。

class Kid(Person):
    def say_hello(self,age):
        print(f"私の名前は{self.name}です。年齢は{age}歳です。")
Kid=Kid("akira")
print(Kid.say_hello(18))

#4.先ほどのPersonクラス内の変数nationalityを外部から呼び出せないprivateな変数に、
#メソッドsay_my_name()も外部から呼び出せないprivateなメソッドに変更せよ。

class Person:
    __nationality="japan"

    def __init__(self,name):
        self.name=name

    def say_hello(self):
        print(f"こんにちは、私の国籍は{self.nationality}です。")
    
    def __say_my_name(self):
        print(f"私の名前は{self.name}です")
       
