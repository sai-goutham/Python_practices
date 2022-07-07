def Function1(value,name='tracin'):
    str=''
    if value==0:
        for i in range(0, len(name),2):
            str=str+name[i]
    elif value==1:
        for i in range(1, len(name),2):
            str=str+name[i]
    return str
c=Function1(0)
print(c)