import requests
cookies='_zap=fc799dd8-403c-48d3-b26c-5c3cbab12cda; _xsrf=EQQKM2cdmOAziAjB5tvntjYkkUnzBZ5P; __guid=74140564.988848292388261800.1536561869266.0845; d_c0="AEAkieyhMA6PTuiA7DsVTG_s1JaQ43z4Bv0=|1536561841"; q_c1=f0ab33e83efc4215a155deade6decc1f|1536561945000|1536561945000; capsion_ticket="2|1:0|10:1536647431|14:capsion_ticket|44:N2FiZGM2Yjc2ZTNhNGZiMDliYWJkNWMzMjVhMWNkZjI=|3dbdcae02517fc981b0692396dfaa9b032780539b5387205d6031070e4facda1"; z_c0="2|1:0|10:1536647433|4:z_c0|92:Mi4xa3VTOUJBQUFBQUFBUUNTSjdLRXdEaVlBQUFCZ0FsVk5DYS1FWEFBN0dLQkRsMDJKYWZmendMeERWSDQtbDhycTh3|8bf14b060f2abd79819e31c4269ad554025e8f02303559b057ba7f1110b6ed83"; __utmv=51854390.100--|2=registration_date=20170419=1^3=entry_date=20170419=1; __utma=51854390.506675401.1536663739.1537930363.1537962837.3; __utmz=51854390.1537962837.3.3.utmcsr=germey.gitbooks.io|utmccn=(referral)|utmcmd=referral|utmcct=/python3webspider/content/3.2.1-%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8.html; tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c; monitor_count=3'
jar=requests.cookies.RquestsCookieJar()
headers={
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key,value=cookie.split('=',1)
    jar.set(key,value)
r=requests.get('http://www.zhihu.com',cookies=jar,headers=headers)
print(r.text)