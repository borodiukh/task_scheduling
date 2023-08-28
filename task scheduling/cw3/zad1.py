N = int(input())

array_when_task_can_do = []
array_how_long_to_do_from_start_to_end = []
update_czasy_gotownosci = [0 for i in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    array_when_task_can_do.append(a)
    array_how_long_to_do_from_start_to_end.append(b)

E = int(input())

graph = [[] for i in range(N)]
indeg = [0 for i in range(N)]

for i in range(E):
    u, v = list(map(int, input().split()))  # input edge
    # adding directed edge u-v in the graph
    graph[u - 1].append(v - 1)


    # updating ile jest przed danym vertex
    indeg[v - 1] += 1


# create list of poprzednikow
predecessors = [[] for i in range(N)]

for i in range(len(graph)):
    for el in graph[i]:
        predecessors[el].append(i)


# topological sort algorithm
queue = []
for i in range(N):
    if indeg[i] == 0:
        queue.append(i)


# List to store the topological ordering of the vertices
topologic_sort = []

while queue:
    queue = sorted(queue)
    # Taking front node of the queue and adding it into the queue.
    node = queue[0]  # zawsze rosnąco
    queue.pop(0)
    topologic_sort.append(node)

    # Iterate through all the neighbouring nodes of dequeued node u and decrease their in-degree by 1
    for neighbour in graph[node]:
        indeg[neighbour] -= 1
        # If the indegree of the neighbour becomes 0 add it to the queue.
        if indeg[neighbour] == 0:
            queue.append(neighbour)


# for index
counter = 0

for node in topologic_sort:
    # jesli nie ma poprzednikow
    if predecessors[node] == []:
        update_czasy_gotownosci[node] = array_when_task_can_do[node]
        counter += 1
    elif len(predecessors[node]) == 1:
        wynik = max(array_when_task_can_do[node], update_czasy_gotownosci[predecessors[node][0]] + array_how_long_to_do_from_start_to_end[predecessors[node][0]])
        update_czasy_gotownosci[node] = wynik

        counter += 1
    elif len(predecessors[node]) > 1:
        # jesli ma 2 i wiecej poprzedniki
        tmp = []
        counter = 0
        tmp.append(array_when_task_can_do[node])
        for el in predecessors[node]:
            wynik = update_czasy_gotownosci[predecessors[node][counter]] + array_how_long_to_do_from_start_to_end[predecessors[node][counter]]
            tmp.append(wynik)
            counter += 1
        update_czasy_gotownosci[node] = max(tmp)


# teraz wreszcie szeregujemy
answer_dict = dict()
for i in range(len(update_czasy_gotownosci)):
    answer_dict[i + 1] = update_czasy_gotownosci[i]


answer_tuple = sorted(answer_dict.items(), key=lambda x:x[1])


suma_minutes = 0
for task_number, time_when_can_start in answer_tuple:
    if suma_minutes < time_when_can_start:
        suma_minutes += time_when_can_start - suma_minutes
        suma_minutes += array_how_long_to_do_from_start_to_end[task_number - 1]

    else:
        suma_minutes += array_how_long_to_do_from_start_to_end[task_number - 1]


print(suma_minutes)









