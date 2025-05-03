# dic = {
#     "Ujjwal" : "Human-Being" ,
#     "Spoon"  : "Object"
# }
# print(dic["Ujjwal"])  

# dic = {
#     344 : "UTTAm" ,
#     56  : "Pintu",
#     678  : "Dimpu",
#     567  : "Raju"
# }    

# print(dic[567])   

# info = {'name' : 'Shivam', 'age' : 19 , 'eligible' : True }
# print(info)
# print(info['name'])
# print(info.get('eligible'))
# print(info['name2'])
# print(info.get('name2'))   
# print(info.keys())
# print(info.values())  


# for key in info.keys():
#     print(info[key])  
# for key in info.keys():
#     print(f"The value corresponding to the key {key} is {info[key]} ")  

# info = {'name' : 'Shivam', 'age' : 19 , 'eligible' : True }
# print(info.items())
# for key, value in info.items():
    #   print(f"The value corresponding to the key {key} is {info[value]} ")  

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}  
ep2 = {222: 67 , 566: 90} 
# ep1.update(ep2)  
# print(ep1)  
# clear()
# ep1.clear()  
# ep1.pop(122)
ep1.popitem()
# del ep1 show error
del ep1[123]
print(ep1)