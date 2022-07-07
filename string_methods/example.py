s="my name is goutham my hobby is to beat my brother"
s=s.split()
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
for k,v in d.items():
    print("{} occurs {} at times:".format(k,v))           