from objects import *
from setup import *

#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#convert the imported files into reasonable data tables
buildBaseTables()
# simpleTeaTea()

# ##########################################################################
# teachers = [] #array of all the unique student data
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
    # probably this --> https://www.cse.msu.edu/~cse802/S17/slides/Lec_20_21_22_Clustering.pdf
    # definitely this --> https://towardsdatascience.com/social-network-analysis-from-theory-to-applications-with-python-d12e9a34c2c7
    # using networkx library...

import networkx as nx
import matplotlib.pyplot as plt
import math
# G = nx.DiGraph() #directional graph
G = nx.Graph() #nondirectional graph

#---------------------------------------------
# test grid for positional drawing
#
# grid=[]
# dimension = int(math.sqrt(len(teachers)+4))
# for x in range(0,dimension):
#     for y in range(0,dimension):
#         grid.append([x,y])
# print(grid)
#---------------------------------------------

G.add_nodes_from(teachers)
# print (G.number_of_nodes(), " nodes present")
# print(G)

for teacher in teachers:
    for tea in teacher.teachers:
        if tea is not None:
            id = findIDbyLookupName(teachers, tea)
            x = findPersonByID(teachers, id)
            G.add_edge(teacher, x)

# print (G.number_of_edges(), " edges present")
print(G)

# nx.clustering(G)
max_clique = []
for person in nx.algorithms.approximation.clique.max_clique(G):
    max_clique.append(person.fullname)
print("Approximate max clique:",max_clique)    

#---------------------------------------------
# Draw the picture of the graph
nx.draw(G, node_size=50)
plt.savefig("graph.png",dpi=300)
#---------------------------------------------


# Thinking this might work: 
#   https://pypi.org/project/partition-networkx/




#\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /
# \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
#  \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/
#-------------------------------------------------------------------------------------------
# first attempt at 'communities'  || https://www.youtube.com/watch?v=PIVx1oedv2o&ab_channel=RoelVandePaar
#
# spring_pos = nx.spring_layout(G)
# parts = nx.best_partition(G)
# values = [parts.get(node) for node in G.nodes()]
# nx.draw(G, pos=spring_pos, cmap=plt.get_cmap("jet"), node_color=values, node_size=50)
# plt.savefig("graph.png",dpi=300)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# trying to use cliques to find breakdowns || https://networkx.org/documentation/stable/reference/algorithms/clique.html?highlight=cliques
#
# for i in nx.find_cliques(G):
#     clique = []
#     for j in i:
#         clique.append(j.fullname)
#     print(clique)
#     # print("\n")
#-------------------------------------------------------------------------------------------