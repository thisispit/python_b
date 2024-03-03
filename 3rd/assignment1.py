""" condition for voitng 
1 age greater than 18
2 nationality indian
 """



age=int(input("enter your age: "))
nat=str(input("enter your natinality: "))
if (age>=18):
    if (nat==("indian" or "india" or "India" or "Indian")):
        print("you are eligible for voting")
    else:
        print("your nationality is not iandian")
else:
    print("you are not 18 above")





