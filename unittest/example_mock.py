import unittest
import mock

#不要使用from simple_mock import *
#mock修改了会无效
import simple_mock

class TestClient(unittest.TestCase):

    def test_success_request(self):
        #生成一个模拟函数
        success_send = mock.Mock(return_value='200')
        #simple_mock.send_request = success_send #将原函数替换成模拟函数
        with mock.patch('simple_mock.send_request', success_send):
            from simple_mock import visit_ustack
            self.assertEqual(visit_ustack(), '200')
            self.assertEqual(visit_ustack(), '200')

            #是否被调用
            self.assertEqual(simple_mock.send_request.called, True)
            #检测参数
            #都只是检测最近一次调用，第二个会忽略其他调用
            #assert_called_once_with
            success_send.assert_called_with('http://www.ustack.com')
            #assert_any_call
            #参数检查
            call_args = simple_mock.send_request.call_args
            self.assertIsInstance(call_args[0][0], str)

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        simple_mock.send_request = fail_send
        self.assertEqual(simple_mock.visit_ustack(), '404')


if __name__ == "__main__":
    unittest.main(verbosity=2)
