from urllib import request,error
try:
    reponse=request.urlopen('http://cuiqingcai.com')
except error.URLError as e:
    print(e.reason)