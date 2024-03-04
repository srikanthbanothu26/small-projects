#Create a simple command line calculator application. This application should prompt the user for three inputs. 
#The first and second inputs should be numbers,
# while the third input should specify the operation to perform on these numbers (e.g., addition, subtraction, multiplication, division).
# Once the operation is completed,
#the application should prompt the user for inputs again, allowing for continuouscalculations.
while True:
       
       num=input("enter two numbers:").split(",")
       (a,b)=[int(item) for item in num]
       oper=input("enter operation")

       if oper=="+":
            print(a+b)
       elif oper=="-":
            print(a-b)
       elif oper=="*":
            print(a*b)
       elif oper=="/":
         print(a/b)
       else:
         print("quit")
         break
