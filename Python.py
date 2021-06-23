from math import pi
radius = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
