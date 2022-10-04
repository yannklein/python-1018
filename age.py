# define an age variable and assign the user input into it
age = int(input("How old are you? "))

print(age)

# Concatenation
print( "You are " + str(age) + " years-old.")

# Interpolation (f formatting)
print(f'You are {age} years-old.')

# re-assigning age, incrementing it
# age = age + 1
age += 1

print(f'You will be {age} years-old next year.')