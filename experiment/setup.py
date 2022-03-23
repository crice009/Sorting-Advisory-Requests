import csv
import random
from objects import *

##########################################################################
students = [] #array of all the unique student data
    #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | friends | teachers | lookupName
teachers = [] #array of all the unique teacher data
    #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | teachers | lookupName
##########################################################################
stu_stu  = [] #array of all requested student pairs
    #OBJ-format ==>> id | student1 | student2
stu_tea  = [] #array of all requested student-teacher pairs
    #OBJ-format ==>> id | student | teacher 
tea_tea  = [] #array of all requested teacher pairs
    #OBJ-format ==>> id | teacher1 | teacher2
##########################################################################

#go from 'Joe Smith' to 'joesmith'
def simpleFullName(name):
    arr = [x.strip() for x in name.split(' ')]
    sum_name = ''
    for i in arr:
        sum_name += i
    return sum_name.lower()

def findIDbyLookupName(list, request):
    request = simpleFullName(request)
    for individual in list:
        if request == individual.lookupName:
            return int(individual.id)

def findPersonByID(list, request):
    for person in list:
        if person.id == request:
            return person

#
#   The following function is a bit of a monolith.
#   It's goal is to sort all the form data into the
#     objects that are described above. 
#
#/\/\/\/\/\ main objects & arrays | setup \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
def buildBaseTables():
    with open('full-students.csv') as csvfile:
        studentReader = csv.DictReader(csvfile, delimiter=',')
        #------------- main students objects & array ----------------------
        for row in studentReader:
            students.append(Student(**row))
            students[-1].id = int(students[-1].id)
            students[-1].makeFriendsRequestArray()
            students[-1].makeTeachersRequestArray()
            students[-1].lookupName = simpleFullName(students[-1].fullname)

        print("\t", len(students), "\tunique Student-s in 'students' array")
        # print("\t\t\t", students[random.randrange(1,len(students))].__dict__)

    with open('full-teachers.csv') as csvfile:
        teacherReader = csv.DictReader(csvfile, delimiter=',')
        #------------- main teachers objects & array ----------------------
        for row in teacherReader:
            teachers.append(Teacher(**row))
            teachers[-1].id = int(teachers[-1].id)
            teachers[-1].makeTeachersRequestArray()
            teachers[-1].lookupName = simpleFullName(teachers[-1].fullname)

        # maybe go back here, and change the name-arrays into foreign keys
                #or in the functions below...
        print("\t", len(teachers), "\tunique Teacher-s in 'teachers' array")
        # print("\t\t\tex:", teachers[random.randrange(1,len(teachers))].__dict__)

#/\/\/\/\/\ foreign keys setup \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
def buildForeignKeys():
    #Change Friend/Teacher Request Arrays to foreign keys
    for student in students:
        for request in enumerate(student.friends):
            student.friends[request[0]] = findIDbyLookupName(students, request[1])

    for student in students:
        for request in enumerate(student.teachers):
            student.teachers[request[0]] = findIDbyLookupName(teachers, request[1])

    for teacher in teachers:
        for request in enumerate(teacher.teachers):
            teacher.teachers[request[0]] = findIDbyLookupName(teachers, request[1])
    
    print("\tConverted all requested names to Foreign Keys, for faster lookup. ['lookupNames' might be just as fast...]")

#/\/\/\/\/\ secondary array setup \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
def buildSecondaryTables():
    # #------------- Stu_Stu objects & array ---------------------------
    new_id = 0
    for i in students:
        for j in i.friends:
            new_id += 1
            stu_stu.append(Stu_Stu(i.id, j))
            stu_stu[-1].id = new_id

    print("\t", new_id, "\tstudent pair requests logged in 'stu_stu' array")
    # print("\t\t\tex:",stu_stu[random.randrange(1,len(stu_stu))].__dict__)

    #------------- Stu_Tea objects & array ---------------------------
    new_id = 0
    for i in students:
        for j in i.teachers:
            new_id += 1
            stu_tea.append(Stu_Tea(i.id,j))
            stu_tea[-1].id = new_id

    print("\t", new_id, "\tstudent-teacher pair requests logged in 'stu_tea' array")
    # print("\t\t\tex:",stu_tea[random.randrange(1,len(stu_tea))].__dict__)


    #------------- Tea_Tea objects & array ---------------------------
    new_id = 0
    for i in teachers:
        for j in i.teachers:
            new_id += 1
            tea_tea.append(Tea_Tea(i.id,j))
            tea_tea[-1].id = new_id

    print("\t", new_id, "\tteacher pair requests logged in 'tea_tea' array")
    # print("\t\t\tex:",tea_tea[random.randrange(1,len(tea_tea))].__dict__)

def simpleTeaTea():
    count = 0 
    for i in teachers:
        for j in i.teachers:
            if j is not None:
                count += 1
                tea_tea.append([i.id,j])
    print("\t", count, "\tteacher pair requests logged in 'tea_tea' array")