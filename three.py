'''
***************函数***************
'''


# 注意python没有方法重载
def descripe_pet1(animal, pet_name):
    print(animal + "'s name is " + pet_name)


def descripe_pet(animal):
    print("only get " + animal)


descripe_pet("dog")
descripe_pet1("dog", "wang")


# 提高鲁棒性
def print_name(first, last, middle=""):
    print(first + " " + middle + " " + last)


print_name("wang", "rui", "tian")
print_name("jin", "yi")


# 返回一个字典
def get_people(name, age, sex):
    people = {
        "name": name,
        "sex": sex,
        "age": age
    }
    return people


print(get_people("wang", 19, 1))

people = ['wang', 'chen', 'jiang', 'he']


def print_models(list):
    list.append("li")


print_models(people[:])  # ['wang', 'chen', 'jiang', 'he'] 无法被修改
print(people)
print_models(people)  # ['wang', 'chen', 'jiang', 'he', 'li']可以被修改
print(people)

#接受任意数量的实参
#toppings是一个元组
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
