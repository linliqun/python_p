#登录网站的账号密码，状态编码要是200，就表示登陆成功，//400表示没登录后台服务器
#这个程序是有问题的，没登录进去
import requests
from requests.auth import HTTPBasicAuth
r=requests.get('https://www.zhihu.com/signup?next=%2F',auth=HTTPBasicAuth('15589102168','linDH@985'))
print(r.status_code)