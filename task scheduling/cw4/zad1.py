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


time = 0
answer_array = []
for numer_zad, due_time in d_array_sorted:
    time += p_array[numer_zad]
    opozninie = time - due_time
    answer_array.append(opozninie)
if max(answer_array) < 0:
    print(max(answer_array))
else:
    print(max(answer_array))