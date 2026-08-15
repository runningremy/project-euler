#Thiis started as a binary converter and turned into something that TRIED to read from a file and print the results of nanoseconds that the algorithm took to run the program.

import time
import math
import os
import matplotlib.pyplot as plt
import numpy as np

def main(x):
    
    start_time = time.perf_counter()

    c = 1
    binary = []
    while c > 0:
        a = math.log(x,2)
        b = math.floor(a)
        c = a - b
    print(c)

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    nanoseconds = execution_time * 1000000000
    nanoseconds = int(nanoseconds)

    print("Execution time:", nanoseconds, "nanoseconds")

    nanoseconds = str(nanoseconds)

    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(nanoseconds + "\n")
    
    data = []
    with open("data.txt", "r") as file:
        for line in file:
            data.append(line.strip())

    data = list(map(int, data))
    
    file_size = os.path.getsize('binaryconverter.py')
    print(file_size, "bytes")

    ypoints = np.array(data)

    plt.plot(ypoints)
    plt.show()

main(4)
time.sleep(2)
main(5)
