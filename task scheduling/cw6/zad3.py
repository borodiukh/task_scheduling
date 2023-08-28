liczba_pracownikow, liczba_zabawek = map(int, input().split())


dictionary = dict()
zadania_wykonane_na_czas = []
answer_array = []

for i in range(liczba_zabawek):
    w, d = map(int, input().split())
    dictionary[i] = (w, d)

sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1][1])
#print(sorted_dictionary)

time = [0 for i in range(liczba_pracownikow)]

for numer_zadania, (waga, due_time) in sorted_dictionary:
    # print(numer_zadania, waga, due_time)

    # wybieram maszyne
    time_pracownika = min(time)
    index_pracownika = time.index(time_pracownika)

    # jesli zadanie bedzie spoznione
    if time[index_pracownika] >= due_time:
        najmniejsza_waga_w_wykonanych = min(zadania_wykonane_na_czas)
        # jesli terazniejsza waga jest wieksza za najmniejsza z juz wykonanych
        if waga > najmniejsza_waga_w_wykonanych:
            # zamieniam zadania
            zadania_wykonane_na_czas.remove(najmniejsza_waga_w_wykonanych)
            answer_array.append(najmniejsza_waga_w_wykonanych)
            zadania_wykonane_na_czas.append(waga)
            continue
        # jesli terazniejsza waga jest mniejsza za najmniejsza z juz wykonanych
        # to bierzace zadanie odrazu w spoznione
        else:
            answer_array.append(waga)
            continue
    # jesli nie spoznione
    zadania_wykonane_na_czas.append(waga)
    time[index_pracownika] += 1
print(sum(answer_array))
