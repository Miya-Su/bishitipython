#打印单链表
#创建链表，通过床架Node类来实现链表，利用类的属性引用来代替指针操作
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

def Createlist(n):
    if n<=0:
        return  False
    if n==1:
        return Node(1)
    else:
        root=Node(1)
        tmp=root
        for i in range(2,n+1):
            tmp.next=Node(i)
            tmp=tmp.next
    return root
    #打印列表
def printlist(head):
    p=head
    while p!=None:
        print(p.value)
        p=p.next
def f1(listnode):
    lists=[]
    while listnode:
        lists.append(listnode.value)
        listnode=listnode.next
    return lists[::-1]
# listnode=Createlist(6)
# print(f1(listnode))