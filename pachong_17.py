import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response=requests.get('http://www.12306.cn',verify=False)
print(response.status_code)
print('###############################################################################################')
import logging
import requests
logging.captureWarnings(True)
response=requests.get('http://www.12306.cn',verify=False)
print(response.status_code)
print('#################################################################################################')


