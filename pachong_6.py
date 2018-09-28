import urllib.parse
import urllib.request
date=bytes(urllib.parse.urlencode({'word':'hello'}),encode='utf8')
reponse=urllib.request.urlopen('http://httpbin.org/post',date=date)
print(reponse.read())