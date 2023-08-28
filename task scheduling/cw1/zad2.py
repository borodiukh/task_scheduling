# WSRT  WEIGHTED SHORTEST PROCESSING TIME

liczba_zaleglych_prac = int(input())
diff = {}
time = []
kara = []
for i in range(liczba_zaleglych_prac):
    time_to_do_task_in_days, kara_for_one_day = map(int, input(). split())
    time.append(time_to_do_task_in_days)
    kara.append(kara_for_one_day)
    diff[i] = time_to_do_task_in_days / kara_for_one_day
sorted_for_priority = sorted(diff.items(), key=lambda x:x[1])


task_queue = [par[0] for par in sorted_for_priority]
suma = 0
days = 0
for task_num in task_queue:
    suma += (time[task_num] + days) * kara[task_num]
    days += time[task_num]
print(suma)