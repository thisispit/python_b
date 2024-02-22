""" if else if ladder """

a=100
b=200
c=300

if (a==100):
    if(b==200):
        if(c==300):
            print("a,b,c are true")
        else:
            print("condition is not matched for c")
    else:
        print("condition is not matched for b")
else:
    print("condition is not meet for a")
