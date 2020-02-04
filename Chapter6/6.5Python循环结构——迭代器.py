list=['a','b','c']
ls= iter(list)    # 创建迭代器对象
for i in list:
	print(next(ls))
