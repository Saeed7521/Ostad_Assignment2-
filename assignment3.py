# Program 1
class Student1:
    def __init__(self, name = "Unknown", id = 0):
        self.name = name
        self.id = id
    def student_details(self):
        return f"{self.name} has id {self.id}"
    def student_hobbies(self):
        pass
std1 = Student1()
print(std1.student_details())
std2 = Student1("Amir")
print(std2.student_details())
std2 = Student1("Sara" , 1001)
print(std2.student_details())
# Program 2
class Person:
    def introduction(self):
        return f"I am a person"   
class Teacher(Person):
    def introduction(self):
        return "I am a teacher"
class Student(Person):
    def introduction(self):
        return f"I am a student"
class Dean(Teacher):
    def introduction(self):
        return f"I am a dean"
obj1 = Person()
print(obj1.introduction())
obj2 = Teacher()
print(obj2.introduction())
obj3 = Student()
print(obj3.introduction())
obj4 = Dean()
print(obj4.introduction())
# Program 3
class Prices:
    def __init__(self,price1, price2):
        self.__price1 = price1
        self.__price2 = price2
    def get_price(self):
        return self.__price1, self.__price2
    def set_price(self,price1,price2):
        self.__price1 = price1
        self.__price2 = price2
    def total_price(self, price1, price2=0):
        return price1 + price2
class Batter:
    def batting_skill(self):
        return f"I can bat"   
class Bowler:
    def bowling_skill(self):
        return f"I can bowl"
class Allrounder(Batter, Bowler):
    def own(self):
        return f"I can do both"   
obj5 = Prices(50,30)
print(obj5.get_price())
obj5.set_price(50,60)
print(obj5.get_price())
print(obj5.total_price(50,60))
print(obj5.total_price(60))
obj6 = Allrounder()
print(obj6.batting_skill())
print(obj6.bowling_skill())
print(obj6.own())                                        