# # 10 + 20     # int + int
# # "10" + "20" # str + str
# # 10 + "20"   # int + str

# print(10 + 20 )   # 30
# print("10" + "20") # 1020       # string concate  # string ko jodna
###print(10 + "20")# TypeError: unsupported operand type(s) for +: 'int' and 'str'

### ----------------------------------------------------------------
# # Typecasting

# aValueInt = 10      # integer 
# bValueStr = "20"    # str

# print(type(bValueStr))      #str

# bValueInt = int(bValueStr)  # int() is function which takes input and convert and provide value in integer 
# print("type(bValueStr) = ", type(bValueStr))    #type(bValueStr) =  <class 'str'>
# print("type(bValueInt) = ", type(bValueInt))    # type(bValueStr) =  <class 'int'>

# ###print(aValueInt + bValueStr)    ## int + str # invalid operation

# print("Addition : ", aValueInt + bValueInt)    #Addition :  30

# ## --------------------------------------------------------------------


# aValueInt = 10      # integer 
# bValueFloat = 20.5    # float

# print(aValueInt + bValueFloat)  # 30.5

### -------------------------------------

aValueInt = 10      # integer 
bValueFloat = "20.5"    # str

# ##print(aValueInt + bValueFloat)  # Error why? can not add int with str

# ## if you want output 1020.5    then typecast to aValueInt to str
# ##   by using str(aValueInt)

# ## if you want output 30.5    then typecast to bValueFloat to float
# ##   by using float(aValueInt)

# print(aValueInt + float(bValueFloat))   #30.5

### ---------------------------------------------------------

# aValue = 10.4           
# conveted = int(aValue)      # portion before . will be integer and later part will be skipped 
# print(conveted)         # 10
# print(type(conveted))   #<class 'int'>


###-------------------------------------------------------------
## inteview
aValue = "10.4"         # when we have . in float which is wrapped under str will not be converted to int
# # conveted = int(aValue)  # invalid     # ValueError: invalid literal for int() with base 10: '10.4'
# # conveted = float(aValue)      # ValueError: invalid literal for int() with base 10: '10.4'
conveted = int(float(aValue)) 
print(conveted)         # 10
print(type(conveted))   #<class 'int'>

## still you want to convert float string to int then first convert into float and then int
# conveted = int(float(aValue)) 
  
### ---------------------------------------------------------------------

# any string can be conveted into int but only if it is valid number
# any type can be converted to another if it is valid respective datatype
aTemp = "10sfd"     # we can not convert to in 
 
### ----------------------------------------------------------------
### Boolean

print("#")
print("##")
print("###")
print("####")
print("#####")

print('''
#
##
###
####
#####
''')

print(10 * 1)
print(10 * 2)
print(10 * 3)
print(10 * 4)
print(10 * 5)
print(10 * 6)
print(10 * 7)
print(10 * 8)
print(10 * 9)
print(10 * 10)

a = "10"
b = 10
int(a)
a = 10
print("type of a:",type(a))









