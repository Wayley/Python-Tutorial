## This is the notes collection of function in Python Lang

## Table of Contents

1. [Python 内置函数](#fn_built_in)
2. [自定义函数](#fn_user_defined)

## Contents

<a name="fn_built_in">

### Python 内置函数

- abs() 求绝对值,有且仅有一个参数,参数类型和数量错误时会报出错误
- max(k1, k2, k3, ...) 求多个数中最大值

- 类型转换函数: int() float() str() bool()

  ```py
  print(
    int(3),  # 3
    int(3.14),  # 3
    int(3.50),  # 3
    int(3.65),  # 3
    int('3'),  # 3
    int('3.14'),  # ValueError: invalid literal for int() with base 10: '3.14'
    int('abc'),  # ValueError: invalid literal for int() with base 10: 'abc'
  )
  ```

  ```py
  print(
      float(3),  # 3.0
      float(3.14),  # 3.14
      float(3.50),  # 3.5
      float(3.65),  # 3.65
      float('3'),  # 3.0
      float('3.0'),  # 3.0
      float('abc'),  # ValueError: could not convert string to float: 'abc'
  )
  ```

  ```py
  print(
      str(3),  # 3
      str(3.0),  # 3.0
      str(3.14),  # 3.14
      str('3'),  # 3
      str('3.0'),  # 3.0
      str('abc'),  # abc
  )
  ```

  ```py
  print(
      bool(1),  # True
      bool('1'),  # True
      bool(0),  # False
      bool('0'),  # True
      bool(''),  # False
      bool(None),  # False
      bool([]),  # False
      bool(()),  # False
      bool([None]),  # True
      bool((None)),  # False
  )
  ```

- 类型检查函数 isinstance()

  ```py
  x1 = 12
  x2 = '12'
  print(isinstance(x1, (int, float)))  # True
  print(isinstance(x2, (int, float)))  # False
  print(isinstance(x2, (int, str)))  # True
  ```

<a name="fn_user_defined">

### 自定义函数

- 自定义函数 格式
  ```py
  def myFn(x, y):
      return x + y
  ```
- 空函数 使用 pass

  > 空函数可以用作占位符, 比如代码逻辑还不知道,但是可以使用 pass 让代码运行起来

  ```py
  def nop():
      pass
  ```

  > pass 还可以用在其他语句中，比如：

  ```py
  age = int(input('enter ur age: '))
  if age < 18:
      # 暂时不知道怎么处理，但是又想程序运行起来
      pass
  else:
      print(' u can get in ')
  ```
