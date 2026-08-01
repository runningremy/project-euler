import time

def project_euler1(x):
    y = range(x)
    z = []
    a = []
    for i in y:
        if i % 3 == 0:
            z.append(i);
        else:
            pass;
    for i in y:
        if i % 5 == 0:
            a.append(i);
        else:
            pass;
    b = z+a;
    b.sort()
    unique_numbers  = list(dict.fromkeys(b))
    c = sum(unique_numbers)
    print(c)
        
start_time = time.perf_counter()
project_euler1(1000)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
