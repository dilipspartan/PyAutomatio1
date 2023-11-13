#Create a program with 5 input of numbers add 1-2  duplicates and print non-duplicate numbers
#numbers=int(input("enter 1st number:\n"))
#print(numbers)
numbers=set()
numbers.add(input("enter 1st number"))
numbers.add(input("enter 2nd number"))
numbers.add(input("enter 3rd number"))
numbers.add(input("enter 4th number"))
numbers.add(input("enter 5th number"))
x=set(numbers)
print(numbers)
print(x)
print(type(numbers))
print(type(x))



