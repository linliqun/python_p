import requests
response=requests.get('http://www.12306.cn',verify=False)
print(response.status_code)