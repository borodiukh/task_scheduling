liczba_pracownikow, liczba_zabawek = map(int, input().split())

dictionary = dict()


for i in range(liczba_zabawek):
    zadanie = list(map(int, input().split()))
    dictionary[i] = zadanie

print(dictionary)

C = [[0 for j in range(liczba_pracownikow + 1)]for i in range(liczba_zabawek + 1)]
# print(C)

for i in range(liczba_zabawek + 1):
    for j in range(liczba_pracownikow + 1):
        if i == 0 or j == 0:
            pass
        else:
            C[i][j] = max([C[i - 1][j], C[i][j - 1]]) + dictionary[i - 1][j - 1]
# print(C)

for i in range(1, len(C)):
    print(C[i][liczba_pracownikow])