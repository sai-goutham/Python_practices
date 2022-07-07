vowels=['a','e','i','o','u']
word=input("enter the string")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("for diff vowels are",word,len(found))             