import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import community
import itertools


def make_graph(partners, Country = "None"):
    Graph = nx.Graph()
    if Country == "None":
        for i in range(len(partners)):
            Graph.add_edge(partners[i].partner1, partners[i].partner2)
    else:
        for i in range(len(partners)):
            if partners[i].country == Country:
                Graph.add_edge(partners[i].partner1, partners[i].partner2)
    return Graph

def make_random_graph(num_nodes, num_edges):
    p=(2*num_edges)/((num_nodes)*(num_nodes-1))
    print(p)
    Erdos_Renyi=nx.generators.random_graphs.gnp_random_graph(num_nodes, p)
    return Erdos_Renyi


def num_edges(Graph):
    return Graph.number_of_edges()


def num_nodes(Graph):
    return Graph.number_of_nodes()


def get_degrees(Graph):
    D = []
    for k in Graph.degree:
        D.append((k[0], k[1]))

    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_degrees_dictionary(Graph):
    D={}
    for k in Graph.degree:
        D[k[0]] = k[1]
    return D


def get_degree_centrality(Graph):
    dictionary = nx.degree_centrality(Graph)
    D = []
    for name in dictionary:
        D.append((name, dictionary[name]))

    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_eigenvector_centrality(Graph):
    dictionary = nx.eigenvector_centrality(Graph, max_iter=200)
    D = []
    for name in dictionary:
        D.append((name, dictionary[name]))

    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_katz_centrality(Graph):
    dictionary = nx.katz_centrality(Graph, max_iter=2000)
    D = []
    for name in dictionary:
        D.append((name, dictionary[name]))

    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_pagerank(Graph):
    dictionary = nx.pagerank(Graph)
    D = []
    for name in dictionary:
        D.append((name, dictionary[name]))

    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_closeness_centrality(Graph):
    dictionary = nx.closeness_centrality(Graph)
    D = []
    for name in dictionary:
        D.append((name, dictionary[name]))

    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_betweenness_centrality(Graph):
    dictionary = nx.betweenness_centrality(Graph)
    D = []
    for name in dictionary:
        D.append((name, dictionary[name]))

    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_local_clustering(Graph):
    dictionary = nx.clustering(Graph)
    D = []
    tot=0
    for name in dictionary:
        D.append((name, dictionary[name]))
        tot=tot+dictionary[name]
    print(tot/num_nodes(Graph))
    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_clustering_coefficient(Graph):
    return nx.average_clustering(Graph)


def get_degree_assortative_coefficient(Graph):
    return nx.degree_assortativity_coefficient(Graph)


def get_triangles(Graph):
    return nx.triangles(Graph)


def get_average_shortest_path_length(Graph):
    return nx.average_shortest_path_length(Graph)


def get_degree_distribution(Graph):
    dist=nx.degree_histogram(Graph)
    tot=num_nodes(Graph)
    for i in range(len(dist)):
        dist[i]=dist[i]/tot
    dist.pop(0)
    return dist


def plot_degree_distribution(Graph):
    Degree_Distribution = get_degree_distribution(Graph)
    plt.plot(Degree_Distribution)


def plot_cumulative_degree_distribution(Graph):
    Degree_Distribution = get_degree_distribution(Graph)
    now_degree=sum(Degree_Distribution)
    total_degree=now_degree
    Cumulative_Distribution=np.zeros(len(Degree_Distribution))
    for i in range (0,len(Degree_Distribution)):
        Cumulative_Distribution[i]=now_degree/total_degree
        now_degree=now_degree-Degree_Distribution[i]
    plt.semilogy(Cumulative_Distribution)
    plt.xlabel("Degree")
    plt.ylabel("Cumulative Degree Distribution")


def partition_girvan_newman(Graph):
    return nx.algorithms.community.girvan_newman(Graph)


def get_community_dictionary(comm, k=4):
    k = k-1
    cc = []
    for communities in itertools.islice(comm, k):
        cc = tuple(sorted(c) for c in communities)

    comp = {}
    for i in range(len(cc)):
        for j in range(len(cc[i])):
            comp[cc[i][j]] = i
    return comp

def partition_modularity_max(Graph):
    return nx.algorithms.community.modularity_max.greedy_modularity_communities(Graph)


def partition_louvian(Graph):
    k = community.best_partition(Graph)
    return k
