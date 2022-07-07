v={'a','e','i','o','u'}
w=input("enter some word:")
s=set(w)
d=s.intersection(v)
print("the different vowels present in given word",d)