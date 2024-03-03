# def positive_neg():
#     a=int(input())
#     if(a>0):
#         print("no is +ve ")
#     else:
#         print("no is -ve ")

# positive_neg()


a=int(input("Enter a: "))
b=int(input("Enter b: "))
i=int(input("Press 1 for addition \nPress 2 for substraction \nPress 3 for multiplication \nPress 4 for division \nPress 5 for Even or Odd \n "))

def add():
    if(i==1):
        print("Addition: " ,a+b)

def sub():
    if(i==2):
        print("Substraction: " ,a-b)

def mul():
    if(i==3):
        print("Multiplication: " ,a*b)

def div():
    if(i==4):
        print("Division: " ,a/b)

def greater_less():
    if(i==5):
        if(a>b):
            print(a, "is gratest")
        else:
            print(b, "is greatest")


# def even_odd():
#     if(i==6):
#         if(a%2==0):
#             if(b%2==0):
#                 print("M" ,a*b)


add()
sub()
mul()
div()
greater_less()