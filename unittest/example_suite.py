import unittest
from example import ExampleTest
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    suite = unittest.TestSuite()

    #按顺序执行
    #添加多个，使用列表
    tests = [ExampleTest("test_get_name"),
             ExampleTest("test_get_age"),
             ExampleTest("test_is_male")]

    suite.addTests(tests)

    #添加单个
    suite.addTest(ExampleTest("test_get_hobby"))

    #可以直接使用名字
    suite.addTests(unittest.TestLoader().loadTestsFromName("example.ExampleTest.test_get_age"))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(["example.ExampleTest.test_get_age"]))

    suite.addTests(unittest.TestLoader().loadTestsFromName("example.ExampleTest"))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(["example.ExampleTest"]))

    #也可以直接添加测试用例
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ExampleTest))

    #with open('UnittestTextReport.txt', 'a') as f:
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2)
        runner.run(suite)