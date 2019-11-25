from scipy.stats import sem, t
from scipy import mean
import numpy as np

def calc_CI(data, confidence=0.95):
    n = len(data)
    m = mean(data)
    std = sem(data)
    h = std * t.ppf((1 + confidence) / 2, n - 1)
    start = m - h
    end = m + h
    return [start, end]


def dictionary_2_desc_pair_list(dictionary):
    D=[]
    for k in dictionary:
        D.append((k, dictionary[k]))
    D.sort(key=lambda x: x[1])
    D.reverse()
    return D


def get_component_sizes(comp):
    max = -1
    for k in comp:
        if comp[k] > max:
            max = comp[k]
    nums = np.zeros((max + 1))
    for k in comp:
        nums[comp[k]] = nums[comp[k]] + 1
    return nums


def component_dictionary_2_list(comp, num_components):
    li = []

    for i in range(num_components):
        li.append([])

    for k in comp:
        li[comp[k]].append(k)
    return li


def get_zis(li, Graph):
    num_components=len(li)
    ki = []
    zi = []
    ksi = np.zeros(num_components)
    Ssi = np.zeros(num_components)
    for i in range(num_components):
        ki.append({})
        zi.append({})
    for i in range(num_components):
        for j in range(0, len(li[i])):
            tot = 0
            for k in range(0, len(li[i])):
                if (Graph.has_edge(li[i][j], li[i][k])):
                    tot = tot + 1
            ki[i][li[i][j]] = tot
        l = list(ki[i].values())
        ksi[i] = np.mean(l)
        Ssi[i] = np.std(l)

    for i in range(num_components):
        for j in range(0, len(li[i])):
            if (Ssi[i] == 0):
                zi[i][li[i][j]] = 0
            else:
                zi[i][li[i][j]] = (ki[i][li[i][j]] - ksi[i]) / Ssi[i]
    return zi

def get_Pis(li, Graph):
    num_components = len(li)
    kis = []
    deg = []
    Pi = []
    for i in range(num_components):
        kis.append({})
        deg.append({})
        Pi.append({})

    for i in range(num_components):
        for j in range(0, len(li[i])):
            new_list = []
            degg = 0
            for k in range(0, num_components):
                tot = 0
                for l in range(0, len(li[k])):
                    if (Graph.has_edge(li[i][j], li[k][l])):
                        tot = tot + 1
                new_list.append(tot)
                degg = degg + tot
            kis[i][li[i][j]] = new_list
            deg[i][li[i][j]] = degg
            sum = 0
            for k in range(num_components):
                sum = sum + (kis[i][li[i][j]][k] / deg[i][li[i][j]]) ** 2
            Pi[i][li[i][j]] = 1 - sum
    return Pi