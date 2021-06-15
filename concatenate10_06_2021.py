###Concatenate and Composition
##Concatenate
s = "AB"
print(s + "C")# ABC
# we can repeat 4
#print((s+ "C")*4)
repeat_4  = (s+ "C")*4
print(repeat_4)
#we can localize a string with:
print(repeat_4[2]) # string begging to counting in 0, so the result of this call is C and not B

##Composition
#int , str , and float tipes can be 'unidas' with:
age= 10
print("Jhon  have %d  , years old" %age)
