
#重建二叉树
#输入二叉树的前序和中序结果（不含重复数字），重建该二叉树
class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right

def construct_tree(pre_order,mid_order):
        if len(pre_order)==0 or len(mid_order)==0:
            return Node
        root_data=pre_order[0]
        for i in range(0,len(mid_order)):
            if mid_order[i]==root_data:
                break
        left=construct_tree(pre_order[1:1+i],mid_order[:i])
        right=construct_tree(pre_order[1+i:],mid_order[i+1:])
        return Node(root_data,left,right)
        
if __name__=='__main__':
        pre_ordef=[1,2,4,7,3,5,6,8]
        mid_order=[4,7,2,1,5,3,8,6]
        root=construct_tree(pre_ordef,mid_order)