#identity operators -is and is not,  used with data structures, list, set etc..
# returns boolean valuesif both variables are same object or not, as list or set is an object
#donot use with primitive data types like a=10, b=10

x=[1,2,3]
y=[1,2,3]
print(x is y)
#False becoz x is not same as Y,
# as they are not saved in same reference/memory
print(x is not y) #True becoz x and y are not same
print(id(x)) # different locations of memory
print(id(y))