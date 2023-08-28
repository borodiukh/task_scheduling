liczba_operacij, liczba_informacji_o_kolejnosci = map(int, input().split())


array_time_for_ending_task = list()
for i in range(liczba_operacij):
    array_time_for_ending_task.append(int(input()))


graph = [[] for i in range(liczba_operacij)]


indeg = [0 for i in range(liczba_operacij)]


for i in range(liczba_informacji_o_kolejnosci):
    u, v = list(map(int, input().split()))  # input edge
    # adding directed edge u-v in the graph
    graph[u - 1].append(v - 1)


    # updating ile jest przed danym vertex
    indeg[v - 1] += 1


queue = []
for i in range(liczba_operacij):
    if indeg[i] == 0:
        queue.append(i)


counter = 0

# List to store the topological ordering of the vertices
topologic_sort = []

while queue:
    queue = sorted(queue)
    # Taking front node of the queue and adding it into the queue.
    node = queue[0] # zawsze rosnąco
    queue.pop(0)
    topologic_sort.append(node)
    counter += array_time_for_ending_task[node]


    # Iterate through all the neighbouring nodes of dequeued node u and decrease their in-degree by 1
    for neighbour in graph[node]:
        indeg[neighbour] -= 1
        # If the indegree of the neighbour becomes 0 add it to the queue.
        if indeg[neighbour] == 0:
            queue.append(neighbour)

for el in topologic_sort:
    print(el + 1)
print(counter)
