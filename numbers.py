#representing numbers (dec, binary, hexidecimal, complex nums)

#binary
x = 10
y = 0b10  #number 2 in binary
z = bin(256)  #takes a number, returns binary representation

#hexidecimal
a = 0x12c #number 300 in hexidecmial system
b = hex(55)  #built in fn -> returns hexidecimal representation 


#complex numbers
c = 1 + 2j #in python 'j' reprseents imaginary number i in mathematics 

print(x, y, z, a, b, c)

#arithmetic operations
d = 10 + 3
e = 10 - 2
f = 10 * 3
g = 10 / 2.5    #returns a floating point number
h = 10 // 2.5   #returns an integer
i = 10 % 3      #modulous = remaineder or a division 
j = 10 ** 3  #exponent (left to power right)

k = 1
k += 1 #don't have x++ or x-- (increment / decrement operators)
