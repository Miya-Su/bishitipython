
#数组的旋转（把数组最开始的若干个元素搬到数组的末尾）
def minNumberInRotateArray(rotateArray):
    left=0
    right=len(rotateArray)-1
    mid=0
    while rotateArray[left]>=rotateArray[right]:
        if right-left==1:
            mid=right
            break
        mid=left+int((right-left)/2)

        if rotateArray[left]==rotateArray[mid] and rotateArray[right]==rotateArray[mid]:
            return minInorder(rotateArray,left,right)
        if rotateArray[mid]>=rotateArray[left]:
            left=mid
        elif rotateArray[mid]<rotateArray[right]:
            right=mid
    return rotateArray[mid]

def minInorder(rotateArray,left,right):
    minNum=rotateArray[left]
    length=right-left
    for i in range(length):
        if rotateArray[left+i]<minNum:
            minNum =rotateArray[left+i]
    return minNum

if __name__=='__main__':
    array=[5,6,7,9,2,4]
    # print(minNumberInRotateArray(array))