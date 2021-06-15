###Exercices relacional and logic operators.
##3.6
#Let's do It!
Math = 7 # math receive 7
Science = 6 #math receive 6
Portuguese = 8 # math receive
#all med's need to be (maior) who 7
ToF = Math > 7 and Science > 6 and Portuguese > 8 #Relacional operators will be calculed first and before logic operators
print(ToF)#False

##using If, can make this:
Math = float(input("Type the medium this student in math: "))
Science = float(input("Type the medium this student in science: "))
Portuguese = float(input("Type the medium this student in portuguese: "))
ToF = Math > 7 and Science > 7 and Portuguese>7
if ToF > 7:
    print("This student be aproved because your note is:" + str(ToF))#in this case ToF var need be parse to string, because string just concatenate with string;
else:
    print("This stundet not be aproved because your note is:" + str(ToF))
   
    
