import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from HwTestReport import HTMLTestReportEN

from autotest.quote_interface.function.usermanage.user_manage import Usermanager
from autotest.quote_interface.test.user_manage.login.loginfailedtest import Loginfailed
from autotest.quote_interface.test.user_manage.login.loginsuccesstest import Loginsuccess
from autotest.quote_interface.util.excelop import ExcelOp


class useradd_success(unittest.TestCase):
    def setUp(self) -> None:
        self.Usermanage = Usermanager('JSESSIONID=4BB5D1DD5DB5E34D9A74CC393FCA3178')
        self.excel = ExcelOp('C:\\Users\\pc\\PycharmProjects\\project01\\autotest\\quote_interface\\config\\用例.xlsx','adduseryongli')
    def test_1_case(self):
        res=self.Usermanage.add_user('http://localhost:8080/JavaPrj_6/control/usermanage_add.do','application/x-www-form-urlencoded;charset=utf-8',{'username':'77jj','password':'123456','grade':1})
        # print(res.text)
        self.assertIn('添加记录成功',res.text)

if __name__ == '__main__':
    # unittest.main()
    # 测试套件
    suite = unittest.TestSuite()
    # 加载测试用例
    useraddsuccess_case = unittest.TestLoader().loadTestsFromTestCase(useradd_success)
    loginsuccess_case = unittest.TestLoader().loadTestsFromTestCase(Loginsuccess)
    loginfailed_case = unittest.TestLoader().loadTestsFromTestCase(Loginfailed)
    # 测试用例加入到测试套件中
    lst_case=[useraddsuccess_case,loginsuccess_case,loginfailed_case]
    suite.addTests(lst_case)
    # 日期
    file_date = time.strftime('%Y-%m-%d_%H_%M_%S')
    # print(file_date)
    # 报告文件
    # fp=open('../../report/'+file_date+'.html','wb+')
    with open('../../../report/report'+file_date+'.html', 'wb+') as fp:
        # runner=HTMLTestRunner(stream=fp, verbosity=2, title='quote project', description='UI auto test')
        runner = HTMLTestReportEN(stream=fp, verbosity=2, title='Quote project', description='interface auto test')
        # # 需要一个文本测试运行对象
        # runner = unittest.TextTestRunner(verbosity=2)
        # 执行套件测试用例
        runner.run(suite)
    # unittest.main(verbosity=2)




