#string slicing
name="dilipkumar"
print(name)

#slice
print(name[0:2])
print(name[0:4])
print(name[3:7])
#last char is ignored while slicing -- 0, len-1
#no error is printed when max number is reached but it will print max char
# it is number of chars from start to len-1

print(name[0:11]) #prints max number but no error is throwed

