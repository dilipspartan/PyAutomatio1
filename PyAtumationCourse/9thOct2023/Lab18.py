string = "dilip KumaR"

x = string.capitalize() #only 1st character to be capital letter
print(x)

x1 = string.upper() #all the word in capitals
print(x1)

x2 = string.lower() #only 1st character to be lowercase letter
print(x2)

print(id(x))
print(id(x1))
print(id(x2))

#strings are immutable
#once a function is used on string new string is formed

#x[0]="A" #string doesnot support char assignment

print(string.swapcase())
#uppercase converted to lower case and lowercase is converted to uppcase in string
name="kekaa poo"
print(name.title())
#returns title case version of string where word starts with uppcase and remaining with lower case

print(len(name))
#print(name.len()) -- we cannot use length obj on string

#replace

text="hello babai"
resl_replace = text.replace('babai','boseworld')
print(resl_replace)
print(text)

#index and len
#length of string starts from 1(count) ex: dilip--5->length
#index[0]-in dilip - d --> it is a character position

name80="dilip kumar"
print(name80)
del name80
print(name80)



