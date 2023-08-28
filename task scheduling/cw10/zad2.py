liczba_pracownikow, liczba_zabawek = map(int, input().split())


dictionary = dict()
tmp_dictionary = dict()

for i in range(liczba_zabawek):
    zadanie = list(map(int, input().split()))
    dictionary[i] = zadanie

# print(dictionary)

kolejka = sorted(dictionary.items(), key=lambda x:sum(x[1]), reverse=True)
# print(f'kolejka {kolejka}')

index_insert = 0
max_numer_uszeregowanie_was = 0
kolejnosc_global_array = []
c_max_global = 0
c_max_global_array = []
array_of_all_task = [[] for i in range(liczba_zabawek)]
# print(array_of_all_task)
# print()

# algoritm
for numer_zadania in range(liczba_zabawek):
    counter = 0
    for numer_uszeregowania in range(numer_zadania + 1):
        tmp_counter = 0
        array_of_all_task[numer_uszeregowania] = kolejnosc_global_array.copy()
        # print(f'kolejnosc_global_array {kolejnosc_global_array}')
        # print(f'numer zadania = {numer_zadania}')
        # print(f'numer uszeregowania = {numer_uszeregowania}')
        # print(f'array_of_all_task =  {array_of_all_task}')
        # print('-----')

        array_of_all_task[numer_uszeregowania].insert(index_insert, kolejka[numer_zadania])
        # print(f'array_of_all_task =  {array_of_all_task}')
        for el in array_of_all_task[numer_uszeregowania]:
            tmp_dictionary[tmp_counter] = el[1]
            tmp_counter += 1
            # print(f'tmp_counter {tmp_counter}')

        # print(f'tmp_dictionary {tmp_dictionary}')
        C = [[0 for j in range(liczba_zabawek + 1)] for i in range(len(array_of_all_task[numer_uszeregowania]) + 1)]
        # print(C)
        # print(f'array_of_all_task =  {array_of_all_task}')
        for i in range(len(array_of_all_task[numer_uszeregowania]) + 1):
            for j in range(liczba_pracownikow + 1):
                if i == 0 or j == 0:
                    pass
                else:
                    C[i][j] = max([C[i - 1][j], C[i][j - 1]]) + tmp_dictionary[i - 1][j - 1]
        # print(C)
        c_max = C[len(array_of_all_task[numer_uszeregowania])][liczba_pracownikow]
        # print(f'c_max = {c_max}')
        c_max_global_array.insert(numer_zadania, c_max)
        index_insert += 1
        # print(kolejnosc_global_array)
        #print(f'c_max_global_array {c_max_global_array}')
    index_insert = 0
    # print('podsumowanie po wykonaniu zadania')
    # print()
    # print(f'array_of_all_task =  {array_of_all_task}')
    # print(f'c_max_global_array {c_max_global_array}')
    najkrotsze_z_uszeregowan = min(c_max_global_array)
    index_najkrotszego_uszeregowania = c_max_global_array.index(najkrotsze_z_uszeregowan)
    kolejnosc_global_array = array_of_all_task[index_najkrotszego_uszeregowania]
    # print(f'kolejnosc_global_array {kolejnosc_global_array}')
    if numer_zadania == liczba_zabawek - 1:
        print(min(c_max_global_array))
        for el in kolejnosc_global_array:
            print(el[0] + 1, end=' ')
    c_max_global_array = []

    # print()
    # print()
    # print()










