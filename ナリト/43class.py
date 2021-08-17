class Student:#クラスは先頭を大文字に
    def __init__(self,name):
        self.name = name


a = Student('narito')#オブジェクトを一つ作る（インスタンス）
print(a.name)