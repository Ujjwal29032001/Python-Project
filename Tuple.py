# tuple = (1,5,6,72,342, "Green" , True)
#print(type(tuple),tuple) 
#print(len(tuple), tuple)
#print(tuple[0])
#print(tuple[-1])
#print(tuple[2])

# print(type(tuple),tuple)
# if 3421 in tuple:
    # print("Yes 342 is present in this tuple")
# else:
    # print("No this is not present")    

# tuple2 = tuple[1:4]
# print(tuple2)    

# Manipulating Tuples
countries = ("spain" , "Turkey", "England", "South Korea", "Argentina")  
temp = list(countries)
temp.append("France")
temp.pop(3) 
temp[2] = "Singapore"
countries = tuple(temp)
print(countries)

countries = ("South Korea", "Australia" , "USA", "Portugal", "Canada")
countries2 = ("China" , "Mongolia" , "Vietnam")
SouthEastAsia = countries + countries2
print(SouthEastAsia)    
Tuple1 = (0,1,2,3,2,3,1,3,2,3)   
res = Tuple1.count(3)
print("Count of 3 in Tuple1 is: ", res)

Tuple2 = (0,1,2,3,2,31,1,3,2,3)   
# res = Tuple2.index(311)
# res = Tuple2.index(3,4,8)
res = len(Tuple2)
print("First occurence of 3 is:", res)