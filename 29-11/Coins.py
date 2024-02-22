""" IMP
    WAP for change calculation with respect to total amount  """


a=float(input("enter the value of currency"))

five_hundred_notes = a // 500
a=a%500
two_hundred_notes = a // 200
a=a%200
one_hundred_notes = a // 100
a=a%100 

print("Notes Change:")
print("Five Hundred Notes:", five_hundred_notes)
print("Two Hundred Notes:", two_hundred_notes)
print("One Hundred Notes:", one_hundred_notes)
print("Remaining Amount:", a)


# amount = float(input("Enter currency amount: "))

# remaining_amount = amount

# five_hundred_notes = remaining_amount // 500
# remaining_amount = remaining_amount % 500

# two_hundred_notes = remaining_amount // 200
# remaining_amount = remaining_amount % 200

# one_hundred_notes = remaining_amount // 100 
# remaining_amount = remaining_amount % 100

# print("Notes Change:") 
# print("Five Hundred Notes:", five_hundred_notes)
# print("Two Hundred Notes:", two_hundred_notes)
# print("One Hundred Notes:", one_hundred_notes)
# print("Remaining Amount:", remaining_amount)
