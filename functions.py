#functions in python

def my_function(number, another_number):
    return number + another_number


output = my_function(2, 3)
print(output)

#return multiple things from a function
def my_new_function(number, another_number):
    return (number, number + another_number)

output_two = my_new_function(5, 3)
print(output_two)

#keyword args 
def my_alt_function(number, another_number):
    return number + another_number

#makes code more readable
output_three = my_alt_function(3, another_number=3)
print(output_three)


#assign default values 
def function (number, another_number = 5):
    return number + another_number

#don't have to pass a second argument 
output_four = function(3)
print(output_four)

#type hinting showing the types for args and type for return values (after the -> )
def function_hints(number: int, another_number: int = 3) -> int:
    return number + another_number

print(function_hints(3))


#passing arbitrary number of elements | python converts *arg into a tuple 
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total

print(multiply(2, 3, 4, 5))

#xxargs - can pass multiple key:value pairs as args
def save_user(**user):
    print(user["name"])

save_user(id=1, name="admin")

#function scope (python doesn't have block level scope, variable accessible anywhere in function)
def greet():
    if True:
        message = "it's a true message"
    print('defined inside a block (if statement), and still accessible within the function', message)

greet()