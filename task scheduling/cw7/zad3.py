liczba_zadan = int(input())

czas_wykonania_array = []
liczba_punktow_za_zadanie_array = []
termin_array = []

for i in range(liczba_zadan):
    czas, liczba_punktow, termin = map(int, input().split())
    czas_wykonania_array.append(czas)
    liczba_punktow_za_zadanie_array.append(liczba_punktow)
    termin_array.append(termin)

# print(czas_wykonania_array)
# print(liczba_punktow_za_zadanie_array)
# print(termin_array)

index = termin_array[liczba_zadan - 1] + 1
macierz = [[-3 for j in range(index)] for i in range(liczba_zadan + 1)]


# for i in range(len(macierz)):
#     print(macierz[i])


# wypewnie całej macierzy
for j in range(liczba_zadan + 1):
    for t in range(index):
        if j == 0:
            macierz[j][t] = 0
        elif t == 0:
            suma = 0
            for i in range(j):
                suma += liczba_punktow_za_zadanie_array[i]
            macierz[j][t] = suma
        elif t <= termin_array[j - 1]:
            if t >= czas_wykonania_array[j - 1]:
                macierz[j][t] = min(macierz[j - 1][t - czas_wykonania_array[j - 1]], macierz[j - 1][t] + liczba_punktow_za_zadanie_array[j - 1])
            else:
                macierz[j][t] = macierz[j - 1][t] + liczba_punktow_za_zadanie_array[j - 1]
        else:
            macierz[j][t] = macierz[j][termin_array[j - 1]]

# print(macierz[liczba_zadan][termin_array[liczba_zadan - 1]])


# array spoznionych zadan
t = termin_array[liczba_zadan - 1]
# print(t)
answer = []
for j in range(liczba_zadan, -1, -1):
    t = min(t, termin_array[j - 1])
    if macierz[j][t] == macierz[j - 1][t] + liczba_punktow_za_zadanie_array[j - 1]:
        answer.append(j - 1)
    else:
        t = t - czas_wykonania_array[j - 1]
# print(answer)

# zadania ktore wykona
suma = 0
answer_array = []
for i in range(liczba_zadan):
    if i not in answer:
        answer_array.append(i + 1)
        suma += liczba_punktow_za_zadanie_array[i]

print(suma)
for el in answer_array:
    print(el)


