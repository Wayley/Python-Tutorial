# Python Grammar

## Table of Contents

1. [输入和输出](#input_print)
2. [数据类型](#data_type)
3. [变量](#variate)
4. [常量](#constant)
5. [运算](#operation)
6. [字符编码](#character_encoding)

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
