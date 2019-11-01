# Python Grammar

## Table of Contents

1. [输入和输出](#input_print)
2. [数据类型](#data_type)
3. [变量](#variate)
4. [常量](#constant)
5. [运算](#operation)
6. [字符编码](#character_encoding)
7. [格式化](#format)
8. [条件判断](#condition)
9. [循环](#loop)

## Contents

<a name="input_print">

### 输入和输出

```py
# 输入
name = input()
age = input('enter ur age: ')

# 输出
print('ur name is ' + name)
print('and u r '+ age + 'year(s) old')

```

<a name="data_type">

### 数据类型

- 整数

- 浮点数

- 字符串

  ```py
  # 使用 \ 来转义
  sentence = 'i\'m wz, and r u \"OK" ?'

  # 使用 r'' 来表示''内部的字符串不转义
  sentence_ = '\\\22e2\\'  # \e2\
  sentence__ = r'\\\222\\'  # \\\222\\
  ```

- 布尔值

  - True or False

  - 布尔值可以用 and or not 运算

- 空值 None

- 列表

  > list 表示有序集合,是内置的数据类型。每一项可以不同类型

  - 获取列表项

    ```py
    fruits = ['apple', 'orange', 'banana', 'pomegranate']
    length = len(fruits)
    print(length)  # 4

    # 获取最后一个
    print(fruits[length - 1])
    # or
    print(fruits[-1])

    # 超出索引会报 IndexError: list index out of range
    # print(fruits[9])

    # 倒数第二个,以此类推
    print(fruits[-2], fruits[-3])
    ```

  - 追加

    - 追加到尾部 appand(value)

      ```py
      # 追加
      fruits.append('grape')
      print(fruits)  # ['apple', 'orange', 'banana', 'pomegranate', 'grape']
      ```

    - 追加到指定位置 insert(index, value)

      ```py
      fruits.insert(2, 'cantaloupe')
      print(fruits)  # 'apple', 'orange', 'cantaloupe', 'banana', 'pomegranate']
      ```

  - 删除列表项 pop([index])

    > 不传 index 的时候 默认删除最后一项

    ```py
    fruits.pop()
    print(fruits)  # ['apple', 'orange', 'cantaloupe', 'banana']
    fruits.pop(0)
    print(fruits)  # ['orange', 'cantaloupe', 'banana']
    ```

- 元组

  > tuple 也是一种有序列表,使用()表示,一旦初始化就不能被修改

  ```py
  tup = ('a', 1, 3, 'tg')

  print(tup)  # ('a', 1, 3, 'tg')
  print(tup[-1]) # tg
  ```

  > Python 规定如下

  ```py
  # Python规定如下来消除歧义
  print((), (1), (1, ), (1, '1'))  # () 1 (1,) (1, '1')
  ```

  > tuple 不可变指的是 指向不可变,例如:

  ```py
  _tup = ('HUAT', 11, 42, ['w', 'z'])
  print(_tup)  # ('HUAT', 11, 42, ['w', 'z'])
  # _tup[0] = '345' # 不被允许的,会报错误TypeError: 'tuple' object does not support item assignment
  _tup[3][0] = 'WWW'  # 是被允许的
  print(_tup)  # ('HUAT', 11, 42, ['WWW', 'z'])
  ```

- 字典

  > 类型于 JavaScript 中的 Object 对象

  - dict

    ```py
    dic = {'name': 'wz', 'age': 19, 'fav_fruits': ['apple', 'banana', 'orange']}
    print(dic)
    ```

    - 检验 key 是否存在
      - key in dic
        ```py
        print('name' in dic)  # True
        print('name1' in dic)  # False
        ```
      - dic.get(key)
        ```py
        print(dic.get('name')) # wz
        print(dic.get('name2')) # None
        print(dic.get('name3', '不存在'))  # key值不存在的时候默认会返回None(交互模式下没有), 也可以指定第二个返回值
        ```
    - 添加

      ```py
      dic['name1'] = 'name111'
      print(dic)
      #{'name': 'wz', 'age': 19, 'fav_fruits': ['apple', 'banana', 'orange'], 'name1': 'name111'}
      ```

    - 删除某个 key 和 value

      > pop(key) 进行删除 (不存在的 key 值会报错)

      ```py
      dic.pop('age')
      print(dic) # {'name': 'wz', 'fav_fruits': ['apple', 'banana', 'orange'], 'name1': 'name111'}
      ```

  - set

    - set 和 dict 类似，但是只存储 key 不存储 value

      ```py
      s = set(['A', 'a', 90, '90'])
      print(s)  # {90, 'a', '90', 'A'}
      ```

    - 在 set 中没有重复的 key,重复的元素会被自动过滤

      ````py
      s2 = set(['A', 'A', 90, 90])
      print(s2)  # {90, 'A'}
      ```
      ````

    - add(key) 可以重复添加元素,但是会过滤重复的。

      ```py
      s.add('wz')
      s.add('wz2')
      print(s)  # {'wz2', '90', 90, 'wz', 'a', 'A'}
      ```

    - remove(key) 删除元素

      ```py
      s.remove('wz2')
      # s.remove('wz22') # 删除不存在的key会报错：KeyError: 'wz22'
      print(s)  # {90, 'wz', 'a', 'A', '90'}
      ```

    - 交集和并集操作
      ```py
      s1 = set(['A', 'B', 'C'])
      s2 = set(['B', 'C', 'D', 'A'])
      s_intersection = s1 & s2  # {'A', 'B', 'C'}
      s_union = s1 | s2  #  {'B', 'D', 'C', 'A'}
      print(s1, s2, s_intersection, s_union)
      ```

<a name="variate">

### 变量

> 大小写英文字母、数字和下划线\_组合,且不能以数字开头

<a name="constant">

### 常量

> 通常使用全部大写字母表示常量

```py
PI = 3.1415826
```

<a name="operation">

### 运算

- 除运算( / 和 // )

  ```py
  print(10/3) # 3.3333333333333335
  print(9/3) # 3.0

  # 地板除
  print(10//3) # 3
  print(9//3) # 3
  ```

- 余数运算( % )

  ```py
  print(10%3) # 1
  ```

  <a name="character_encoding">

### 字符编码

<a name="format">

### 格式化

- Python 格式化方式一：使用 % 实现

  | 占位符 |       备注       |   替换内容   |
  | :----: | :--------------: | :----------: |
  |   %d   | 可以指定是否补 0 |     整数     |
  |   %f   |  可以指定小数位  |    浮点数    |
  |   %s   |                  |    字符串    |
  |   %x   |                  | 十六进制整数 |

  > 只有一个占位符的时候可以省略括号,多个占位符的时候使用()依次展开

  ```py
  print('the score is %d' % 96)  # the score is 96
  print('the score is %5d' % 96)  # the score is    96 # 会总长度为5 多余的用空格占据
  print('the score is %05d' % 96)  # the score is 00096 # 会总长度为5 多余的用0占据
  ```

  ```py

  # %f 没有指定小数点的时候 会 五舍六入到小数点后6位(如下代码)
  print('the score is %f' %
        96.12345)  # the score is 96.123450   # 末尾会补0 直到小数点后六位(未知原因) TODO;
  print('the score is %f' % 96.123456)  # the score is 96.123456
  print('the score is %f' % 96.1234567)  # the score is 96.123457
  print('the score is %f' % 96.1234546)  # the score is 96.123455
  print('the score is %f' % 96.1234545)  # the score is 96.123454

  ```

  ```py
  # 正常的情况下
  print('the score is %.3f' % 96.1234)  # the score is 96.123
  ```

  ```py
  # 没有小数点的时候 %0Xf 会保留小数点后6位 没有的用0补充, 遵循四舍五入
  print('the score is %03f' % 96.12345)  # the score is 96.123450
  print('the score is %03f' % 96.123456)  # the score is 96.123456
  print('the score is %03f' % 96.1234561)  # the score is 96.123456
  print('the score is %03f' % 96.1234564)  # the score is 96.123456
  print('the score is %03f' % 96.1234565)  # the score is 96.123457
  ```

  > 用 %% 来表示一个普通的字符串 %

  ```py
  print('the rate is %.2f%%' % 75.3419)  # the rate is 75.34%
  ```

- Python 格式化方式二：使用 字符串的 format()方法 实现

  > 占位符是{0} {1} {2}...

  ```py
  result = 'i m {0}, i m in class {1:02d} and my score is {2:.2f} under the full mark which is {3:.3f}'.format(
    'wz', 9, 98.7609, 100.00)
  print(result)# i m wz, i m in class 09 and my score is 98.76 under the full mark which is 100.000
  ```

<a name="condition">

### 条件判断

```py
score = int(input('Enter ur score: '))
if score >= 90:
    print('u get an A')
elif score >= 80:
    print('u get a B')
elif score >= 60:
    print('u get a C')
else:
    print('u get a D')
```

<a name="loop">

### 循环

- for in

  ```py
  fruits = ['apple', 'orange', 'banana', 'pomegranate']
  tups = ('HUAT', 11, 42, ['w', 'z'])
  for fruit in fruits:
      print(fruit)
  for tup in tups:
      print(tup)
  ```

- while

  ```py
  # 打印1-10内的整数
  n = 1
  while n < 10:
      print(n)
      n += 1
  ```

  ```py
  # 打印1-20内的偶数 continue
  m = 0
  while m < 20:
      m += 1
      if (m % 2 == 1):
          continue
      print(m)
  ```

  ```py
  # 打印1-50内 第一个9的倍数
  q = 1
  while q <= 50:
      if q % 9 == 0:
          print('找到了第一个9的倍数', q)
          break
      print(q)
      q += 1
  ```
