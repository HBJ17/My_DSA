lst = [95, 84, 101, 62, 73, 33, 90, 108, 115, 15, 45, 28, 24, 12, 56, 41, 50, 37, 79, 19, 3, 7, 150, 123, 67]

n = int(input("Enter Target number = "))

found = False

lst = sorted(lst)

print(f"The list in ascending order {lst}")

l = len(lst)

low = 0
high = l - 1

while low <= high:
    mid = (low+high)//2
    if lst[mid] == n:
        found = True
        break
    elif lst[mid] < n:
        low = mid + 1
    else:
        high = mid - 1
    
print(f"Found at position {lst.index(n)}" if found else "Not Found")


