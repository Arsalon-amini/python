age = 22

# no curly brances, an indentation signifies a code block
# pep 8 specifies four spaces for indentation (cannot mix tab and four spaces)

if age >= 18:
    print("This is an adult")
    print("this is an adult")
elif age >= 13:
    print("this is a teenager")
else:
    print("done")

# ternary operatory in Java
# message= age >= 18 ? "Eligable": "Not Eligable")

# ternary operator in python
message = "Teenager" if age >= 18 else "Adult"
