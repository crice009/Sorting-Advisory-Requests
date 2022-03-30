from objects import *
from functions import *

classSize = 24 #the number of students we want in a class
partitioning_resolution = 1 #number take from testing function output

#\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /
# \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
#  \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/
#this is where the sorting happens
    # Collected Ideas below:
    # https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68#:~:text=Given%20a%20set%20of%20data,dissimilar%20properties%20and%2For%20features.
    # https://machinelearningmastery.com/clustering-algorithms-with-python/
    # https://homes.cs.washington.edu/~etzioni/papers/www8.pdf
    # https://www.researchgate.net/publication/221507594_A_Survey_on_Clustering_Algorithms_for_web_Applications
    #
    # https://dl.acm.org/doi/10.1145/3366424.3383296
    # http://theory.stanford.edu/~nmishra/Papers/clusteringSocialNetworks.pdf
    # probably this --> https://www.cse.msu.edu/~cse802/S17/slides/Lec_20_21_22_Clustering.pdf
    # definitely this --> https://towardsdatascience.com/social-network-analysis-from-theory-to-applications-with-python-d12e9a34c2c7
    # using 'networkx' & 'community' library for access to graph-data models & python-louvain partitioning methods
    # try this: https://www.geeksforgeeks.org/operations-on-graph-and-special-graphs-using-networkx-module-python/?ref=lbp
    # should probably make a dataset with two or three obvious cliques for a "barbell" graph


#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#convert the imported files into reasonable data tables
# buildBaseTables() #vestigial line
buildClusterTable() #from more broken-up data (to mock real life)
buildForeignKeys()  #for (maybe) faster lookups

#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#Build the Graph-Data set from the tables that were just made
import networkx as nx
import matplotlib.pyplot as plt
import math
# G = nx.DiGraph() #directional graph
G = nx.Graph() #nondirectional graph

for teacher in teachers:
    for tea in teacher.teachers:
        if tea is not None:
            x = findPersonByID(teachers, tea)
            # G.add_edge(teacher, x)
            if x != teacher:
                G.add_edge(teacher, x)

# summary of the Graph-Data
print("\t",G)
# this one is an interesting tidbit of Graph Theory
print("\t average shortest path between two nodes: ",nx.average_shortest_path_length(G))

#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#Use the Graph data, and some libraries to sort into communities
# taken from partition-networkx tutorial on pip page
print("--------From Networkx & Louvain-Community:")
import community #https://github.com/taynaud/python-louvain
print("\tFor community.best_partition resolution max is:",0.2*len(G.nodes), "min is: 1.0")
ml = community.best_partition(G,resolution=partitioning_resolution) #the resolution seems like it can be anywhere from 1.0 to 0.2n
import partition_networkx #https://github.com/ftheberge/graph-partition-and-measures  https://pypi.org/project/partition-networkx/
# ec = community.ecg(G, ens_size=10) 
# ec = community.ecg(G) 

hues=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080']

groups = ml #this is a dictionary | keys are nodes, vals are partition number
# groups = ec.partition #this is the ml equivalent dictionary, processed by another alrogithm
color_map=[]
labeldict={}
num_partitions = 0
for group in groups:
    if groups[group] > num_partitions:
        num_partitions = groups[group]
    # print(groups[group])
    color_map.append(
        hues[groups[group] % len(hues)])
    labeldict[group] = groups[group]

print("\t",num_partitions+1," automatically generated partitions")
# print(groups) #<--- this could use some more investigation...

#---------------------------------------------
# Draw the picture of the graph
nx.draw(G, node_color=color_map, node_size=175, labels=labeldict, with_labels = True)
plt.savefig("graph.png",dpi=200)
plt.figure().clear() #so the saved and displayed graph don't overlap "clear"
#---------------------------------------------

#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#test to find the best resolution to use 
print("testing for optimal match between resolution (X) and avg class size(Y)")
graphOptimalResolutions(G)