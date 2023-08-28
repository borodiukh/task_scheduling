liczba_urzednikow, liczba_raportow = map(int, input().split())

p_array = list()
p_dict = dict()
liczba_urzednikow_array = [0 for i in range(liczba_urzednikow)]

for i in range(liczba_raportow):
    p = int(input())
    p_array.append(p)
    p_dict[i] = p

# licze dlugosc optymalnego uszeregowanie
suma_ = sum(p_array) / liczba_urzednikow
c_max = max(p_array)
c_max = max(suma_, c_max)
c_max = int(c_max)
print(int(c_max))

# algorytm mcnaughtona
time = 0
urzednik = 0

answer_dict = dict()

for i in range(liczba_urzednikow):
    answer_dict[i] = []



for numer_zadania, czas_wykonania in p_dict.items():
    if time + czas_wykonania <= c_max:
        liczba_urzednikow_array[urzednik] += czas_wykonania
        answer_dict[urzednik].append((numer_zadania + 1, time, time + czas_wykonania))
        time = time + czas_wykonania

    else:
        if c_max - (time - czas_wykonania + p_array[numer_zadania]) != 0:
            answer_dict[urzednik].append((numer_zadania + 1, time, c_max))
            answer_dict[urzednik + 1].append((numer_zadania + 1, 0, p_array[numer_zadania] - (c_max - time)))

            urzednik += 1
            time = p_array[numer_zadania] - (c_max - time)
        else:
            answer_dict[urzednik + 1].append((numer_zadania + 1, 0, p_array[numer_zadania] - (c_max - time)))

            urzednik += 1
            time = p_array[numer_zadania] - (c_max - time)

output = ""
for key, sub_list in answer_dict.items():
    output += f"{key + 1}: "
    for item in sub_list:
        output += f"{item[0]}[{item[1]},{item[2]}] "
    output += "\n"

print(output)



