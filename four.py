'''
***************类***************
'''


class Dog():
    '''不能重载
    def __init__(self, name, age):
        self.name = name
        self.age = age
    '''

    def __init__(self, name):
        self.name = name
        self.love = 'chen'  # 设定默认值

    def sit(self):
        print(self.name + " is sitting.")


my_dog = Dog("wang")
my_dog.sit()
my_dog.name = "wang tian"
my_dog.sit()


class EattingDog(Dog):
    def __int__(self, name):
        super().__init__(name)
        self.age = 10


    def printf(self):
        print(self.name + " is eatting")


eatting_dog = EattingDog("wang")
eatting_dog.printf()
print(eatting_dog.love)
