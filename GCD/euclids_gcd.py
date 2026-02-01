def gcd(m,n):
    if m < n:
        m,n = n,m

    if m%n==0:
        return n
    else:
        dif = m-n
        return gcd(max(n,dif),min(n,dif))


x = int(input("ENter first number = "))
y = int(input("Enter second number = "))

print(gcd(x,y))
