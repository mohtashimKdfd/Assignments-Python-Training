import date_op
s=input()
date = date_op.my_date(s)

#could have used a separate function to check the input string but tried a short cut :p
# if len(s)>10:
date.giveAge()
# else:
#     date.giveDOB()