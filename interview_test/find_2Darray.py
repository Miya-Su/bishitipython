#二维数组查找
def Find2D(array,target):
    x=len(array)-1
    y=len(array[0])-1
    z=0
    while x>=0 and z<=y:
        if array[x][y]==target:
            return True
        elif array[x][y]>target:
            y-=1
        else:
            x+=1
    return False

arrayA=[[1,2,8],[2,4,9],[4,7,10]]
Find2D(arrayA,3)



