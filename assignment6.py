# Q1
# class Stack:
#     def __init__(self):
#         self.arr=[]
#         self.maxlen=12
#     def push(self,data):
#         if len(self.arr)<self.maxlen:
#             self.arr.append(data)
#             self.maxlen+=1
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
# for i in range(10,20):
#     St.push(i)
# St.printStack()

# for i in range(12,16):
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

# def generator(start,end):
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
# print(d)
# for i in d:
#     for j in range(len(d[i])):
#         d[i][j].append(d[i][j][2]*d[i][j][1] *d[i][j][0])
# print("****Calculating the total amount for each order****")
# print(d)
# x=int(input("enter the min quantity: "))
# for i in d:
#     for j in range(len(d[i])):
#         if d[i][j][-1]>x:
#             print(i,end=":")
#             print(d[i][j])
#             print()

# Q4 


# def calculate_sum(arr):
#     return sum(arr)

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
# print(calculate_sum(arr))
# print(evenSum(arr))
# if evenSum(arr)%2==0:
#     print(makeOdd(evenSum(arr)))
