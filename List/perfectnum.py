n=int(input("enter a the range:"))
Sum=0
for num in range(1,n+1):
    for i in range(1,num):
        if num%i==0:
            Sum=Sum+i       
    if num==Sum:
        print(num)      