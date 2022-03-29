from objects import *
from setup import *

#  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \
#/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
#convert the imported files into reasonable data tables
# buildBaseTables() #vestigial line
buildClusterTable()
buildForeignKeys()

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
    # using 'networkx' & 'community' library for access to graph-data models & python-louvain partitioning methods
    # try this: https://www.geeksforgeeks.org/operations-on-graph-and-special-graphs-using-networkx-module-python/?ref=lbp
    # should probably make a dataset with two or three obvious cliques for a "barbell" graph

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

print("\t",G)

#taken from partition-networkx tutorial on pip page
print("\tFrom the imported partitioning libray:")
import community #https://github.com/taynaud/python-louvain
max_res = 0.2*len(G.nodes) #about as high as it seems to be stable
low_res = 1.0 #also the default value
ml = community.best_partition(G,resolution=low_res) #the resolution seems like it can be anywhere from 1.0 to 0.2n
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
#---------------------------------------------

print("\t average shortest path between two nodes: ",nx.average_shortest_path_length(G))

#\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /
# \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
#  \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/
#-------------------------------------------------------------------------------------------
# # #test to see how the resolution of the Function impacts things...
# partition_resolution_pattern=[]
# from tqdm import tqdm
# for i in tqdm(range(1,len(G.nodes)*10)):
#     res = i/20
#     nodes_dict = community.best_partition(G,resolution=res)
#     #nodes_dict = community.ecg(G, ens_size=int(res*20)).partition

#     new_parts = 0
#     for node in nodes_dict:
#         if nodes_dict[node] > new_parts:
#             new_parts = nodes_dict[node]
#     partition_resolution_pattern.append([res,new_parts])

# for i in partition_resolution_pattern:
#     plt.scatter(i[0],i[1])
# plt.show()