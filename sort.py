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
#     #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | friends | teachers | lookupName
# teachers = [] #array of all the unique teacher data
#     #OBJ-format ==>> id | timestamp | email | fullname | firstname | surname | teachers | lookupName
# ##########################################################################
# stu_stu  = [] #array of all requested student pairs
#     #OBJ-format ==>> id | student1 | student2
# stu_tea  = [] #array of all requested student-teacher pairs
#     #OBJ-format ==>> id | student | teacher 
# tea_tea  = [] #array of all requested teacher pairs
#     #OBJ-format ==>> id | teacher1 | teacher2
# ##########################################################################

#\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /
# \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
#  \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/
#this is where the sorting happens

