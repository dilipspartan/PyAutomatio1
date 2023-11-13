t1="dutta ji"
t2="pramod ji"
print(t1.capitalize())
print(t2.upper())

#length
name="dutta ji"
print(len(name))

name2=name.replace("dutta", "pramod")
print(name2)

name3=name.replace("dutta", "tirumalesh")
print(name3)

#find()-- returns lowest index value of substring in the same string
# returns -1 when the substring is not found

name99 = "hello my cute babai"
index = name99.find("babi")
print(index)

#count() -- count number of characters.
l_name="lot of last names left in the  names with lefty's"
count = l_name.count("s")
print(count)

#lenth() -- example
paragraph= ("the babu moshai tea is very tasty tan any other teas in  the world "
            "which makes it very foums among all the tea lkovers arpund the wprld")
length= len(paragraph)
print(length)
index_p=paragraph.find("tea")
print(index_p)