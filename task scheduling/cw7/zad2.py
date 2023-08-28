liczba_zadan, termin_do_ktorego_trzeba_wykonac = map(int, input().split())

dictionary = dict()
for i in range(liczba_zadan):
    time, waga = map(int, input().split())
    dictionary[i] = (waga, time)

# print(dictionary)

macierz = [[-3 for j in range(termin_do_ktorego_trzeba_wykonac + 1)] for i in range(liczba_zadan + 1)]


for i in range(liczba_zadan + 1):
    for j in range(termin_do_ktorego_trzeba_wykonac + 1):
        if i == 0 or j == 0:
            macierz[i][j] = 0
        elif dictionary[i - 1][1] > j:
            macierz[i][j] = macierz[i - 1][j]
        else:
            macierz[i][j] = max(macierz[i - 1][j], macierz[i - 1][j - dictionary[i - 1][1]] + dictionary[i - 1][0])

# maksymalna liczba punktow
print(macierz[liczba_zadan][termin_do_ktorego_trzeba_wykonac])

# for i in range(len(macierz)):
#     print(macierz[i])

# zadania ktore wykona
answer = []
j = termin_do_ktorego_trzeba_wykonac
for i in range(liczba_zadan, 0, -1):
    if macierz[i][j] != macierz[i - 1][j]:
        answer.append(i)
        j = j - dictionary[i - 1][1]

for i in range(len(answer) - 1, -1, -1):
    print(answer[i])


