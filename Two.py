bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])  # 返回最后一个
print(bicycles[-2])  # 返回倒数第二个
print(bicycles[-3])  # 返回倒数第三个

print("--------------------")
'''
***************动态改变列表***************
'''
print("Original:", bicycles)

bicycles.append('Giant')  # 在尾部加一个
print("append:", bicycles)

bicycles.insert(2, 'Fenghuang')  # 在位置2处增加一个元素
print("insert:", bicycles)

del bicycles[1]  # 删除位置1的元素
print("del:", bicycles)

the_last_element = bicycles.pop()  # 弹出最后一个元素（删除后返回该元素）,“栈抛出”
print("pop:", the_last_element)
print("after pop:", bicycles)

poped_element = bicycles.pop(2)  # 弹出任意位子元素
print("pop2:", poped_element)
print("after pop2:", bicycles)

bicycles.remove('Fenghuang')  # 删除第一个出现的该变量，无返回值
print("remove:", bicycles)
deleted_element = 'specialized'
bicycles.remove(deleted_element)
print("remove:", bicycles)
print("I deleted " + deleted_element)  # 注意思想，这样可以暂时保存删除的变量

print('--------------------')
'''
***************列表的顺序操作***************
'''
cars = ["bmw", "audi", "benz", "toyota", "Subaru"]
print("original:", cars)

cars.sort()  # 排序，并且无法变回以前的顺序
print("sort:", cars)

cars.sort(reverse=True)  # 倒序
print("reverse sort:", cars)

cars = ["bmw", "audi", "benz", "toyota", "Subaru"]
print("original:", cars)
cars_sort = sorted(cars)  # 此方法是将参数列表排序后返回给新的变量，原列表不变
print("after sorted the original:", cars, "\nthe return by sorted():", cars_sort)

print("original:", cars)
cars.reverse()  # 倒序，但是不会排序！
print("reverse:", cars)

print("len:", len(cars))  # 得到列表长度

print('--------------------')

'''
***************列表的其他操作***************
'''
singers = ["初音未来", "林俊杰", "reol", "薛之谦"]
print("original:", singers)

# 顺序循环遍历
for singer in singers:
    print("顺序遍历：", singer)
    singer = singer + "No.1"
    print("将当前元素'singer'增加一个字符串", singer, "\n")
print("循环中操作的不是原列表的元素：", singers)

print('--------------------')

'''
***************数值列表***************
'''
for value in range(1, 5):
    print(value)

rangetest = range(1, 5)
print(rangetest)
rangetest = list(range(5))
print(rangetest)
squares = []
for value in range(1, 11, 2):
    squares.append(value ** 2)
print(squares)
'''
***************列表的切片***************
'''
foods = ['pizza', 'falafel', 'cake']
my_foods = foods[2:]  # 2以后的
print(my_foods)
my_foods = foods[:-1]
print(my_foods)
my_foods = foods[:]  # 列表赋值必须[:]
print(my_foods)

'''
***************元组***************
'''
image = (1024, 728)  # 元组元素无法单独修改
print(image[0])
print(image[1])
# image[0] = 100   #错误
image = (100, 728)  # 正确
print(image)

#遍历元组
for i in image:
    print(i)

'''
***************if语句***************
'''


def checkAnswer(answer):
    if 1 == answer:
        print("answer is 1")
    elif (2 < answer) and (answer < 5):  # and和or关联词
        print('answer is betten 2 and 5')
    else:
        print("answer is (,1)||[5,)||2")


checkAnswer(0)
checkAnswer(1)
checkAnswer(2)
checkAnswer(4)

names = ["wang", "chen", "bao", "jiang"]
name1 = "wang"
name2 = "tang"
if name1 not in names:
    print("wang dont exist")
else:
    print("wang exist")
if name2 in names:
    print("tang exist")
else:
    print("tang not exist")

names = []
if names:
    print("列表不为空")
else:
    print("列表是空的")

'''
***************字典***************
'''
car = {
    'color': "blue",
    "money": 20000
}
print(car['money'])
car['color'] = 'red'
print(car['color'])
car = {}
car['name'] = "benz"
car["type"] = "bicycle"
print(car)
del car['name']
print(car)

# 遍历字典
people = {
    "language": 'chinese',
    "age": 19,
    "major": "computer",
    "class": 16070941
}
# 字典遍历
for key, value in people.items():
    print(key, value)
num = people["age"] + 1
str = str(num) + "1"
print(str)
# 遍历键
for key in people.keys():
    print(key)
# 遍历值
for value in people.values():
    print(value)
print("-------------------------")
# 遍历前排序 (注意int不能和string比较，所以排序value会报错)
for key in sorted(people.keys()):
    print(key)

# 嵌套使用

# 列表中放字典
peoples = []
for i in range(1, 6):
    peoples.append(people)
print(peoples[:])

# 字典中放列表
songs = ["song1", "song2", "song3"]
person = {
    "can_sing_song": songs,
    "age": 20,
    "name": 'jinyi'
}
print(person)
print(person['can_sing_song'][2])

# 字典中放字典
classes = {
    "class_name": "wulianwang",
    "classmate": person
}
print(classes)
print(classes["classmate"]['can_sing_song'][2])

'''
***************input和while循环***************


message = input("输入:")
print("输入的是:" + message)

while message != "wang":
    message = input()
    print(message)
'''

