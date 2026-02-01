l1 =[]
l2 =[]
lc =[]

def common(l1,l2):
    for i in l1:
        if i in l2:
            lc.append(i)
    return lc

x = int(input("Enter first number = "))
y = int(input("Enter second number = "))

for i in range(1,x+1):
    if x % i == 0:
        l1.append(i)

for i in range(1,y+1):
    if y % i == 0:
        l2.append(i)

print(l1)
print(l2)

common(l1,l2)

k = len(lc)
print("The GCD of",x,"and",y,"is",lc[k-1])



