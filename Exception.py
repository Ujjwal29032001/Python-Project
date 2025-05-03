# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")  
# try:
    # for i in range(1, 11):
        # print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
    # print("e")        
    # print("Sorry Some Error")        
    # print("Invalid Input")        
    
# print("Some Imp lines of Code")
# print("End of program")       
# try:
#     num = int(input("Enter an integer: "))    
#     a = [6, 3]
#     print(a[num]) 
# except ValueError:
#     print("Number entered is not an integer.")   
# except IndexError:
#     print("Index Error")    

# Finally Keyword   
# try:
#     l = [1,5,6,7]
#     i = int(input("Enter the index: "))
#     print(l[i]) 
# except:
#     print("Some error Occured")
# finally:
#     print("I am executed")   

# try:
    #    l = [1,5,6,7]
    #    i = int(input("Enter the index: ")) 
    #    print(l[i])
       
# except:    
        # print("Some error occured")   
        
# finally:
    #  print("I am executed")   
   

def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1  
    except:
        print("some error occured")  
        return 0  
    finally:
        print("I am always executed")   

x = func1()
print(x)        