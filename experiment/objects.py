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