# # 输入
# name = input()
# age = input('enter ur age: ')
# # 三元表达式
# unit = ' years' if int(age) > 0 else ' year'
# # 输出
# print('ur name is ' + name)

# print('and u r ' + age + unit + ' old')

# sentence = 'i\'m wz, and r u \"OK" ?'
# print(sentence)

# sentence_ = '\\\22e2\\'  # \e2\
# sentence__ = r'\\\222\\'  # \\\222\\
# print(sentence_)
# print(sentence__)
# print('the score is %d' % 96)  # the score is 96
# print('the score is %5d' % 96)  # the score is    96
# print('the score is %05d' % 96)  # the score is 00096

# # %f 没有指定小数点的时候 会 五舍六入到小数点后6位(如下代码)
# print('the score is %f' %
#       96.12345)  # the score is 96.123450   # 末尾会补0 直到小数点后六位(未知原因) TODO;
# print('the score is %f' % 96.123456)  # the score is 96.123456
# print('the score is %f' % 96.1234567)  # the score is 96.123457
# print('the score is %f' % 96.1234546)  # the score is 96.123455
# print('the score is %f' % 96.1234545)  # the score is 96.123454

# print('the score is %.3f' % 96.1234)  # the score is 96.123

# # 没有小数点的时候 %0Xf 会保留小数点后6位 没有的用0补充, 遵循四舍五入
# print('the score is %03f' % 96.12345)  # the score is 96.123450
# print('the score is %03f' % 96.123456)  # the score is 96.123456
# print('the score is %03f' % 96.1234561)  # the score is 96.123456
# print('the score is %03f' % 96.1234564)  # the score is 96.123456
# print('the score is %03f' % 96.1234565)  # the score is 96.123457

# print('the rate is %.2f%%' % 75.3419)  # the rate is 75.34%

# result = 'i m {0}, i m in class {1:02d} and my score is {2:.2f} under the full mark which is {3:.3f}'.format(
#     'wz', 9, 98.7609, 100.00)
# print(result)
# # i m wz, i m in class 09 and my score is 98.76 under the full mark which is 100.000

# fruits = ['apple', 'orange', 'banana', 'pomegranate']
# length = len(fruits)
# print(length)  # 4
# # 获取最后一个
# print(fruits[length - 1])
# # or
# print(fruits[-1])
# # 超出索引会报 IndexError: list index out of range
# # print(fruits[9])

# # 倒数第二个,以此类推
# print(fruits[-2], fruits[-3])

# # 追加到末尾 append
# fruits.append('grape')
# print(fruits)  # ['apple', 'orange', 'banana', 'pomegranate', 'grape']

# 追加到指定位置 insert
# fruits.insert(2, 'cantaloupe')
# print(fruits)  # 'apple', 'orange', 'cantaloupe', 'banana', 'pomegranate']

# # 删除 pop([index])
# fruits.pop()
# print(fruits)  # ['apple', 'orange', 'cantaloupe', 'banana']
# fruits.pop(0)
# print(fruits)  # ['orange', 'cantaloupe', 'banana']

# 元组 tuple

# tup = ('a', 1, 3, 'tg')

# # print(tup)  # ('a', 1, 3, 'tg')
# # print(tup[-1])  # tg

# # Python规定如下
# print((), (1), (1, ), (1, '1'))  # () 1 (1,) (1, '1')
# tuple 不可变指的是 指向不可变,例如:

# _tup = ('HUAT', 11, 42, ['w', 'z'])
# print(_tup)  # ('HUAT', 11, 42, ['w', 'z'])
# # _tup[0] = '345' # 不被允许的,会报错误TypeError: 'tuple' object does not support item assignment
# _tup[3][0] = 'WWW'  # 是被允许的
# print(_tup)  # ('HUAT', 11, 42, ['WWW', 'z'])

# 条件判断
# score = int(input('Enter ur score: '))
# if score >= 90:
#     print('u get an A')
# elif score >= 80:
#     print('u get a B')
# elif score >= 60:
#     print('u get a C')
# else:
#     print('u get a D')

# 循环
# for in
# fruits = ['apple', 'orange', 'banana', 'pomegranate']
# tups = ('HUAT', 11, 42, ['w', 'z'])
# for fruit in fruits:
#     print(fruit)
# for tup in tups:
#     print(tup)
# while
# 打印1-10内的整数
# n = 1
# while n < 10:
#     print(n)
#     n += 1
# print('--------------------分割线---------------------')
# # 打印1-20内的偶数 continue
# m = 0
# while m < 20:
#     m += 1
#     if (m % 2 == 1):
#         continue
#     print(m)
# print('--------------------分割线---------------------')

# # 打印1-50内 第一个9的倍数
# q = 1
# while q <= 50:
#     if q % 9 == 0:
#         print('找到了', q)
#         break
#     print(q)
#     q += 1
# print('--------------------分割线---------------------')

# # DICT
# dic = {'name': 'wz', 'age': 19, 'fav_fruits': ['apple', 'banana', 'orange']}
# print(dic)
# # print('name' in dic)  # True
# # print('name1' in dic)  # False
# # print(dic.get('name'))  # wz
# # print(dic.get('name2'))  # None
# # print(dic.get('name3', '不存在'))  # key值不存在的时候默认会返回None(交互模式下没有), 也可以指定第二个返回值

# # 添加
# dic['name1'] = 'name111'
# print(dic)
# #{'name': 'wz', 'age': 19, 'fav_fruits': ['apple', 'banana', 'orange'], 'name1': 'name111'}
# # 删除
# dic.pop('age')
# print(dic)
# # {'name': 'wz', 'fav_fruits': ['apple', 'banana', 'orange'], 'name1': 'name111'}

# SET
# s = set(['A', 'a', 90, '90'])
# print(s)  # {90, 'a', '90', 'A'}

# s2 = set(['A', 'A', 90, 90])
# print(s2)  # {90, 'A'}

# # 添加
# s.add('wz')
# s.add('wz2')
# print(s)  # {'wz2', '90', 90, 'wz', 'a', 'A'}

# # 删除
# s.remove('wz2')
# # s.remove('wz22') # 删除不存在的key会报错：KeyError: 'wz22'
# print(s)  # {90, 'wz', 'a', 'A', '90'}

s1 = set(['A', 'B', 'C'])
s2 = set(['B', 'C', 'D', 'A'])
s_intersection = s1 & s2  # {'A', 'B', 'C'}
s_union = s1 | s2  #  {'B', 'D', 'C', 'A'}
print(s1, s2, s_intersection, s_union)
