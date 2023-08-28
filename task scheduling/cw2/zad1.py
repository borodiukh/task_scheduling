n = int(input())
array_time_when_can_do_task = []
array_time_to_do_task = []
dictionary = {}
for i in range(n):
    time_when_can_do_task, time_to_do_task = map(int, input().split())
    array_time_when_can_do_task.append(time_when_can_do_task)
    array_time_to_do_task.append(time_to_do_task)
    dictionary[i] = time_when_can_do_task  # number_of_task : when_can_do
good_queue_for_task = sorted(dictionary.items(), key=lambda x:x[1])

suma_minutes = 0
dict_answer = {}
for task_number, time_when_will_do in good_queue_for_task:
    if suma_minutes <= time_when_will_do:  # wait
        suma_minutes += (time_when_will_do - suma_minutes)
    suma_minutes += array_time_to_do_task[task_number]  # rob zadanie
    dict_answer[task_number] = suma_minutes  # for every task we know when ended
tmp = sorted(dict_answer.items(), key=lambda x:x[0])
for tuple_ in tmp:
    print(tuple_[1])
print(suma_minutes)

