s=input("enter some string:")
l=s.split()
l1=[]
for x in l:
    l1.append(x[::-1])
    output=''.join(l1)
print(output)    
