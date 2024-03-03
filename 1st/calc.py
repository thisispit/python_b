a = int(input("enter value for a="))
b = int(input("enter value for b="))
i = int(input("Press 1 for addition \nPress 2 for substraction \nPress 3 for multiplication \nPress 4 for Division\n"))

if (i==1):
    print(f"addition= {a+b}")
elif (i==2): 
    print(f"substraction= {a-b}")  
elif (i==3):
    print(f"multiplication= {a*b}")
elif (i==4):
    print(f"Division= {a/b}")
else: 
    print("invalid input")