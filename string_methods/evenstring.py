s="i am goutham sai"
s=s.split()
l=[]
l1=[]
for x in s:
    if len(x)%2==0:
        l.append(x)
    else:
        l1.append(x)    
print(l)
print(l1)