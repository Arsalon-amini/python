#for loops can iteratre over anything that's iterable

#for loop - iterate a string, loop variable will hold one character
for x in "Python":
    print(x)

#for loop - iterate a list 
for x in ['a', 'b', 'c', 'd']:
    print(x)
 
#range object - loop over a sequence of numbers range(5) = (0, 1, 2, 3, 4) returns a range object that can be iterated over 
for x in range(5):
    print(x)

#range obj - excluding ending value in range
for y in range(0, 5):
    print(y)

#range obj - step function ex. step = 2 ending range = 10 output 0, 2, 4, 6, 8 (excludes ending range value)
for z in range(0, 10, 2):
    print(z)

#for else (example without else clausing using a flag)
names = ["Arsalon", "Dylan", "Jonathan", "Peter"]
found = False
for name in names:
    if name.startswith("A"):
        print("Found")
        found = True
        break
    if not found:
        print("not found")


#cleaner python syntax, else clause executed if for loop completes successfully without immediate break
names = ["Arsalon", "Dylan", "Jonathan", "Peter"]
for name in names:
    if name.startswith("A"):
        print("Found")
        break
    else:
        print("not found")
