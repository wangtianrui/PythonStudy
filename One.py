print("Hello World")
message = 'Hello "1" World'
print(message)
message = "hello 'python' world"
print(message)
message = message.title()
print(message)
message = message.upper()
print(message)
message = message.lower()
print(message)

print("----------------------------------------------")

message2 = "I will print"
messageAdd = message2 + " " + message
print(messageAdd)

print("Languages:\n\tPython\n\tC\n\tJavaScript")
print("----------------------------------------------")

message = '    python    '
print(message)
print(message.rstrip())  # 去掉后面的空格
print(message.lstrip())  # 去掉前面的空格
print(message.strip())  # 去掉前后的空格

number = 23
# message = message + number  错误！TypeError: Can't convert 'int' object to str implicitly
# 必须先把int数据类型转换成string才能进行"+"
message = message + str(number)
print(message)

