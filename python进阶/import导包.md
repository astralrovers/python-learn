## import的使用规则

一个`python`源文件可以称作一个模块，那么在其他模块中想要使用另一个模块，就涉及到引用（导入），理入c语言里面的头文件。

### 关于__name__

```python
import test

print(test.__name__) # test，当一个模块被导入时，它的__name__属性就是它的名字
# 不过我们经常看到下面语句
if __name__ == "__main__":
    print("start") # 这是因为我们在运行python程序时传递给python解释器的第一个入口文件，它的__name__会被置为__main__
```

### 关于符号表

符号表sys.modules是一个将模块名称（module_name）映射到已加载的模块（modules） 的字典，每个模块都有一个属性前__name__，
当我们导入一个模块时(import module)，并不会进入到模块内部（直接访问内部函数），只是进入到模块名__name__，需要使用__name__.func来访问模块内部。所以不用担心不同模块里的全局变量、函数和类等重名，在被导入后我们可是使用modulename.itemname去访问：`test.printf("hello")`

### import和from ... import

- import:符号表只是进入模块名
- from ... import:符号表进入了模块内部某些指定的量，可以直接访问itemname，不过只有指定的几个
- from ... import * 会导入模块里的不是以_开头的所有符号表

### 导入过程

不管哪种导入方式，被导入的模块会被执行一次，而且多次导入也只会执行一次，如果说存在链式导入即一个模块导入了另第一个模块和第二个模块，第二个模块导入了第三个模块：
a.py:
```python
import b
import c

print("a")
```

b.py:
```python
import c

print("b")
```

c.py:
```python
print("c")
```

结果：c b a
可以发现c.py只被执行了一次，这是因为在执行a.py时导入b.py，b.py会导入c.py，那么此时c.py已经被添加到符号表sys.module了，a.py再次导入c.py时就直接从符号表里查找，不再重新导入。

### 每个模块的符号表

注意前面提到的符号表存在系统记得符号表sys.module，还存在模块本身的符号表，都在内存里，就比如前一小节说到的，b.py已经导入了c.py，但是a.py并不能访问c.py里的方法，它只在sys.module和b.py的符号表里，b.py才能访问，那么导入sys.module有啥用？前面也提到过，只要导入一次，就会记录到sys.module里，其他模块a.py再导入时，就直接去拿就好了，不用再次执行c.py，用来提高效率。

### 别名

`import a as b`

### 导入模块搜索路径

- 内置模块(标准库)
- 第三方模块
- 自定义模块

你可以从`sys.path`中来查看。

### 关于pyc

现在简单提下，用于加快导入速度，源文件改变了，它会重新被编译。

### 查看模块内部

`dir(modulename)`

### 关于导包

关于目录组织的模块集合，甚至直接理解为目录，称作包。他是一个层次结构的。

前面我们使用到的导入，只是当前目录下的模块，那么如果要导入其他路径下的模块该怎么办呢？

**一个目录下面必须要有__init.py文件才会被识别为一个包。**，最简单的情况是它是一个空文件。

### 不同路径的导包

包的导入和前面的模块导入查找方式是一样的`sys.path`。

- 下级目录:
    ```
    a.py
    nextdir/d.py
    ```

    ```python
    import nextdir.d

    print("a")
    ```

- 上级目录:
    ```
    d.py
    ../c.py
    ```

    ```python
    import sys
    sys.path.append("../")
    import c

    print("d")
    ```

- 上级目录的下级目录
    ```
    d.py
    ../prevdir/e.py
    ```

    ```python
    import sys
    sys.path.append("../")
    import prevdir.e

    print("d")
    ```

    原则上只要是路径匹配了就年内找到，注意`__init__.py`得有。

- from ... import *导包

如果是这种方式导包的话，`__init__.py`就不能写空了:
```python
__all__ = ["echo", "surround", "reverse"] # 那么在使用from ... import * 的时候就会导入这三个模块
```

### 避免循环导入
