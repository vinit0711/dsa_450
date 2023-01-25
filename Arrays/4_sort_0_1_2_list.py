a = [1, 1, 0, 0, 2, 2, 1, 0]
l = 0
m = 0
h = len(a)-1
i = 0

for i in range(len(a)):
    if(a[m] == 1):
        m += 1
        continue
    elif(a[m] == 0):
        a[l], a[m] = a[m], a[l]
        l += 1
        m += 1
    elif(a[m] == 2):
        a[h], a[m] = a[m], a[h]
        h -= 1

print(a)
