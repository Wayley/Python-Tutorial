# Python

## intro

> Python 是解释型语言(执行时会一行一行翻译成机器码)

> Python 解释器

- CPython

  Python 3.x 后官方自带的解释器，C 语言开发的。

  ```bash
  # 运行python就启动了CPython这个解释器,然后进入Python交互模式
  $ python

  # exit()会退出Python交互模式,并回到命令行模式
  >>> exit()
  ```

- IPython

  IPython 是基于 CPython 之上的一个交互式解释器。

- PyPy

  PyPy 采用 JIT 技术,对 Python 代码进行动态编译(不是解释)

- Jython

  Jython 是运行在 Java 平台上的 Python 解释器,可以把 Python 代码编译成 Java 字节码执行。

- IronPython

  IronPython 是运行在 .NET 平台上的 Python 解释器,可以把 Python 代码编译成 .NET 的字节码。

## 输出和输入

> 输出 ( print )

```python
print('hi i m wz)
```

> 输入 ( input )
