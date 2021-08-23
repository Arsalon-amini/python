# returns number of items in a list | number of characters in a string
course = "Python Programming"
print(len(course))

# access individual characters in a string
print(course[0])

# negative index (will return circular indexing) - chars from end
print(course[-2])

# slicing
# pass start and end index (returns non inclusive of ending index)
print(course[0:3])
print(course[:3])  # exclude start index (python passes 0)
print(course[0:])  # exclude ending index (python passes len of string)

# exclude start/end (python passes 0 and length of string - result is entire )
print(course[:])

#strings are immutable - python allocates new memory and copies previous string into new memory + appends / deletes / slices chars
print(id(course))
print(id(course[0]))

#formatted strings (concatination)
first = "arsalon"
last = "amini"
full = first + ' ' + last
print(full)

#formatted strings (expression evaluated at runtime) - any valid expression between curly braces
first = "arsalon"
last = "amini"
full = f"{first} {last}"
print(full)

#string methods
course = "  Python for Machine Learning"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip()) #removes whitespace

print(course.find("Mach"))  #returns index of chars | case sensitive 
print(course.replace("P", "J"))

print("Machine" in course)  #check for existance in string
print("Machine" not in course)  # check for !existance in string
