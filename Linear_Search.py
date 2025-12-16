lst = [1,32,45,65,2,4,98,78,34,80,32,68,32,80,532,12,4,678,9,42,45,990,55]

n = int(input("Enter Target number = "))

found = False
for i in lst:
    if i == n:
        found = True
        break

print("Found" if found else "Not found")


