from math import ceil

liczba_maszyn, liczba_swidrow = map(int, input().split())

ile_czasu_zajmie_pyproduk_swidra_rozmiaru_1_array = list(map(int, input().split()))

print(ile_czasu_zajmie_pyproduk_swidra_rozmiaru_1_array)

p_array = []
for i in range(liczba_swidrow):
    p = int(input())
    p_array.append(p)

p_array = sorted(p_array, reverse=True)
print(p_array)

macierz = list()
w_array = []
for x in ile_czasu_zajmie_pyproduk_swidra_rozmiaru_1_array:
    w_array.append(1/x)
    macierz.append([])

print(w_array)
print(macierz)

answer = 0
counter = 0
for p in p_array:
    print(f'zadanie numer = {counter}')
    w = min(w_array)
    w_index = w_array.index(w)
    print(f'w = {w}')
    for i in range(len(macierz[w_index])):
        macierz[w_index][i] += ceil(p * (1 / ile_czasu_zajmie_pyproduk_swidra_rozmiaru_1_array[w_index]))


    print(f'wartosc = {p * (1 / ile_czasu_zajmie_pyproduk_swidra_rozmiaru_1_array[w_index])}')
    macierz[w_index].insert(0, ceil(p * (1 / ile_czasu_zajmie_pyproduk_swidra_rozmiaru_1_array[w_index])))
    print(macierz)
    w_array[w_index] = w + (1 / ile_czasu_zajmie_pyproduk_swidra_rozmiaru_1_array[w_index])
    print(f'w_array = {w_array}')
    counter += 1
    print()
print(macierz)

for i in range(liczba_maszyn):
    answer += sum(macierz[i])
print(int(answer))