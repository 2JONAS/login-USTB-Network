import requests
import re






APP_TITLE = u'校园网登录程序'
APP_ICON = 'res/python.ico'
# 账号
account = ""
# 密码
password = ""
common = {'DDDDD':'','upass':'','v6ip':'0','0MKKey':'123456789'}
pdata = {'DDDDD':account,'upass':password,'v6ip':'0','0MKKey':'123456789'}
class login():
        def __init__(self):
                self.loginurl = 'http://202.204.48.66/'
                self.checkurl = 'http://cippv6.ustb.edu.cn/get_ip.php'
        def repost(self,dict):
                userData = dict
                try:
                        r = requests.get(self.loginurl)
                except:
                        return False
                try:
                        p = requests.get(self.checkurl)
                        if p.status_code == 200 :
                                userData['v6ip'] = re.findall("'(.+?)'",p.text)[0]
                        else :
                                userData['v6ip'] = '0'
                except:
                        userData['v6ip'] = '0'
                print(userData)
                try:
                        m = requests.post(self.loginurl,data=userData)
                        print("msg",m)
                        return True
                except:
                        return False
####
#登录
####
send = login()
print("login",send.repost(pdata))