n = int(input("enter:"))
factorial = 1
for i in range(1,n+1):
    factorial=n*factorial
    n=n-1
print(factorial)

