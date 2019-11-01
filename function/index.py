# print(
#     int(3),  # 3
#     int(3.14),  # 3
#     int(3.50),  # 3
#     int(3.65),  # 3
#     int('3'),  # 3
#     # int('3.14'),  # ValueError: invalid literal for int() with base 10: '3.14'
#     # int('abc'),  # ValueError: invalid literal for int() with base 10: 'abc'
# )
# print(
#     float(3),  # 3.0
#     float(3.14),  # 3.14
#     float(3.50),  # 3.5
#     float(3.65),  # 3.65
#     float('3'),  # 3.0
#     float('3.0'),  # 3.0
#     # float('abc'),  # ValueError: could not convert string to float: 'abc'
# )
# print(
#     str(3),  # 3
#     str(3.0),  # 3.0
#     str(3.14),  # 3.14
#     str('3'),  # 3
#     str('3.0'),  # 3.0
#     str('abc'),  # abc
# )

# print(
#     bool(1),  # True
#     bool('1'),  # True
#     bool(0),  # False
#     bool('0'),  # True
#     bool(''),  # False
#     bool(None),  # False
#     bool([]),  # False
#     bool(()),  # False
#     bool([None]),  # True
#     bool((None)),  # False
# )
x1 = 12
x2 = '12'
print(isinstance(x1, (int, float)))  # True
print(isinstance(x2, (int, float)))  # False
print(isinstance(x2, (int, str)))  # True

# def myFn(x, y):
#     return x + y

# # 空函数可以用作占位符, 比如代码逻辑还不知道,但是可以使用pass让代码运行起来
# def nop():
#     pass

# age = int(input('enter ur age: '))
# if age < 18:
#     # 暂时不知道怎么处理，但是又想程序运行起来
#     pass
# else:
#     print(' u can get in ')
