graph = {   "a":{"b": 4, "h": 8},
            "b":{"a": 4, "c": 8, "h":11},
            "c":{"b": 8, "d": 7, "i": 2, "f":4},
            "d":{"e": 9, "f": 14, "c":7 },
            "e":{"d": 9, "f":10 },
            "f":{"c": 4, "d":14, "e":10, "g":2},
            "g":{"f":2, "i":6, "h":1},
            "h":{"g":1, "i":7, "b":11, "a":8}
             }
tree_min = []
g_aux = {}
aresta = {}
for i in graph:
    g_aux[i] = 99
p0 = input('Aresta de origem: ')
aresta[p0] = 'None'
g_aux[p0] = 0
while g_aux:
    mini = list(min(zip(g_aux.values(), g_aux.keys())))
    mini_peso  = mini[0]
    mini_aresta = mini[1]
    if aresta[mini_aresta]!='None':
        tree_min.append(aresta[mini_aresta])
    next_graph = [i for i in graph[mini_aresta].keys()]
    for adj in next_graph:
        if adj in g_aux.keys():
            if graph[mini_aresta][adj] < g_aux[adj]:
                g_aux[adj] = graph[mini_aresta][adj]
                aresta[adj] = (mini_aresta, adj)
    g_aux.pop(mini_aresta)
print('Minimo: ',tree_min)