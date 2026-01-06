arr = [1, 2, 3, 5, 66, 77, 8, 54, 322, 56, 76]  #lists are array

#basic appending and insertion
arr.append(40)       
arr.insert(1, 15)    
print(arr)

#removing and deleting items
arr.remove(5)
del arr[1]
print(arr)

#updating
arr[0] = 99
print(arr)

#checking for elements
if 15 in arr:
    print("found!!")

#find max, min , sum
max = max(arr)
min = min(arr)
sum = sum(arr)

#reverse array
print(arr[::-1])

#sorting
arr.sort()
print(arr)

#linear search
arr = [3, 7, 9, 1]
target = 9
found = False
for i in arr:
    if i == target:
        found = True
        break
print("Found" if found else "Not Found")
