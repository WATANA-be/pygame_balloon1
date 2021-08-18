members = {}

class Student:
    def __init__(self,name):
        self.name = name
        self.score = {}#（からの辞書）selfがないとinitのメソッドが終わると見えなくなっちゃう
    def add_score(self,subject_name,point):
        self.score[subject_name] = point#キーに教科名
    def get_score(self,subject_name):
        return self.score.get(subject_name,'その教科はまだ')#ない時は、まだと表示
a = Student('narito')
narito = Student('narito')
members['narito']=narito#名前をキーにしてその値に対してstudentオブジェクトを作成
members['saitou']=Student('saitou')
members['yosida']=Student('yoshida')

print(members)
members['narito'].add_score('math',50)
