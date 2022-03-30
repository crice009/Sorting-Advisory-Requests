import csv
from importlib.metadata import packages_distributions
import random
from objects import *

##########################################################################
students = [] #array of all the unique student data
    #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | friends | teachers | lookupName
teachers = [] #array of all the unique teacher data
    #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | teachers | lookupName
##########################################################################

#go from 'Joe Smith' to 'joesmith'
def simpleFullName(name):
    arr = [x.strip() for x in name.split(' ')]
    sum_name = ''
    for i in arr:
        sum_name += i
    return sum_name.lower()

#will work for any array of objects with 'lookupName's
def findIDbyLookupName(list, request):
    request = simpleFullName(request)
    for individual in list:
        if request == individual.lookupName:
            return int(individual.id)

#will work for any array of objects with 'id's
def findPersonByID(list, request):
    for person in list:
        if person.id == request:
            return person

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

def buildClusterTable():
    with open('clique-teachers.csv') as csvfile:
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

#\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /
# \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
#  \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/
#----------------------------------------------------------------------------------------
# # #test to see how the resolution of the Function impacts things...
# # # I know it is a bit messy, be wee can refactor later. It is readable-ish.
def graphOptimalResolutions(G):    
    import community #https://github.com/taynaud/python-louvain
    from tqdm import tqdm
    import matplotlib.pyplot as plt
    import math
    parts_res_pattern=[]

    for i in tqdm(range(1,len(G.nodes))):
        res = i/20
        partitions = community.best_partition(G,resolution=res)
        num_parts = 0
        for node in partitions:
            if partitions[node] > num_parts: num_parts = partitions[node]

        pop = populations(partitions)
        sum_pop = 0
        for n in pop: sum_pop += n
        avg_pop = math.ceil(sum_pop/len(pop))
        parts_res_pattern.append([res,avg_pop])

    for i in parts_res_pattern:
        plt.scatter(i[0],i[1])
    plt.grid(True)
    plt.ylabel("Average Class Size")
    plt.xlabel("Louvain Partition Resolution Values")
    plt.show()


def populations(parts_dict):
    pop = []
    for node in parts_dict: pop.append(0)
    for node in parts_dict:
        i = parts_dict[node]
        pop[i] += 1
    for n in range(1,pop.count(0)): pop.remove(0)
    return pop
