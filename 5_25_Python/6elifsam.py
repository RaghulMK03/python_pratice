#2 input a,b from user
#get i/p add/sub /mul/div
# 
 
a= int(input("num1:"))
b=int(input("num2:"))

user= input("add/sub/mul/div ?:")

if(user=="add"):
    print("Value: ",a+b)
elif(user=="sub"):
    print("Value :",a-b)
elif(user=="sub"):
    print("Value :",a*b)
elif(user=="div"):
    print("Value :",a/b)
else:
    print(" invalid Operation :")

