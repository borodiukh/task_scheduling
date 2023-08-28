liczba_urzednikow, liczba_raportow = map(int, input().split())

p_array = list()
p_dict = dict()
liczba_urzednikow_array =[0 for i in range(liczba_urzednikow)]

for i in range(liczba_raportow):
    p = int(input())
    p_array.append(p)
    p_dict[i] = p

p_sorted_dict = sorted(p_dict.items(), key=lambda x:x[1], reverse=True)


for i in range(liczba_raportow):
    najmniej_rzgruzona_maszyna_index = min(liczba_urzednikow_array)
    najmniej_rzgruzona_maszyna_index = liczba_urzednikow_array.index(najmniej_rzgruzona_maszyna_index)

    liczba_urzednikow_array[najmniej_rzgruzona_maszyna_index] += p_sorted_dict[0][1]

    del p_sorted_dict[0]

print(max(liczba_urzednikow_array))





