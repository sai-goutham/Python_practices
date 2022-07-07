s={10,29,30,40}
l=[50,60,70]
s.update(l,range(1,5),"durga")
print(s)


print()
s={10,20,30}
s.update([9,99,54])
print(s)


print()
s={10,20}
s.update("go"+"hi")
print(s)
 
s={10,29,3,4,5,67,78,98,99,0,23}
s.update(range(1,3) and range(4,8))
print(s)