def main():
    even_fibs = [1,2];
    while even_fibs[-1] < 4000000:
        x = even_fibs[-1] + even_fibs[-2];
        even_fibs.append(x);
    even_fibs.pop();
    j = 0;
    for i in even_fibs:
        if i % 2 == 0:
            j = j + i;
        else:
            pass;
    print(j);
main()

