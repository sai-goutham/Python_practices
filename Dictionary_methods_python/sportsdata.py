students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
n=int(input())
for i in range(n):
    key_values = input().split()
    key , value =key_values[0],key_values[1]
    students_dict[key] = value 
print(students_dict)