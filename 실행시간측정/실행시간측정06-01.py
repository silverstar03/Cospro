import time
import numpy as np

record = list()
for j in range(30):
    start = time.time()

    for i in range(1000000):
        200%10
    end = time.time()
    record.append(end-start)


print("차이의 평균\t\t", np.mean(record))
print("차이의 표준편차\t", np.std(record))