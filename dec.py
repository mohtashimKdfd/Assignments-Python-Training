#Assignments
# Assinment 1 
#q1
# s=input()
# w=input()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# flag=0
# for i in w:
#     if i not in d or d[i]<=0:
#         flag=1
#         break
#     else:
#         d[i]-=1
# if flag==1:
#     print("Not Possible")#Assignments
# Assinment 1 
#q1
# s=input()
# w=input()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# flag=0
# for i in w:
#     if i not in d or d[i]<=0:
#         flag=1
#         break
#     else:
#         d[i]-=1
# if flag==1:
#     print("Not Possible")
# else:
#     print('Possiblity 100')


#q2
# s=input()
# s=s*5
# ans=[]
# d={}
# for i in range(len(s)):
#     # x=(i%5)+1
#     if s[i] not in d:
#         d[s[i]]=[s[i]]
#     else:
#         d[s[i]].append(s[i])
# for i in d:
#     print(i,end=" => ")
#     print(*d[i])

# Q4
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# n=int(input())
# for i in range(1,n+1):
#     print('* '*i)
# for i in range(n-1,0,-1):
#     print("* "*i)


# Assignment 2:
#q1
# arr = [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]
# output sceen
# Enter the number of tuples:4
# Tuple1 121
# Tuple2 125
# Tuple3 135
# Tuple4 478
# [('Tuple1', 121), ('Tuple2', 125), ('Tuple3', 135), ('Tuple4', 478)]
# ['Tuple1', 'Tuple2', 'Tuple3', 'Tuple4']
# [('Tuple1', 121), ('Tuple2', 125), ('Tuple3', 135), ('Tuple4', 478)]
# arr=[]
# for i in range(int(input('Enter the number of tuples:'))):
#     temp=list(input().split())
#     arr.append((temp[0],int(temp[1])))
# print(arr)
    
# ans=[]
# visited=[]
# for i in range (len(arr)):
#     if arr[i][0] not in visited:
#         ans.append(arr[i])
#         visited.append(arr[i][0])
# print(visited)
# print(ans)

#q2
# vote = list(map(input().split())
# arr=list(vote)
# arr=list(input().split())
# d={}
# for i in arr:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# n=0
# for i in d:
#     n=max(n,d[i])
# ans=[]
# for i in d:
#     if d[i]==n:
#         ans.append(i)
# if len(ans)==1:
#     print(ans[0])
# else:
#     ans.sort()
#     print(ans[0])

#Assignment 3

# def give(n):
#     ans=[]
#     for i in range(1,11):
#         ans.append(n*i)
#     return ans


# with open('table.txt','w') as f:
#     for i in range(1,21):
#         arr=give(i)
#         ans=[i,':',*arr]
#         # print(*ans)
#         # f.write(*ans)
#         for j in ans:
#             f.write(str(j))
#             f.write(' ')
#         f.write('\n')

# with open('table.txt','a') as f:
#     for i in range(21,41):
#         arr=give(i)
#         ans=[i,':',*arr]
#         # print(*ans)
#         # f.write(*ans)
#         for j in ans:
#             f.write(str(j))
#             f.write(' ')
#         f.write('\n')
# with open('table.txt','r') as f:
#     lines = f.readlines()
#     d={}
#     for line in lines:
#         if int(line[:2]) not in d:
#             d[int(line[:2])]=line[2:-2]
#     for i in d:
#         print(i,d[i])
#     # print(d)
# #using pickle to dump dict object
# import pickle
# pickle.dump(d,open('new.p','wb'))

# #taking user input and printing table for that input
# n=int(input("Enter the number:"))
# for i in d:
#     if int(i)==n:
#         print(d[i][3:])
#ouput screen
#Enter the number:37
# 37 74 111 148 185 222 259 #Assignments
# Assinment 1 
#q1
# s=input()
# w=input()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# flag=0
# for i in w:
#     if i not in d or d[i]<=0:
#         flag=1
#         break
#     else:
#         d[i]-=1
# if flag==1:
#     print("Not Possible")
# else:
#     print('Possiblity 100')


#q2
# s=input()
# s=s*5
# ans=[]
# d={}
# for i in range(len(s)):
#     # x=(i%5)+1
#     if s[i] not in d:
#         d[s[i]]=[s[i]]
#     else:
#         d[s[i]].append(s[i])
# for i in d:
#     print(i,end=" => ")
#     print(*d[i])

# Q4
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# n=int(input())
# for i in range(1,n+1):
#     print('* '*i)
# for i in range(n-1,0,-1):
#     print("* "*i)


# Assignment 2:
#q1
# arr = [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]
# output sceen
# Enter the number of tuples:4
# Tuple1 121
# Tuple2 125
# Tuple3 135
# Tuple4 478
# [('Tuple1', 121), ('Tuple2', 125), ('Tuple3', 135), ('Tuple4', 478)]
# ['Tuple1', 'Tuple2', 'Tuple3', 'Tuple4']
# [('Tuple1', 121), ('Tuple2', 125), ('Tuple3', 135), ('Tuple4', 478)]
# arr=[]
# for i in range(int(input('Enter the number of tuples:'))):
#     temp=list(input().split())
#     arr.append((temp[0],int(temp[1])))
# print(arr)
    
