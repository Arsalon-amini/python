# and, or, not 

#not operator
#falsy values - empty string '' empty list [] 0 None - apply not to a false, get true
name = ''
if not name:
    print("Name is empty")
    
#and operator 
age = 22
if age >= 18 and age < 65: 
    print("You're eligable")

#rewrite in cleaner syntax 
if 18 <= age < 65:
    print("Eligable")


