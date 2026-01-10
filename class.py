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