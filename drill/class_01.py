class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def intro(self):
        print(f"我是{self.name}，今年{self.age}岁")

    def average(self):
        try:
            return sum(self.scores) / len(self.scores)
        except ZeroDivisionError:
            return 0
        return sum(self.scores)/len(self.scores)
        

s = Student("张三",18, [90, 85, 77])
s.intro()
print(s.average())

s3 = Student("张三", 18, [])
print(s3.average())
print(Student("张三", 18, []).average())            # 期望 0
print(Student("张三", 18, [90, 85, 77]).average())  # 期望 84.0


