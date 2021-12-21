from datetime import datetime, timedelta
class my_date:
    def __init__(self,s):
        self.time = s
    
    def getAge(self):
        today = datetime.now()
        s=list(input().split('/'))
        s=[int(x) for x in s]
        d=s[0]
        d+=(s[-1])*365
        d+=s[1]*30
        print(d)
        print(today-timedelta(days=d))