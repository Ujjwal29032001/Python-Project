# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#         print("Average is: ", sum/len(numbers))
# average(5,6,7,1)                
# Default Argument
# def average(a=9 , b=1):
#     print("The average is ", (a+b)/2)
# # average(1 ,6)    
# average(b=9)    

# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello," ,fname, mname, lname)  
# name("Ujjwal")  
 
# Keyword Argument    
# def name(fname , mname , lname):
#     print("Hello," , fname , mname, lname)
# name(mname= "Ujjwal", fname = "Shivam" , lname="Shinu")

# def average(a=9 , b=1):
#      print("The average is ", (a+b)/2)    
# average(b=9 , a=21)      
# Required arguments    
# def name(fname, mname, lname):
#     print("Hello," , fname,lname,mname)  
# name("Ujjwal" , "Shivam" , "Lola")    
    
# variable-Length argument

# Arbiatry argument

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i 
#     print("Average is: ", sum / len(numbers))   
# average(5,6,7,11)


#  Keyword-Arbiatry argument

# def name(**name):
#     print(type(name))
#     print("Hello", name["fname"], name["mname"], name["lname"])
# name(mname = "Jaimata di", lname = "Kalkamata" , fname="JamuvayaMata")

# return statement

def average(*numbers):
    #  print(type(numbers))
     sum = 0
     for i in numbers:
         sum = sum + i 
    #  print("Average is: ", sum / len(numbers))  
         return 7
        #  return sum / len(numbers) 
c = average(5,6,7,1)
print(c)

    


  