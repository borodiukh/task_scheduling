liczba_dokumentow = int(input())

czas_na_podpisy_array = []
czas_na_pieczeci_array = []

for i in range(liczba_dokumentow):
    czas_na_podpisy, czas_na_pieczeci = map(int, input().split())
    czas_na_podpisy_array.append(czas_na_podpisy)
    czas_na_pieczeci_array.append(czas_na_pieczeci)

# print(czas_na_podpisy_array)
# print(czas_na_pieczeci_array)


suma_podpisy = sum(czas_na_podpisy_array)
suma_pieczeci = sum(czas_na_pieczeci_array)

array = [czas_na_podpisy_array[i] + czas_na_pieczeci_array[i] for i in range(liczba_dokumentow)]
print(max(suma_podpisy, suma_pieczeci, max(array)))