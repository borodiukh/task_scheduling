liczba_raportow = int(input())

p_array = []

# czyta input
for i in range(liczba_raportow):
    p = int(input())
    p_array.append(p)

# B - pojemnosc
B = int(sum(p_array) / 2)

# tworze macierz
macierz = [[-3 for j in range(B + 1)] for i in range(liczba_raportow + 1)]

# cala pierwsza columna wypewniam w 1
for i in range(liczba_raportow + 1):
    macierz[i][0] = 1

# caly pierwszy wiersz wypewniam w 0
for j in range(1, B + 1):
    macierz[0][j] = 0

# wypewniam pozostale komurki z pseudokodu na slajdzie
for i in range(1, liczba_raportow + 1):
    for j in range(1, B + 1):
        macierz[i][j] = macierz[i - 1][j]
        if p_array[i - 1] <= j:
            if macierz[i - 1][j - p_array[i - 1]] == 1:
                macierz[i][j] = 1

# for i in range(liczba_raportow + 1):
#     print(macierz[i])

# C - czas pracy Yulii
C = 0
for i in range(B, 0, -1):
    if macierz[liczba_raportow][i] == 1:
        C = i
        break

print(C, sum(p_array) - C)

