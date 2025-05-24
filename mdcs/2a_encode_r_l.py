def printRLE(st):
    n = len(st)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and st[i] == st[i + 1]:
            count += 1
            i += 1
        print(st[i] + str(count), end=" ")
        i += 1


# Example usage
printRLE("aaabbcddd")  # Output: a3 b2 c1 d3
