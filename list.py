students = ["Roger", "Crystal", "Sebastian", "Yuri", "Vincent"]
#              0           1         2         3         4
#             -5          -4        -3        -2        -1


# List manipulation:
print(students)
print(len(students))
print("Roger" in students)
print("Yuki" in students)
print(students[1])
print(students[2:]) # from index 2 to end
print(students[:2]) # from start to index 2, excluding index 2
print(students[1:3]) # from index 1 to index 3, excluding index 3
print(students[-2])


# CRUD

# Create
students.append("Sagar")
students.insert(2, "Kanami")
print(students)

# Read
print(students[1])

# Update
students[1] = students[1].upper()
print(students.index("CRYSTAL"))
print(students)

# Delete
del students[1]

# Iteration
for student in students:
    print(f'{student} is amazing!')
    
# [ print(f'{student} is amazing!') for student in students]
sentences = [ f'{student} is amazing!' for student in students]

print(sentences)

print(list(enumerate(students)))

for index, student in enumerate(students):
    print(f'{index + 1} - {student}')