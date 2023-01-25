a = [1, 2, 3, 4, 5]

min = a[0]
max = a[0]
for i in range(len(a)):
    if (a[i] < min):
        min = a[i]
    elif(a[i] > max):
        max = a[i]
    print(min, max)
print("-")
print(min, max)
