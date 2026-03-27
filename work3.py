#program to convert any value in integer
print(int(3.14)) #3
#print(int(10+5j))  Type Error
print(int(True)) #1
print(int(False)) #0
#print(int("4.22"))  value Error
print(int("4"))#4

#program to convert any value into the
print(float(3))#3.0
#print(float(50+2j))  Type Error
print(float(True))#1.0
print(float(False))#0.0
print(float(4.22))#4.22
print(float("4"))#4.0


#program to convert any value into the complex value
print(complex(3))#(3+0j)
print(complex(12.5))#(12.5+0j)
print(complex(True))#(1+0j)
print(complex(False))#0j
print(complex("5"))#(5+0j)
print(complex("5.6"))#(5.6+0j)
#print(complex("name"))  Value Error
print(complex(5,-3))#(5-3j)
print(complex(True,False))#(1+0j)

#program to convert any value into the boolean value
print(bool(0))#False
print(bool(15))#True
print(bool(3.14))#True
print(bool(0.0))#False
print(bool(1+2j))#True
print(bool(0+0j))#False
print(bool(-1))#True
print(bool(False))#False
print(bool(True))#True
print(bool(""))#False

#program to check if 3 variables have same value then 3rd variable adrees is same
math = 50  
chemistry = 50  
physics = 50  
print('Address of Math      =:', id(math))  #140567677458664
print('Address of chemistry =:', id(chemistry))  #140567677458664
print('Address of physics   =:', id(physics))  #140567677458664

#program to check if 3 variables have differnt value then they stored in differnt adrees
math = 100    
chemistry = 50    
physics = 70    
print('Address of Math      =:', id(math))   #133433577631528 
print('Address of chemistry =:', id(chemistry))   #133433577629928 
print('Address of physics   =:', id(physics))  #133433577630568