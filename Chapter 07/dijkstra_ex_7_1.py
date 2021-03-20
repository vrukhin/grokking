#!/usr/bin/python

# алгоритм Дейкстры не может обработать граф C, т.к. он содержит ребро с отрицательным весом.
# граф A

graph = {}

graph["start"] = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["d"] = {}
graph["finish"] = {}

graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"]["d"] = 6
graph["c"]["finish"] = 3

graph["d"]["finish"] = 1

# хеш-таблица для хранения весов ребер

infinity = float("inf") # создадим переменную, равную бесконечности

costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["finish"] = infinity

# хеш-таблица родителей

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
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


print(costs["finish"])

# граф B

graph = {}

graph["start"] = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["finish"] = {}

graph["start"]["a"] = 10

graph["a"]["c"] = 20

graph["b"]["a"] = 1
graph["c"]["b"] = 1

graph["c"]["finish"] = 30

# хеш-таблица для хранения весов ребер

infinity = float("inf") # создадим переменную, равную бесконечности

costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["finish"] = infinity

# хеш-таблица родителей

parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
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


print(costs["finish"])
