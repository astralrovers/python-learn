# 更好的格式化输出

关于python你可以使用类似c语言的格式化输出，这里介绍另一种格式化输出，更加直观`format`模块

## 注意点

在3.6之前只能使用`format`函数做这方面的格式化:

```shell
In [1]: age = 24

In [2]: name = 'yuwangliang'

In [9]: 'my name is {name}, age is {age}'.format(name=name, age=age)
Out[9]: 'my name is yuwangliang, age is 24'
```

在3.6之后可以加字符串前缀:

```shell
In [9]: f'my name is {name}, age is {age}'
```

## 关于format函数格式化

### 基本用法

使用格式化的话，你要使用{}表示这段字符窜使用的是格式化字符串，使用方法举例

```python
print("my name is {}, age is {}".format("ywl", 23)) # 默认填充
# out : my name is ywl, age is 23

print("my age is {1}, name is {0}".format("ywl", 23)) # 按索引填充

print("my age is {age}, name is {name}".format(name="ywl", age=23)) # 按关键字填充

my_info = {"name" : "ywl", "age" : 23}
print("my age is {0[age]}, name is {0[name]}".format(my_info)) # 访问字典/那么列表也可以使用下标/字典解包也可以

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('ywl', 24)
print("my age is {p.age}, name is {p.name}".format(p=p)) # 访问对象属性

```

### 格式化输出

> 语法:
> 格式限定符
> 语法是{}中带:号
> {:对齐方式  填充}
> 填充与对齐
> 填充常跟对齐一起使用
> ^、<、>分别是居中、左对齐、右对齐，后面带宽度
> :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充

```shell
In [4]: '输出左对齐定长为10位  [{:<10}]'.format('12') #默认填充空格的
Out[4]: '输出左对齐定长为10位  [12        ]'

In [5]: '输出右对齐定长为10位  [{:>10}]'.format('12') #默认填充空格的
Out[5]: '输出右对齐定长为10位  [        12]'

In [6]: '输出右对齐定长为10位  [{:0>10}]'.format('12') #修改填充，填充只能是一个ASCII字符
Out[6]: '输出右对齐定长为10位  [0000000012]'

In [7]: '输出居中对齐定长为10位，填充x  [{:x^10}]'.format('12') #修改填充，填充只能是一个ASCII字符
Out[7]: '输出居中对齐定长为10位，填充x  [xxxx12xxxx]'

In [8]: '{:.2f}'.format(1233442.23453) #通常都是配合 f 使用,其中.2表示长度为2的精度，f表示float类型
Out[8]: '1233442.23'

In [9]: '{:,}'.format(9987733498273.0432) #使用逗号金额分割符
Out[9]: '9,987,733,498,273.043'

```

关于进制转换和其他的

b : 二进制
d ：十进制
o ：八进制
x ：十六进制
!s ：将对象格式化转换成字符串
!a ：将对象格式化转换成ASCII
!r ：将对象格式化转换成repr

```shell
In [10]: '10 二进制 ：{:b}'.format(10)
Out[10]: '10 二进制 ：1010'

In [11]: '10 十进制 ：{:d}'.format(10)
Out[11]: '10 十进制 ：10'

In [12]: '10 八进制 ：{:o}'.format(10)
Out[12]: '10 八进制 ：12'

In [13]: '10 十六进制 ：{:x}'.format(10)
Out[13]: '10 十六进制 ：a'

In [14]: '{!s}'.format(10) #格式化转换
Out[14]: '10'

In [15]: '{!a}'.format('1000') #格式化转换
Out[15]: "'1000'"

In [16]: '{!r}'.format('1000') #格式化转换
Out[16]: "'1000'"

```

## f和F的字符串表达式前缀

前面也说过，3.6之后可以直接在字符串前面加f或者F进行格式化输出，不需要使用format，而且更加方便，
方便之处在于你在{}之间直接写变量名就好了，不再需要传参，我们来看几个例子就明白了：

```shell
In [3]: class Person: 
   ...:     def __init__(self,name,age): 
   ...:         self.name = name 
   ...:         self.age = age 
   ...:  
   ...: person = Person('ywl', 24)

In [4]: f"my age is {person.age}, name is {person.name}" # 直接使用对象
Out[4]: 'my age is 24, name is ywl'

In [5]: my_info = {"name" : "ywl", "age" : 23} 
   ...: "my age is {my_info[age]}, name is {my_info[name]}" # 直接使用变量
Out[5]: 'my age is {my_info[age]}, name is {my_info[name]}'

In [6]: f'输出左对齐定长为10位  [{12:<10}]' #新的格式化
Out[6]: '输出左对齐定长为10位  [12        ]'

In [9]: number = 10

In [10]: f'{number!a}' #格式转换
Out[10]: '10'

```