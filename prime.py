var = int(input("ENTER A NUMBER:"))
count = 0
for i in range(1,var+1):
    if(var%i==0):
        count=count+1
if(count==2):
    print("it is a prime number")
else:
    print("its not a prime number")
        


