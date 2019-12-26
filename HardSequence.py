l = 0
a = [0]
k = 0
f = 0
j = 0
for x in range(1, 129):
    j = l - 1
    while j >= 0:
        if a[l] == a[j]:
            f = 1
            k = j
            break
        j = j - 1
    if f == 0:
        a.append(0)
    else:
        a.append(l - k)
    f = 0
    l = l + 1
t = int(input("Enter no of test cases "))
for m in range(0, t):
    n = int(input("Enter the value of n "))
    ctr = 0
    for c in range(0, n):
        if a[c] == a[n - 1]:
            ctr = ctr + 1
    print("Occurance at nth position are {}".format(ctr))
print(a)
