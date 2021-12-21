#date = 26/10/2021
#age = 19 years 5 months 20days

from datetime import datetime

class my_date:
    def __init__(self,s):
        self.x=s

    def giveAge(self):  #timedelta 
        givenS=self.x
        today = list(datetime.today().strftime('%d-%m-%Y').split('-'))
        birth=list(givenS.split('/'))
        birth=[int(x) for x in birth]
        today=[int(x) for x in today]
        age=[]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if birth[0]>today[0]:
            today[1]-=1
            today[0]+=days[birth[1]-1]
        if birth[1]>today[1]:
            today[2]-=1
            today[1]+=12
        age=[]
        for i in range(3):
            age.append(today[i]-birth[i])

        print(str(age[-1]) + ' years ' + str(age[-2])+ ' months and ' + str(age[-3]) + ' days')

        if age[-1]>50:
            print('Already 50')
        else:
            print('Turning 50 in: ',str(50-age[-1]) + " years " + str(age[-2]) + ' months ' + str(age[-3]) + ' days')


    def giveDOB(self):
        s = self.x
        dob = []
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(len(s)-1):
            if s[i].isdigit() and s[i+1].isdigit():
                dob.append(int(s[i]+s[i+1]))
            elif s[i].isdigit() and (((i==0 or i==len(s)-1)) or ((s[i-1]==" " or s[i-1].isalpha()) and (s[i+1]==" " or s[i+1].isalpha()))):
                dob.append(int(s[i]))


        today = list(datetime.today().strftime('%Y-%m-%d').split('-'))
        birth=[int(x) for x in dob]
        today=[int(x) for x in today]
        print(birth)
        print(today)
        if today[-1]<birth[-1]:
            today[1]-=1
            today[-1]+=days[birth[1]-1]

        if today[1]<birth[1]:
            today[0]-=1
            today[1]+=12
        print(today)
        dateofbirth =[]
        # if 
        for i in range(3):
            dateofbirth.append(today[i]-birth[i])

        print(str(dateofbirth[-1]) + '/' + str(dateofbirth[1]) + "/" + str(dateofbirth[0]))

# s=input()
# date = my_date(s)
# date.giveAge()