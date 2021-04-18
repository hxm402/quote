import requests

from autotest.quote_interface.util.loginfo import LogInfo


class Usermanager:
    def __init__(self,cookie):
        self.cookie=cookie
        self.log=LogInfo()

    # def get_cookie(self,login):
    #     set_cookie =login.headers['Set-Cookie']
    #     # print(set_cookie)
    #     array=set_cookie.split(';')
    #     # print(array)
    #     cookieValue = ''
    #     for arr in array:
    #         if arr!=' Path=/JavaPrj_6' and arr!=' HttpOnly':
    #             cookieValue += arr + ';'
    #     return cookieValue

    def login(self,url,Content_Type,data):
        header = {
            "Content-Type":Content_Type
        }
        data =data
        self.log.set_message('info','发送登录请求')
        res = requests.post(url,data=data, headers=header)
        return res

    def add_user(self,url,Content_Type,data):
        header = {
            "Content-Type":Content_Type,
            'Cookie':self.cookie
        }
        data =data
        self.log.set_message('info', '发送添加用户请求')
        res = requests.post(url,data=data, headers=header)
        return res

    def search_user(self,url,Content_Type,username,query):
        header = {
            "Content-Type": Content_Type,
            'Cookie':self.cookie
        }
        data = {
            'username':username,
            'query':query
        }
        res = requests.post(url,data=data, headers=header)
        return res

    def delete_user(self,url,Content_Type):
        header = {
            "Content-Type": Content_Type,
            'Cookie':self.cookie
        }
        res = requests.post(url, headers=header)
        return res
# Usermanager=Usermanager('JSESSIONID=4BB5D1DD5DB5E34D9A74CC393FCA3178')
# # print(Usermanager.login('http://localhost:8080/JavaPrj_6/login.do','application/x-www-form-urlencoded;charset=utf-8',{'username':55,'password':'445'}).cookies)
# print(Usermanager.add_user('http://localhost:8080/JavaPrj_6/control/usermanage_add.do','application/x-www-form-urlencoded;charset=utf-8',{'username':'66','password':'123456','grade':1}).text)
