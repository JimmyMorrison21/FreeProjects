from collections import deque


graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jhonny"]
graph["thom"] = []
graph["anuj"] = []
graph["jhonny"] = []
graph["peggy"] = []


def person_is_seller(x):
    return x[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print('{} is mango owner'.format(person.upper()))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")