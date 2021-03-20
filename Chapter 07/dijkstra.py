#!/usr/bin/python

# более подробно алгоритм описан в файле dijkstra.md

# хеш-таблица моделирующая граф

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["finish"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5

graph["finish"] = {}

# хеш-таблица для хранения весов ребер

infinity = float("inf") # создадим переменную, равную бесконечности

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

# хеш-таблица родителей

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

# список обработанных вершин
processed = []

# реализация алгоритма

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_code_node = None
    for node in costs: # перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # если узел с наименьшей стоимостью и не обработан ...
            lowest_cost = cost # он становится новым узлом с наименьшей стоимостью
            lowest_code_node = node
    return lowest_code_node

node = find_lowest_cost_node(costs) # найти узел с наименьшей стоимостью среди необработанных

while node is not None: # если обработаны все узлы, цикл завершается
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # если к соседу можно добраться быстрее через текущий узел, ...
            costs[n] = new_cost # ... то обновляется стоимость узла ...
            parents[n] = node # ... и этот узел становится новым родителем для соседа
    processed.append(node) # узел помечается как обработанный
    node = find_lowest_cost_node(costs) # найти следующий узел для обработки и повторить цикл


# функция поиска пути (вызывается после выполнения алгоритма)
def find_way(parents):
    way = []
    node = "finish"
    while node != "start":
        way.insert(0, node)
        node = parents[node]
    
    print(way)

find_way(parents)
