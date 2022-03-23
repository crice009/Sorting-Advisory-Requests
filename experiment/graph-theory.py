from objects import *
from setup import *

#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#convert the imported files into reasonable data tables
# buildBaseTables()
buildClusterTable()
buildForeignKeys()
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

#---- turns out: nodes implied from edges ------- don't need these -------------
# G.add_nodes_from(teachers)
# print (G.number_of_nodes(), " nodes present")
# print(G)

for teacher in teachers:
    for tea in teacher.teachers:
        if tea is not None:
            x = findPersonByID(teachers, tea)
            # G.add_edge(teacher, x)
            if x != teacher:
                G.add_edge(teacher, x)

# print (G.number_of_edges(), " edges present")
print("\t",G)

# # nx.clustering(G)
# max_clique = []
# for person in nx.algorithms.approximation.clique.max_clique(G):
#     max_clique.append(person.fullname)
# print("Approximate max clique:",max_clique)    

#taken from partition-networkx tutorial on pip page
print("from partition-networkx libray:")
import community ## this is the python-louvain package which can be pip installed 
import partition_networkx
ml = community.best_partition(G)
ec = community.ecg(G, ens_size=10) 

# print(ml)
# groups = ec.partition
groups = ml
color_map=[]
num_partitions = 0
for group in groups:
    if groups[group] > num_partitions:
        num_partitions = groups[group]
    if groups[group] == 0:
        hue='#00ff00'
    if groups[group] == 1:
        hue='#ff0000'
    if groups[group] == 2:
        hue='#0000ff'
    if groups[group] == 3:
        hue='#ffff00'
    if groups[group] == 4:
        hue='#00ffff'
    if groups[group] == 5:
        hue='#ff00ff'
    color_map.append(hue)

print("\t",num_partitions+1," automatically generated partitions")
# print(groups) #<--- this could use some more investigation...

# print("\tAdjusted Graph-Aware Rand Index for Louvain:",G.gam(G, ml))
# print("\tAdjusted Graph-Aware Rand Index for ecg:",G.gam(G, ec.partition))

# print("\n\tJaccard Graph-Aware for Louvain:",G.gam(G, ml, method="jaccard",adjusted=False))
# print("\tJaccard Graph-Aware for ecg:",G.gam(G, ec.partition, method="jaccard",adjusted=False))

#---------------------------------------------
# Draw the picture of the graph
nx.draw(G, node_color=color_map, node_size=50)
plt.savefig("graph.png",dpi=200)
#---------------------------------------------


# Thinking this might work: 
#   https://pypi.org/project/partition-networkx/


# following these instructions: 
#   https://www.geeksforgeeks.org/python-clustering-connectivity-and-other-graph-properties-using-networkx/
# #------- only undirected graph -----------------------
# print(nx.is_connected(G))
# for n in list(nx.connected_components(G)): #this catches all that are even slightly connected.
#     count = 0
#     print(n)
#     for j in n:
#         count += 1
#     print(count, " items in connected 'clique'")

print("\t average short path between two nodes: ",nx.average_shortest_path_length(G))

# try this: https://www.geeksforgeeks.org/operations-on-graph-and-special-graphs-using-networkx-module-python/?ref=lbp
# should probably make a dataset with two or three obvious cliques for a "barbell" graph

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