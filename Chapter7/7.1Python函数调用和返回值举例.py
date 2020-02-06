def funcPara(m):   
    n = 5 + m
    s = 3 * n
    t = s - 6
    q = "Hello"*3
    return n,s,t,q

if __name__ == '__main__':
	#调用funcPara(m)函数并且输入的参数m的值为10，返回4个变量a,b,c,d
	#a,b,c,d的顺序和funcPara(m)函数返回值的顺序n,s,t,q一一对应
	a,b,c,d = funcPara(10)
	#变量a对应funcPara(m)函数里面的n，执行n = 5 + m的计算
	print("a=",a) 
	#变量b对应funcPara(m)函数里面的s，执行s = 3 * n的计算
	print("b=",b)
	#变量c对应funcPara(m)函数里面的t，执行t = s - 6的计算
	print("c=",c)
	#变量d对应funcPara(m)函数里面的q，执行q = "Hello"*3的计算
	print("d=",d)	