liczba_maszyn, liczba_swidrow = map(int, input().split())

p_array = []
for i in range(liczba_swidrow):
    p = int(input())
    p_array.append(p)


p_array = sorted(p_array)

time_maszin_array = [0 for i in range(liczba_maszyn)]

answer = 0

for p in p_array:
    number_of_maszin = min(time_maszin_array)
    #print(f'number of maszine = {time_maszin_array.index(number_of_maszin)}')
    number_of_maszin = time_maszin_array.index(number_of_maszin)
    time_maszin_array[number_of_maszin] += p
    #print(time_maszin_array)
    answer += time_maszin_array[number_of_maszin]
    #print(f'answer = {answer}')
print(answer)





