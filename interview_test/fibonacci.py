

#斐波那契数列(从第三项开始，每个数的值为前两个数之和,输入n，输出斐波那契第n项）
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        list=[0,1]
        while len(list)<=n:
            list.append(list[-1]+list[-2])
        return list[-1]

# print(Fibonacci(8))