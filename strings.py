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