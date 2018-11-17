
#用两个栈来实现一个队列，完成队列的pop和push操作
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    #入队
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

#
if __name__=='__main__':
    solution=Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    print(solution.pop())
    print(solution.pop())
    print(solution.pop())