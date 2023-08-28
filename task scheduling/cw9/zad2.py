liczba_plyt = int(input())

dictionary = dict()

for index in range(liczba_plyt):
    czas_na_wyciecie, czas_na_wywiercenie_otworow = map(int, input().split())
    dictionary[index] = (czas_na_wyciecie, czas_na_wywiercenie_otworow)

# print(dictionary)

A = dict()
B = dict()

for numer_zadania, (p1, p2) in dictionary.items():
    if p1 <= p2:
        A[numer_zadania] = (p1, p2)
    else:
        B[numer_zadania] = (p1, p2)

# print(A)
# print(B)

A = sorted(A.items(), key=lambda x:x[1][0])
B = sorted(B.items(), key=lambda x:x[1][1], reverse=True)

# print(A)
# print(B)

queue = A + B
# print(queue)

time_array = [0, queue[0][1][0]]
# print(time_array)

for numer_zadania, (p1, p2) in queue:
    print(numer_zadania + 1, end=' ')
    time_array[0] += p1
    print(time_array[0], end=' ')
    if time_array[1] < time_array[0]:
        time_array[1] = time_array[0]
    time_array[1] += p2
    print(time_array[1])




