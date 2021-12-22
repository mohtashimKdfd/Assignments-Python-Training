# Q1
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.maxlen=12
#     def push(self,data):
#         if len(self.arr)<self.maxlen:
#             self.arr.append(data)
#             # self.maxlen-=1
#             print("Pushed {} into stack".format(data))
#         else:
#             print("Over Flow Scene")
#     def pop(self):
#         if len(self.arr)>0:
#             x=self.arr.pop(-1)
#             self.maxlen-=1
#             print('Popped {} from Stack'.format(x))
#         else:
#             print("Under Flow Scene")
#     def printStack(self):
#         print(self.arr)
    
# St = Stack()
# for i in range(10,25):
#     St.push(i)
# St.printStack()

# for i in range(1,30):
#     St.pop()
# St.printStack()


# Q2


# def palindromicNumber(n):
#     if str(n)==str(n)[::-1]:
#         return True
#     return False
# print(palindromicNumber(55))
# arr=[]
# def printt(start,end):
#     for i in range(start,end):
#         if palindromicNumber(i)==True:
#             arr.append(i)
# printt(10, 999999)
# print(arr)

# def generator(start,end):  redo
#     while start !=end:
#         if str(start)==str(start)[::-1]:
#             yield(start)
        
#         start+=1
# for i in generator(10,99999):
#     print(i)

# Q3
# d={}
# for i in range(int(input("Enter the number of items:"))):
#     temp=list(input().split())
#     idd=int(temp[0])
#     num = int(temp[1])
#     quantity = int(temp[2])
#     ppu = int(temp[3])
#     if idd in d:
#         d[idd].append([num,quantity,ppu])
#     else:
#         d[idd]=[[num,quantity,ppu]]
# print(d)  # d[i]=[id num quan ppu  total]
# for i in d:
#     for j in range(len(d[i])):
#         d[i][j].append(d[i][j][2]*d[i][j][1])
# print("****Calculating the total amount for each order****")
# print(d)
# x=int(input("enter the min total: "))
# for i in d:
#     for j in range(len(d[i])):
#         if d[i][j][-1]>x:
#             print(i,end=":")
#             print(d[i][j][:-1])
#             print()

# Q4 


# def calculate_sum(arr):
#     return sum(arr)


# def calculate_sum(arry,n):
#     if n%2==0:
#         return "odd"
#     return sum(arry)

# def evenSum(arr):
#     s=0
#     for i in arr:
#         if i%2==0:
#             s+=i
#     return s
# def makeOdd(s):
#     s+=1
#     return s
# arr=list(map(int,input().split()))
# arry = list(map(int,input().split()))
# print(calculate_sum(arr))
# print(calculate_sum(arry,7))


# print(calculate_sum(arr))
# print(evenSum(arr))
# if evenSum(arr)%2==0:
#     print(makeOdd(evenSum(arr)))


#generators :>
# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(function):
#     greeting = function(input())
#     print(greeting)
# greet(shout)
# greet(whisper)

def makeOdd(arr):
    
    s=0
    for i in arr:
        if i%2==0:
            s+=i
        else:
            continue
    if s%2==0:
        s+=1
        return s
    else:
        return s

def calcEVEN(arr):
    s=0
    for i in arr:
        if i%2==0:
            s+=i
    return s

def calculateSUM(function):
    calc = function(list(map(int,input("Enter the array: ").split())))
    print(calc)
calculateSUM(calcEVEN)
calculateSUM(makeOdd)