import math, time, random

def main(x):
    start_time = time.perf_counter()
    y = x
    binary = []
    log = math.log(x,2)
    floor = math.floor(log)
    b = '0' * (floor + 1)
    for i in b:
        binary.append(i)
    binary[floor] = '1'
    while log - floor > 0:
        x = x - 2**floor
        log = math.log(x,2)
        floor = math.floor(log)
        binary[floor] = '1'
    else:
        binary.reverse()

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    nanoseconds = execution_time * 1000000000
    nanoseconds = int(nanoseconds)

    master = []
    master.append(y)
    binary_string = ''.join(binary)
    master.append(binary_string)

    print(master)


counter = 0
while counter < 1000000:
    rando = random.randint(1, 1000000)
    main(rando)
    counter = counter + 1
    time.sleep(1)

