liczba_gospodarstw = int(input())

array_czas_budowanie_zabiezpieczen = []
A_array = list()
B_array = list()
C_array = list()



for i in range(liczba_gospodarstw):
    p, a, b, c = list(map(int, input().split()))
    array_czas_budowanie_zabiezpieczen.append(p)
    A_array.append(a)
    B_array.append(b)
    C_array.append(c)


E = int(input())

graph = [[] for i in range(liczba_gospodarstw)]
array_ile_ma_nastepnikow = [0 for i in range(liczba_gospodarstw)]

#  konstrukcja grafu
for i in range(E):
    u, v = list(map(int, input().split()))  # input edge
    # adding directed edge u-v in the graph
    graph[u - 1].append(v - 1)

    # updating ile jest przed danym vertex
    array_ile_ma_nastepnikow[v - 1] += 1

topologic_sort = list(range(len(graph)))


stala = len(array_czas_budowanie_zabiezpieczen)
# print(f'graph {graph}')

answer_array = []
p = sum(array_czas_budowanie_zabiezpieczen)
# print(f'p = {p}')
while len(topologic_sort) != 0:
    L_array = [i for i in range(len(graph)) if len(graph[i]) == 0]
    #print(f'L_array {L_array}')
    funkcion_array = [0 for i in range(stala)]
    # print(f'function array = {funkcion_array}')
    #print(f'p = {p}')
    for index in L_array:
        wynik_f = (A_array[index] * (p**2)) + (B_array[index] * p) + C_array[index]
        # print(wynik_f)
        funkcion_array[index] = wynik_f
    #print(f'function_array {funkcion_array}')
    min_value = min([el for el in funkcion_array if el > 0 ])
    answer_array.append(min_value)
   # print(f'min_value = {min_value}')
    # answer_array.append(max(funkcion_array))
    numer_zadania = funkcion_array.index(min_value)
    #print(f'numer_zadania = {numer_zadania}')
    #uszeregowanie.insert(0, numer_zadania)
    # print(f'uszeregowanie {uszeregowanie}')
    topologic_sort.remove(numer_zadania)
    #print(f'topologic sort = {topologic_sort}')
    if len(topologic_sort) == 0:
        break
    p = p - array_czas_budowanie_zabiezpieczen[numer_zadania]
    # print(f'p = {p}')
    # array_czas_budowanie_zabiezpieczen.pop(numer_zadania)
    graph[numer_zadania] = (1000, )
    #print(f'graph = {graph}')

    for el in graph:
        if numer_zadania in el:
            el.remove(numer_zadania)

print(max(answer_array))

# trzeba obnowicz graf po wywaleniu wezla