# ans=[]
# visited=[]
# for i in range (len(arr)):
#     if arr[i][0] not in visited:
#         ans.append(arr[i])
#         visited.append(arr[i][0])
# print(visited)
# print(ans)

#q2
# vote = list(map(input().split())
# arr=list(vote)
# arr=list(input().split())
# d={}
# for i in arr:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# n=0
# for i in d:
#     n=max(n,d[i])
# ans=[]
# for i in d:
#     if d[i]==n:
#         ans.append(i)
# if len(ans)==1:
#     print(ans[0])
# else:
#     ans.sort()
#     print(ans[0])

#Assignment 3

# def give(n):
#     ans=[]
#     for i in range(1,11):
#         ans.append(n*i)
#     return ans


# with open('table.txt','w') as f:
#     for i in range(1,21):
#         arr=give(i)
#         ans=[i,':',*arr]
#         # print(*ans)
#         # f.write(*ans)
#         for j in ans:
#             f.write(str(j))
#             f.write(' ')
#         f.write('\n')

# with open('table.txt','a') as f:
#     for i in range(21,41):
#         arr=give(i)
#         ans=[i,':',*arr]
#         # print(*ans)
#         # f.write(*ans)
#         for j in ans:
#             f.write(str(j))
#             f.write(' ')
#         f.write('\n')
# with open('table.txt','r') as f:
#     lines = f.readlines()
#     d={}
#     for line in lines:
#         if int(line[:2]) not in d:
#             d[int(line[:2])]=line[2:-2]
#     for i in d:
#         print(i,d[i])
#     # print(d)
# #using pickle to dump dict object
# import pickle
# pickle.dump(d,open('new.p','wb'))

# #taking user input and printing table for that input
# n=int(input("Enter the number:"))
# for i in d:
#     if int(i)==n:
#         print(d[i][3:])
#ouput screen
#Enter the number:37
# 37 74 111 148 185 222 259 296 333 370 


# Zipp Practice
# arr=[1,2,3,5]
# name = ['Mk','mk2','Mk3','Mk4']
# d={i:j for (i,j) in (zip(arr,name))}
# print(d)
# ans=[]
# d={}
# for i in range(len(s)):
#     # x=(i%5)+1
#     if s[i] not in d:
#         d[s[i]]=[s[i]]
#     else:
#         d[s[i]].append(s[i])
# for i in d:
#     print(i,end=" => ")
#     print(*d[i])

# Q4
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# n=int(input())
# for i in range(1,n+1):
#     print('* '*i)
# for i in range(n-1,0,-1):
#     print("* "*i)


# Assignment 2:
#q1
# arr = [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]
# output sceen
# Enter the number of tuples:4
# Tuple1 121
# Tuple2 125
# Tuple3 135
# Tuple4 478
# [('Tuple1', 121), ('Tuple2', 125), ('Tuple3', 135), ('Tuple4', 478)]
# ['Tuple1', 'Tuple2', 'Tuple3', 'Tuple4']
# [('Tuple1', 121), ('Tuple2', 125), ('Tuple3', 135), ('Tuple4', 478)]
# arr=[]
# for i in range(int(input('Enter the number of tuples:'))):
#     temp=list(input().split())
#     arr.append((temp[0],int(temp[1])))
# print(arr)
    
# ans=[]
# visited=[]
# for i in range (len(arr)):
#     if arr[i][0] not in visited:
#         ans.append(arr[i])
#         visited.append(arr[i][0])
# print(visited)
# print(ans)

#q2
# vote = list(map(input().split())
# arr=list(vote)
# arr=list(input().split())
# d={}
# for i in arr:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# n=0
# for i in d:
#     n=max(n,d[i])
# ans=[]
# for i in d:
#     if d[i]==n:
#         ans.append(i)
# if len(ans)==1:
#     print(ans[0])
# else:
#     ans.sort()
#     print(ans[0])

#Assignment 3

# def give(n):
#     ans=[]
#     for i in range(1,11):
#         ans.append(n*i)
#     return ans


# with open('table.txt','w') as f:
#     for i in range(1,21):
#         arr=give(i)
#         ans=[i,':',*arr]
#         # print(*ans)
#         # f.write(*ans)
#         for j in ans:
#             f.write(str(j))
#             f.write(' ')
#         f.write('\n')

# with open('table.txt','a') as f:
#     for i in range(21,41):
#         arr=give(i)
#         ans=[i,':',*arr]
#         # print(*ans)
#         # f.write(*ans)
#         for j in ans:
#             f.write(str(j))
#             f.write(' ')
#         f.write('\n')
# with open('table.txt','r') as f:
#     lines = f.readlines()
#     d={}
#     for line in lines:
#         if int(line[:2]) not in d:
#             d[int(line[:2])]=line[2:-2]
#     for i in d:
#         print(i,d[i])
#     # print(d)
# #using pickle to dump dict object
# import pickle
# pickle.dump(d,open('new.p','wb'))

# #taking user input and printing table for that input
# n=int(input("Enter the number:"))
# for i in d:
#     if int(i)==n:
#         print(d[i][3:])
#ouput screen
#Enter the number:37
# 37 74 111 148 185 222 259 296 333 370 


# Zipp Practice
# arr=[1,2,3,5]
# name = ['Mk','mk2','Mk3','Mk4']
# d={i:j for (i,j) in (zip(arr,name))}
# print(d)

