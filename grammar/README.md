# Python Grammar

## Table of Contents

1. [输入和输出](#input_print)
2. [数据类型](#data_type)
3. [变量](#variate)
4. [常量](#constant)
5. [运算](#operation)
6. [字符编码](#character_encoding)
7. [格式化](#format)

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

- 字典

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

> Python 格式化方式是使用 % 实现

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
