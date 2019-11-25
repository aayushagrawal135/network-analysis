import load_data
import network_functions as n_func
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import helper_functions as hf

filename="./cricinfo-statsguru-data/Test Matches - Partnerships.xlsx"
filename2="./cricinfo-statsguru-data/Test Matches - Batting.xlsx"


partners=load_data.load(filename)
batting=load_data.get_batting_average_dictionary(filename2)
# print(batting)

############################NETWORK PROPERTIES
print("#################NETWORK PROPERTIES######################")
countries=["India", "South Africa", "England", "New Zealand", "Australia", "West Indies"]
print("Country\t\t\tNumber of Nodes\tNumber of Edges\tAverage Degree\tClustering Coefficient\tAssortative Coefficient\tAverage Shortest Path Length")
for country in countries:
    Graph = n_func.make_graph(partners, country)
    Degrees=n_func.get_degrees_dictionary(Graph)
    Betweenness=nx.betweenness_centrality(Graph)
    x=list(Degrees.values())
    y=list(Betweenness.values())



    all_degrees=list(Degrees.values())
    avg_degree=np.mean(all_degrees)
    avg_betweenness=np.mean(y)
    print(avg_betweenness/avg_degree)
    avg_degree=round(float(avg_degree), 2)
    num_edges=n_func.num_edges(Graph)
    num_nodes=Graph.number_of_nodes()
    clustering_coefficient = n_func.get_clustering_coefficient(Graph)
    clustering_coefficient = round(float(clustering_coefficient), 2)
    assortative_coefficient=n_func.get_degree_assortative_coefficient(Graph)
    assortative_coefficient=round(float(assortative_coefficient), 2)
    avg_shortest_path_length=n_func.get_average_shortest_path_length(Graph)
    avg_shortest_path_length=round(float(avg_shortest_path_length),2)
    print(country+"\t"+str(num_nodes)+"\t"+str(num_edges)+"\t"+str(avg_degree)+"\t"+str(clustering_coefficient)+"\t"
          +str(assortative_coefficient)+"\t"+str(avg_shortest_path_length))
    n_func.plot_cumulative_degree_distribution(Graph)
plt.legend(countries)
plt.show()




###############FOR RANDOM GRAPH
print("##################FOR RANDOM GRAPHS")
num_nodes=388
num_edges=2529
Erdos_Renyi=n_func.make_random_graph(num_nodes, num_edges)
clustering_coefficient = n_func.get_clustering_coefficient(Erdos_Renyi)
clustering_coefficient = round(float(clustering_coefficient), 2)
avg_shortest_path_length=n_func.get_average_shortest_path_length(Erdos_Renyi)
avg_shortest_path_length=round(float(avg_shortest_path_length),2)
print(str(clustering_coefficient)+" "+str(avg_shortest_path_length))
##########################

###FOR BETWENNESS TABLE################
for country in countries:
    Graph = n_func.make_graph(partners, country)
    Degrees=n_func.get_degrees_dictionary(Graph)
    Betweenness=n_func.get_betweenness_centrality(Graph)
    num=5
    for i in range(5):
        name=Betweenness[i][0]
        betwn=Betweenness[i][1]
        degree=Degrees[name]
        avg=batting[name]
        print(str(round(betwn,2))+"\t"+str(degree)+"\t"+str(avg)+"\t"+name)
#################################################


############FOR GRAPH PARTITIONING########################
for country in countries:
    Graph = n_func.make_graph(partners, country)
    num_components=4
    comm = n_func.partition_girvan_newman(Graph)
    comp= n_func.get_community_dictionary(comm, num_components)
    nums= hf.get_component_sizes(comp)
    print(country+" "+str(nums))
    li= hf.component_dictionary_2_list(comp, num_components)
    zi=hf.get_zis(li, Graph)
    Pi=hf.get_Pis(li, Graph)

    mean_avg=np.zeros(num_components)
    CI=[]
    for i in range(len(li)):
        averages=[]
        for j in range(len(li[i])):
            averages.append(batting[li[i][j]])
        mean_avg[i]=np.mean(averages)
        CI.append(hf.calc_CI(averages))

    names=[]
    for i in range(len(li)):
        z_dict=zi[i]
        z_list=hf.dictionary_2_desc_pair_list(z_dict)
        num_names=3
        comm_name=[]
        num_nodes=int(nums[i])
        min=num_names
        if num_nodes<min:
            min=num_nodes
        for j in range(min):
            comm_name.append(z_list[j][0])
        names.append(comm_name)
    print(zi)
    print(Pi)

    R1=[]
    R2=[]
    R3=[]
    R4=[]
    R5=[]
    R6=[]
    R7=[]

    for i in range(len(li)):
        for j in range(len(li[i])):
            name=li[i][j]
            if(zi[i][name] < 2.5 and Pi[i][name]<=0.05):
                R1.append(name)
            elif(zi[i][name] < 2.5 and Pi[i][name]<=0.62):
                R2.append(name)
            elif (zi[i][name] < 2.5 and Pi[i][name] <= 0.80):
                R3.append(name)
            elif (zi[i][name] < 2.5 and Pi[i][name] > 0.80):
                R4.append(name)
            elif (zi[i][name] >= 2.5 and Pi[i][name] <= 0.30):
                R5.append(name)
            elif (zi[i][name] >= 2.5 and Pi[i][name] <= 0.75):
                R6.append(name)
            else:
                R7.append(name)

    print("R1 = " + str(R1))
    print("R2 = " + str(R2))
    print("R3 = " + str(R3))
    print("R4 = " + str(R4))
    print("R5 = " + str(R5))
    print("R6 = " + str(R6))
    print("R7 = " + str(R7))