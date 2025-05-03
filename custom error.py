# a = int(input("Enter any value between 5 and 9"))
# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")
 
a = input("Enter any value between 5 and 9: ")
if (a== "quit"):
    print("ohk")
elif(int(a)<5 or int(a)>9):
    raise ValueError("The Number should be  between 5 and 9")



        