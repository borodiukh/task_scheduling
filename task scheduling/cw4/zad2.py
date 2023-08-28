liczba_zamowien = int(input())

p_array = []
d_array = []
d_dict = {}
for i in range(liczba_zamowien):
    p, d = list(map(int, input().split()))
    p_array.append(p)
    d_array.append(d)
    d_dict[i] = d


d_array_sorted = sorted(d_dict.items(), key=lambda x:x[1])


answer_array = []
time = 0

for numer_zadania, due_time in d_array_sorted:
    time += p_array[numer_zadania]
    answer_array.append((numer_zadania, p_array[numer_zadania]))

    # jesli zadanie mieszci sie
    if due_time - time >= 0:
        continue
    else:
        #time -= p_array[numer_zadania]

        answer_array = sorted(answer_array, key=lambda x:x[1])

        time -= p_array[answer_array[-1][0]]
        del answer_array[-1]

print(len(answer_array))


