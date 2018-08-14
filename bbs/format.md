### 总结format函数格式化输出
  - 1.基本语法  
      ```
      #str.format()
      In [4]: print('{}'.format('hello'))
      hello
      ``` 
      str为格式，format内参数为输出内容，每个参数对应{}来输出  
      ```
      In [5]: print('hello {} {}'.format('world', 2018))
      hello world 2018
      ```  
  - 2.指定参数索引位置来输出  
      ```
      print('hello {1} {0}'.format(2018, 'world'))
      hello world 2018
      ```  
      把format的参数比作一个元组的话，那么{num}中的num就是下标  
      还可以使用关键字参数的形式：  
      ```
      In [7]: print('hello {arg} {0}'.format(2018, arg='world')) #arg相当于关键字参数名
      hello world 2018
      ```  
  - 3.{field_name:conversion}形式输出  
      field_name表示元组下标，conversion表示格式，使用:分割  
      ```
      In [8]: print('hello {arg} {0:f}'.format(2018, arg='world')) #0:f表示下标为0的数据输出为浮点数，数据类型与c相同
      hello world 2018.000000
      ```
      In [9]: print('hello {arg} {0:.2f}'.format(2018.1234, arg='world'))
      hello world 2018.12
      ```  
  - 4.对齐
      ```
      In [10]: print('hello {arg} {0:10}'.format(2018, arg='world')) #:后面直接跟数字则表示对齐长度，10个字符对齐
      hello world       2018
      ```  
      默认是有对齐，<表示左对齐，^表示居中对齐，>表示右对齐  
      ```
      In [11]: print('hello {arg} {0:c>10}'.format(2018, arg='world')) #长度不够时重用指定字符(c)来填充，只能使用单个字符
      hello world cccccc2018
      ```
      ```
      In [14]: print("Sammy ate {0:5.0f} percent of a pizza!".format(75.765367)) #数字的话小数点前面是对齐大小，与c类似
      Sammy ate    76 percent of a pizza!
      ```  

