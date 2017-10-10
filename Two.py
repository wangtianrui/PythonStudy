bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1]) #返回最后一个
print(bicycles[-2])#返回倒数第二个
print(bicycles[-3])#返回倒数第三个


print("--------------------")
'''
***************动态改变列表***************
'''
print("Original:",bicycles)

bicycles.append('Giant') #在尾部加一个
print("append:",bicycles)

bicycles.insert(2,'Fenghuang') #在位置2处增加一个元素
print("insert:",bicycles)

del bicycles[1]  #删除位置1的元素
print("del:",bicycles)

the_last_element = bicycles.pop() #弹出最后一个元素（删除后返回该元素）,“栈抛出”
print("pop:",the_last_element)
print("after pop:",bicycles)

poped_element = bicycles.pop(2) #弹出任意位子元素
print("pop2:",poped_element)
print("after pop2:",bicycles)

bicycles.remove('Fenghuang') #删除第一个出现的该变量，无返回值
print("remove:",bicycles)
deleted_element = 'specialized'
bicycles.remove(deleted_element)
print("remove:",bicycles)
print("I deleted " + deleted_element) #注意思想，这样可以暂时保存删除的变量


print('--------------------')
'''
***************列表的顺序操作***************
'''
cars = ["bmw","audi","benz","toyota","Subaru"]
print("original:",cars)

cars.sort() #排序，并且无法变回以前的顺序
print("sort:",cars)

cars.sort(reverse=True) #倒序
print("reverse sort:",cars)

cars = ["bmw","audi","benz","toyota","Subaru"]
print("original:",cars)
cars_sort= sorted(cars) #此方法是将参数列表排序后返回给新的变量，原列表不变
print("after sorted the original:",cars,"\nthe return by sorted():",cars_sort)

print("original:",cars)
cars.reverse() #倒序，但是不会排序！
print("reverse:",cars)

print("len:",len(cars)) #得到列表长度

print('--------------------')

'''
***************列表的其他操作***************
'''
singers = ["初音未来","林俊杰","reol","薛之谦"]
print("original:",singers)

#顺序循环遍历
for singer in singers:
    print("顺序遍历：",singer)
    singer = singer + "No.1"
    print("将当前元素'singer'增加一个字符串",singer,"\n")
print("循环中操作的不是原列表的元素：",singers)

