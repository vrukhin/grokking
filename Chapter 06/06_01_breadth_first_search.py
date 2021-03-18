#!/usr/bin/python

# функция проверки человека

def person_is_seller(person):
    return person[-1] == 'm' # для примера будем считать продавцом манго человека, чье имя заканчивается на m

# создание графа

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# создание двухсторонней очереди (дека)

from collections import deque


def search(name):
    search_queue = deque() # создание очереди
    search_queue += graph["you"] # соседи добавляются в очередь поиска
    searched = [] # чтобы не было рекурсии будем вести список проверенных людей
    while search_queue:
        person = search_queue.popleft() # первый человек извлекается из очереди
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
    print("Seller not found")
    return False

search("you")
