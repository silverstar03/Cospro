import time
import numpy as np

record = list()
for j in range(50):
    start = time.time()
    count = 0
    for i in range(1, 100000):  # for(int i=1; i<number+1)
        current = i
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
            current = current // 10

    end = time.time()
    record.append(end - start)

print("차이의 평균\t\t", np.mean(record))
print("차이의 표준편차\t", np.std(record))