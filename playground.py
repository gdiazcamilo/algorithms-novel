def file_records():
    return [n for n in range(1_000_000)]

def sort_file(records): # 0.57
    sorted_list = [0] * 10_000_000

    for record in records:
        sorted_list[record] = 1
    
    return [n for n in range(10_000_000) if n == 1]

def builtin_sort(records): # 0.02
    return sorted(records)


import time

records = file_records()
aveg = 0
for _ in range(10):
    start = time.process_time()
    builtin_sort(records)
    aveg += time.process_time() - start

print(aveg/10)