#!/usr/bin/python
# coding=utf-8
"""
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
语法
def functionname( parameters ):
	"函数_文档字符串"
	function_suite
	return [expression]

默认情况下，参数值和参数名称是按函数声明中定义的的顺序匹配起来的。
"""
#定义
def firsthello(str):
	print "打印任何输入字符串"
	print str
	return

#调用
firsthello("hello world")

"""
在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]

a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""
#不可变对象
def ChangeInt( a ):
	a = 10

b = 2
ChangeInt(b)
print b # 结果是 2

# 可写函数说明
def changeme( mylist ):
	"修改传入的列表"
	mylist.append([1,2,3,4]);
	print "函数内取值: ", mylist
	return
					 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist


'''
参数
以下是调用函数时可使用的正式参数类型：

必备参数
关键字参数
默认参数
不定长参数

'''

#必备参数为调用时必须传入函数声明参数的正确顺序与数量

#关键字参数是指传参顺序可以随意，使用声明时参数名来确定，如下
def printfinfo(name, age):
	print "姓名：%s，年龄：%d" % (name, age)
	return

printfinfo(age = 22, name = "yu_yuan")

#缺省参数
#调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
def printfinfo2(name, age = 25):
	print "姓名：%s，年龄：%d" % (name, age)
	return

printfinfo2(name = "niki")

"""
不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
	"函数_文档字符串"
	function_suite
	return [expression]
加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。如下实例：
"""

def printfinfo3(*varlist):
	global	globalvar 
	globalvar = "globalvar"
	print "参数长度：%d" % (len(varlist))
	for var in varlist:
		print "var:", var

	return

printfinfo3(10, 20, 30)
print "内部声明的全局变量：", globalvar
"""
匿名函数
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
"""

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )

#全局变量和局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
#但是在函数内部可以声明全局变量:	global globvar    # 使用 global 声明全局变量
