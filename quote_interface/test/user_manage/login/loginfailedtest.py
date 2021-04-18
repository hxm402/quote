import unittest

from autotest.quote_interface.function.usermanage.user_manage import Usermanager
from autotest.quote_interface.util.excelop import ExcelOp


class Loginfailed(unittest.TestCase):
    def setUp(self) -> None:
        self.Usermanage = Usermanager('JSESSIONID=4BB5D1DD5DB5E34D9A74CC393FCA3178')
        self.excel = ExcelOp('C:\\Users\\pc\\PycharmProjects\\project01\\autotest\\quote_interface\\config\\用例.xlsx','登录用例参数')

    def test_1_unull_pnull(self):
        res = self.Usermanage.login('http://localhost:8080/JavaPrj_6/login.do',self.excel.get_value(1,2),self.excel.get_value(2,3))
        # print(res.text)
        self.assertIn('用户名',res.content.decode('gbk'))


    def test_2_usernameerror(self):
        res = self.Usermanage.login('http://localhost:8080/JavaPrj_6/login.do',self.excel.get_value(1,2),self.excel.get_value(3,3))
        # print(res.text)
        self.assertIn('用户名',res.content.decode('gbk'))

    def test_3_ucorrect_perror(self):
        res = self.Usermanage.login('http://localhost:8080/JavaPrj_6/login.do',self.excel.get_value(1,2),self.excel.get_value(4,3))
        # print(res.text)
        self.assertIn('用户名',res.content.decode('gbk'))

    def test_4_ucorrect_pnull(self):
        res = self.Usermanage.login('http://localhost:8080/JavaPrj_6/login.do',self.excel.get_value(1,2), self.excel.get_value(5,3))
        # print(res.text)
        self.assertIn('用户名',res.content.decode('gbk'))


if __name__ == '__main__':
    unittest.main()
