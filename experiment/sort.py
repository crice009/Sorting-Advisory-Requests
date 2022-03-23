from objects import *
from setup import *

#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#convert the imported files into reasonable data tables
buildBaseTables()
buildForeignKeys()
buildSecondaryTables()

# ##########################################################################
# students = [] #array of all the unique student data
#     #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | friends[FK] | teachers[FK] | lookupName
# teachers = [] #array of all the unique teacher data
#     #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | teachers[FK] | lookupName
# ##########################################################################
# stu_stu  = [] #array of all requested student pairs
#     #OBJ-format ==>> id | student1 [FK] | student2 [FK]
# stu_tea  = [] #array of all requested student-teacher pairs
#     #OBJ-format ==>> id | student [FK] | teacher [FK] 
# tea_tea  = [] #array of all requested teacher pairs
#     #OBJ-format ==>> id | teacher1 [FK] | teacher2 [FK]
# ##########################################################################

#\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /
# \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
#  \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/
#this is where the sorting happens
    # Collected Ideas below:
    #
    # https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68#:~:text=Given%20a%20set%20of%20data,dissimilar%20properties%20and%2For%20features.
    # https://machinelearningmastery.com/clustering-algorithms-with-python/
    # https://homes.cs.washington.edu/~etzioni/papers/www8.pdf
    # https://www.researchgate.net/publication/221507594_A_Survey_on_Clustering_Algorithms_for_web_Applications
    #
    # https://dl.acm.org/doi/10.1145/3366424.3383296
    # http://theory.stanford.edu/~nmishra/Papers/clusteringSocialNetworks.pdf
    #  probably this --> https://www.cse.msu.edu/~cse802/S17/slides/Lec_20_21_22_Clustering.pdf
    

for student in students:
    count = 0
    for each in stu_stu:
        if each.student2 == student.id:
            count += 1
    stuRequestWeight.append([student.id, count])
print(stuRequestWeight)