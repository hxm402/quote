import unittest

from autotest.quote_interface.function.usermanage.user_manage import Usermanager
from autotest.quote_interface.util.excelop import ExcelOp


class Loginsuccess(unittest.TestCase):
    def setUp(self) -> None:
        self.Usermanage=Usermanager('JSESSIONID=4BB5D1DD5DB5E34D9A74CC393FCA3178')
        self.excel=ExcelOp('C:\\Users\\pc\\PycharmProjects\\project01\\autotest\\quote_interface\\config\\用例.xlsx','登录用例参数')

    def test_1_username_passwd_correct(self):
        res=self.Usermanage.login('http://localhost:8080/JavaPrj_6/',self.excel.get_value(1,2),self.excel.get_value(1,3))
        print(res)
        self.assertIn('报价管理系统',res.content.decode('gbk'))



if __name__ == '__main__':
    unittest.main()
