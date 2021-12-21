from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        print("Area")
class child(Shape):
    def area(self):
        super().area()
        print("HElll yeah")
    def shape(self):
        s=input('Enter The shape:')
        if s=='traingle':
            self.triangle()
        elif s=='square':
            self.square()
        elif s=='rectangle':
            self.rectangle()

    def triangle(self):
        b=int(input())
        h=int(input())
        print(0.5*b*h)
    def rectangle(self):
        l=int(input())
        b=int(input())
        print(l*b)
    def square(self):
        l=int(input())
        print(l*l)

# s = Shape()
c=child()
c.area()
c.shape()

# q3

# Design a linked list that supports these ops:

# Adds an element at the end.
# Adds an element between the two elements.
# Deletes an element from the given key.
# Search an element from the given key.
# Display the complete linked list.
# Reverse the linked list.

# class Node:
#     def __init__(self,x):
#         self.val=x
#         self.next = None
# class Linkedlist:
#     def insert(self,head,data):
#         if head is None:
#             return Node(data)
#         else:
#             curr = head
#             while curr.next:
#                 curr=curr.next
#             curr.next = Node(data)
#             return head
#     def addBetween(self,head,st,en,data):
#         if head is None:
#             return 
#         curr = head
#         while curr is not None and curr.val!=st and curr.next.val!=en:
#             print(curr.val)
#             curr=curr.next
#         x=Node(data)
#         x.next = curr.next
#         curr.next=xreturn 
#     def prin(self,head):
#         while head:
#             print(head.val,end=">")
#             head = head.next
#     def delete(self,head,data):
#         if head is None:
#             return
#         curr = head
#         while curr.next.val != data:
#             curr = curr.next
#         curr.next=curr.next.next
#         return head

#     # 1>2>3>None
#     # none<1<2<3
#     # none<1

#     def reverse(self,head):
#         curr=head
#         prev=None
#         while curr:
#             nex = curr
#             curr=curr.next
#             nex.next=prev
#             prev = nex
#         return prev


# ll=Linkedlist()
# head = Node(0)
# for i in range(1,10):
#     x=ll.insert(head,i)
#     x=x.next
# ll.prin(head)
# print()
# ll.addBetween(head,4,5,500)
# ll.prin(head)

# print()

# ll.delete(head,500)
# ll.prin(head)

# print()

# curr = ll.reverse(head)
# ll.prin(curr)

# class Car:
#     def __init__(self,speed,regprice,clr):
#         self.Speed = speed
#         self.regularPrice = regprice
#         self.color = clr
#     def doublegetSalePrice(self):
#         return self.regularPrice

# class Truck(Car):
#     def __init__(self, speed,regprice,clr,wt):
#         self.weight = wt
#         # self.regularPrice=super().regularPrice
#         Car.__init__(self,speed,regprice,clr)
        
#     def op(self):
#         if self.weight>2000:
#             self.regularPrice*=0.9
    


# class Ford(Car):
#     def __init__(self,speed,regprice,clr,mfgdiscount):
#         self.Manufacturer_discount = mfgdiscount
#         Car.__init__(self,speed,regprice,clr)        
#     def op(self):
#         self.regularPrice-=self.Manufacturer_discount

# class Sedan(Car):
#     def __init__(self,speed,regprice,clr,lengthh):
#         self.length = lengthh
#         Car.__init__(self,speed,regprice,clr)

#     def op(self):
#         if self.length>20:
#             self.regularPrice*=0.95
#         else:
#             self.regularPrice*=0.9

# Car(20,10000,'B')
# T = Truck(20,40000,'B',20000)
# T.op()
# print(T.doublegetSalePrice())

# S=Sedan(20,10000,'B',30)
# S.op()
# print(S.doublegetSalePrice())
# F=Ford(20,20000,'B',100)
# F.op()
# print(F.doublegetSalePrice())