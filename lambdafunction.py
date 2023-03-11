
# def isAdult(age):
#     if age > 18:
#         return True
#     else:
#         return False

# print(isAdult(20))

# # Syntax of Lambda Function
# # lambda arguments: expression 

# # syntax when return type is boolean
# isAdultBoolean =  lambda age : age > 18 
# print(isAdultBoolean(20))   ## True


# # syntax when return type is other than boolean
# isAdultStr = lambda age : "Adult" if age > 18 else "Minor"
# print(isAdultStr(17))       ## Minor
# print(isAdultStr(27))       ## Adult
# print(isAdultStr(3))       ## Minor
# print(isAdultStr(45))       ## Adult
# print(isAdultStr(77))       ## Adult
# print(isAdultStr(10))       ## Minor



# print( (lambda age : "Adult" if age > 18 else "Minor")(10,20)) ## Minor

# listNumber  = [[10,1], [5,64],[1,98],[9,10]]
# listNumber.sort()
# print(listNumber)   ##[[1, 98], [5, 64], [9, 10], [10, 1]]


# listNumber  = [[10,1], [5,64],[1,98],[9,10]]
# listNumber.sort(key=lambda a : a[1])
# print(listNumber)

# listNumber  = [[10,1,30,40], [5,64],[1,98],[9,10]]
# listNumber.sort(key=lambda a : a[1])
# print(listNumber)   #[[10, 1, 30, 40], [9, 10], [5, 64], [1, 98]]

# listNumber  = [[10,1,30,40], [5,64],[1,98],[9,10]]
# listNumber.sort(key=lambda a : a[3])    ##IndexError: list index out of range
# print(listNumber)


#### =============================================================================

### Filter

# numberList  = [10,4,57,8,4,2,9]
# evens = []
# for item in numberList:
#     if item % 2 == 0 :
#         evens.append(item)

# print(evens)



# numberList  = [10,4,57,8,4,2,9] 
# evens = list(filter(lambda n : n % 2 == 0 , numberList))
# print(evens)


# numberList  = [10,4,57,8,4,2,9] 
# odds = list(filter(lambda n : n % 2 == 1 , numberList))
# print(odds)

# ### -----------------------------------------------------------


# numberList  = [10,4,57,8,4,2,9] 
# square = list(filter(lambda n : n * 2, numberList))
# print(square) ###[10, 4, 57, 8, 4, 2, 9]


### -----------------------------------------------------------



# numberList  = [10,4,57,8,4,2,9] 
# square = list(map(lambda n : n * n, numberList))
# print(square) ### [100, 16, 3249, 64, 16, 4, 81]

# ### --------------------------------------------------------

# numberList  = ['asdf','hello','credence','Never be overconfident','be confident', 'dont forget roots ever'] 
# square = list(map(lambda n : n.upper(), numberList))
# print(square) ### ['ASDF', 'HELLO', 'CREDENCE', 'NEVER BE OVERCONFIDENT', 'BE CONFIDENT', 'DONT FORGET ROOTS EVER']

# #### --------------------------------------------------------------------------
# from functools import reduce


# numberList  = [10,4,57,8,4,2,9] 
# add = reduce(lambda x,y : x + y, numberList )
# print(add)

# #### --------------------------------------------------------------------------



number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)



# ### 104359
# # print like below 
# # 1
# # 0
# # 4
# # 3
# # 5
# # 9

# aNumber = 104359
# reminder = aNumber % 10  ## => reminder 9
# print(reminder)     ## or make addition
# aNumber = aNumber // 10   ## number = 10435
# print(aNumber)

# ## or print in reverse

# #

# ##I want to add all digits from this number, it is not a string




















