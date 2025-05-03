# info = {"Carla" , 19 , False , 5.9 , 19}
# print(info)

# ujjwal = set()
# print(type(ujjwal))   

# ujjwal = {}
# print(type(ujjwal))

# for value in info:
    # print(value)

# Sets operator
# s = {1,2,5,6}
# s1 = {3,6,7}
# print(s.union(s1))
# print(s, s1)
# print(s.update(s1))
# s.update(s1)
# print(s, s1)
# Intersection
# cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}

# cities3 = cities1.union(cities2)
# print(cities3)
# intersection_update
# cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}

# cities3 = cities1.intersection(cities2)
# cities1.intersection_update(cities2)
# print(cities1)    

# Symmetric_difference  
# cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}

# cities3 =cities1.symmetric_difference(cities2)
# print(cities3)   
# cities1.symmetric_difference_update(cities2)   
# difference
# cities1 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
# cities3 = cities1.difference(cities2) 
# print(cities3)    

# isdisjoint() 
# cities1 = {"Tokyo" ,"Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}   
# print(cities1.isdisjoint(cities2)) 

# cities1 = {"Tokyo" ,"Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Bejing" , "Seoul" , "Kabul" , "Perth"}   
# print(cities1.isdisjoint(cities2))   

# cities1 = {"Tokyo" ,"Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}   
# print(cities1.issuperset(cities2))
 
# cities = {"Tokyo" ,"Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Seoul" , "Kabul"} 
# print(cities.issuperset(cities2))
# cities3 = {"Tokyo" , "Madrid" , "Delhi"}
# print(cities.issuperset(cities3)) 
# print(cities3.issubset(cities))    

# add()  
# cities = {"Tokyo" , "Madrid" , "Berlin" , "London"}
# cities.add("Perth")
# print(cities)   

# remove()/discard() 
# cities = {"Tokyo" , "Berlin" , "Madrid" , "Delhi"}
# cities.remove("Tokyo")  
# print(cities)
# discard()
# cities = {"Tokyo" , "Berlin" , "Madrid" , "Delhi"}
# cities.discard("Tokyo2")  
# print(cities)  

# pop()
# cities= {"Tokyo" , "Berlin", "Madrid" , "Delhi"} 
# item = cities.pop()
# print(cities) 
# print(item)   

# del()
# cities= {"Tokyo" , "Berlin", "Madrid" , "Delhi"} 
# del(cities)
# print(cities)    


# clear()
# cities= {"Tokyo" , "Berlin", "Madrid" , "Delhi"} 
# cities.clear()
# print(cities)    

# Check if item exist()
info = {"Carla" , "19" , "False" ,"5.9"}
if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is not present")