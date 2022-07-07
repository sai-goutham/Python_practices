s={x*x for x in range(1,9)}
print(s)
print()


s={x+x for x in range(1,19)}
s1={x for x in s if x%2==0}
s2={x for x in s if x%2!=0}
print(s1)
print(s2)