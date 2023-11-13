#area of circle
pie=3.14
r=int(input("enter raduis of circle:\n "))

area_circle=pie*r*r
print("area of circle is :", area_circle )

print("--------------------------")
print("--------------------------")

#takes 2 numbers as i/p and prints if >, < or equals to

a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))

print("a is greater",a>b)
print("a is smaller",a<b)
print("a & b are equal",a==b)
print("--------------------------")
print("--------------------------")

#max of 3 numbers entered by user
n1=int(input("enter 1st num:\n"))
n2=int(input("enter 2nd num:\n"))
n3=int(input("enter 3rd num:\n"))
check= ("n1 is greater" if (n1>n2 and n1>n3) else
("n2 is greater" if (n2>n1 and n2>n3) else "n3 is greater"))
print(check)

#Develop a Python script that calculates the square and cube of a given number.

num=int(input("enter a number:\n"))
num_square= num*num
print("square of number is:", num_square)
num_cube= num*num*num
print("cube of number is:", num_cube)