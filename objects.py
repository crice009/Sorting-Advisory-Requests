
from types import NoneType


class Person:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    
    #both types of people have teacher lists
    #split the lists of teachers
    def makeTeachersRequestArray(self):
            self.teachers = self.teachers.split("|") #split() returns a list
            if isinstance(self.teachers, str):
                self.teachers = [self.teachers]

    #go from 'Mr. Smith' to 'Smith'
    def teaSurname(formal_name):
        return [x.strip() for x in formal_name.split('.')][1]

class Student(Person):
    def makeFriendsRequestArray(self):
            self.friends = self.friends.split("|") #split() returns a list
            if isinstance(self.friends, str):
                self.friends = [self.friends]

class Teacher(Person):
    def intentionallybBlank():
        return



class Relationship:
    id = 0

class Stu_Stu(Relationship):
    def __init__(self, student_1, student_2):
        self.student1 = student_1
        self.student2 = student_2

class Stu_Tea(Relationship):
    def __init__(self, student, teacher):
        self.student = student
        self.teacher = teacher

class Tea_Tea(Relationship):
    def __init__(self, teacher_1, teacher_2):
        self.teacher1 = teacher_1
        self.teacher2 = teacher_2
