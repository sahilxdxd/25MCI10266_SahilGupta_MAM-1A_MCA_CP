t = int(input())
for _ in range(t):
    n = int(input())

    if n <= 4:
        print(-1)
        continue

    odds = []
    evens = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    # Print odds except 5
    for x in odds:
        if x == 5:
            continue
        print(x, end=" ")

    # Print 5 and 4 explicitly
    print(5, end=" ")
    print(4, end=" ")

    # Print evens except 4
    for x in evens:
        if x == 4:
            continue
        print(x, end=" ")

    print()
