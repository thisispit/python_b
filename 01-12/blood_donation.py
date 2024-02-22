z=int(input("Enter your age: "))
a=str(input("Do you have any disease or sugar ? (Please answer in yes or no) : "))
b=str(input("Enter your gender (Male or Female) : "))
c=float(input("Enter your weight in kg : "))
if(z>=18):
    if (a=="no" or a=="No" or a=="NO"):
            if (b=="Male" or b=="male"):
                if (c>=55):
                    print("You are eligible for Blood Donation.")
                else:
                    print("you aren't not eligible for Blood Donation.")
            elif (b=="Female" or b=="female"):
                if (c>=45):
                    print("You are eligible for Blood Donation.")
                else:
                    print("you aren't not eligible for Blood Donation.")
            else:
                print("you aren't not eligible for Blood Donation.")
    else:
        print("you aren't not eligible for Blood Donation.")
else:
    print("you are not eligible for blood donation")