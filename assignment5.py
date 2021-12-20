# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class child(Shape):
#     def shape(self):
#         s=int(input('Enter The shape'))
#         if s=='traingle':
#             self.triangle()
#         elif s=='square':
#             self.square()

#     def triangle(self):
#         b=int(input())
#         h=int(input())
#         return 0.5*b*h
#     def rectangle(self):
#         l=int(input())
#         b=int(input())
#         return l*b
#     def square(self):
#         l=int(input())
#         return l*l

# # s = Shape()
# c=child()
# c.shape()

# q3

# Design a linked list that supports these ops:

# Adds an element at the end.
# Adds an element between the two elements.
# Deletes an element from the given key.
# Search an element from the given key.
# Display the complete linked list.
# Reverse the linked list.

class Node:
    def __init__(self,x):
        self.val=x
        self.next = None
class Linkedlist:
    def insert(self,head,data):
        if head is None:
            return Node(data)
        else:
            curr = head
            while curr.next:
                curr=curr.next
            curr.next = Node(data)
            return head
    def addBetween(self,head,st,en,data):
        if head is None:
            return 
        curr = head
        while curr is not None and curr.val!=st and curr.next.val!=en:
            print(curr.val)
            curr=curr.next
        x=Node(data)
        x.next = curr.next
        curr.next=x
        return head

    def prin(self,head):
        while head:
            print(head.val,end=">")
            head = head.next
    def delete(self,head,data):
        if head is None:
            return
        curr = head
        while curr.next.val != data:
            curr = curr.next
        curr.next=curr.next.next
        return head

    def reverse(self,head):
        curr=head
        prev=None
        while curr:
            nex = curr
            curr=curr.next
            nex.next=prev
            prev = nex
        return prev


ll=Linkedlist()
head = Node(0)
for i in range(1,10):
    x=ll.insert(head,i)
    x=x.next
ll.prin(head)
print()
ll.addBetween(head,4,5,500)
ll.prin(head)

print()

ll.delete(head,500)
ll.prin(head)

print()

curr = ll.reverse(head)
ll.prin(curr)