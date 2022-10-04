student = {
  'name': 'Jaylon',
  'age': 27,
  'nationality': "France"
}

# Dict manipulation
print(len(student))
print("name" in student) # True, only searching within the keys
print("Jaylon" in student) # False, only searching within the keys
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

#CRUD

# Create
student["job"] = "Data Scientist"
print(student)

# Read
print(student["name"])
# print(student["hobby"])
print(student.get("name"))
print(student.get("hobby"))
print(student.get("hobby", "Not found"))

# Update
student["job"] = "Super Data Scientist"
print(student)

# Delete
del student["job"] 
print(student)

# Iteration
for key, value in student.items():
  print(f'{key} -- {value}')