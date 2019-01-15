import unittest

from simple import *

"""
TestCase 也就是测试用例
TestSuite 多个测试用例集合在一起，就是TestSuite
TestLoader是用来加载TestCase到TestSuite中的
TestRunner是来执行测试用例的,测试的结果会保存到TestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息


1.一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，
包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。
元测试(unit test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。

2.而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。

3.TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法，
就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例。

4.TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法。
测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。

5.而对一个测试用例环境的搭建和销毁，是一个fixture。

6.一个class继承了unittest.TestCase，便是一个测试用例，但如果其中有多个以 test 开头的方法，
那么每有一个这样的方法，在load的时候便会生成一个TestCase实例，
如：一个class中有四个test_xxx方法，最后在load到suite中时也有四个测试用例。

到这里整个流程就清楚了：
写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，
运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，
main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。
这里加个说明，在Runner执行时，默认将执行结果输出到控制台，我们可以设置其输出到文件，
在文件中查看结果（你可能听说过HTMLTestRunner，是的，通过它可以将结果输出到HTML中，
生成漂亮的报告，它跟TextTestRunner是一样的，从名字就能看出来，这个我们后面再说）。
"""

class ExampleTest(unittest.TestCase):
    def setUp(self):
        #每个测试用例执行之前执行
        #print("case start")
        pass

    def tearDown(self):
        #每个测试项用例执行之后执行
        #print("case stop")
        pass

    #必须要加这装饰器
    @classmethod
    def setUpClass(self):
        #所有测试用例执行之前执行，只执行一次
        #print("test start")
        pass

    @classmethod
    def tearDownClass(self):
        #所有测试用例执行之后执行，只执行一次
        #print("test stop")
        pass

    def test_get_name(self):
        self.assertEqual("unittest", get_name())

    def test_get_age(self):
        self.assertEqual(24, get_age())

    """
    skip装饰器一共有三个 
    unittest.skip(reason)、
    unittest.skipIf(condition, reason)、
    unittest.skipUnless(condition, reason)，
    skip无条件跳过，
    skipIf当condition为True时跳过，
    skipUnless当condition为False时跳过。
    """
    @unittest.skip("I don't want to run this case.")
    def test_get_hobby(self):
        self.assertEqual("program", get_hobby())

    def test_is_male(self):
        self.skipTest('Do not run this.')
        self.assertTrue(is_male())

"""
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
"""

if __name__ == "__main__":
    unittest.main(verbosity=2)
