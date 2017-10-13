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
