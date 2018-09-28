import requests

headers = {
    'Cookie': '_zap=c58c36f6-92d0-4e43-890c-c391eb00ff9e; _xsrf=XuyyzL4cbJzyt1yEKTohD7DIfkdUdrF8; d_c0="AKAlYn4lQQ6PTr6363XBhFSfdrizMHy6asw=|1537670073"; capsion_ticket="2|1:0|10:1537670139|14:capsion_ticket|44:MGRmMzAwNzZlMTBiNDk3NGIxNWViYWE1Mjk4MDM2MTk=|fe758df6b65a697b6d1ad6b253cd6bd262f3c74ff87e2d76a2296f8b17b32b56"; z_c0="2|1:0|10:1537670165|4:z_c0|92:Mi4xa3VTOUJBQUFBQUFBb0NWaWZpVkJEaVlBQUFCZ0FsVk5GVXFVWEFCZklvLXNkRkFuQUt0ekxZLVRxa0syUE5zYVp3|95fb8ec0e0dc062131f4d9eb97423b4b68654d6834b27e92fafe356536b67abb"; q_c1=8d21c4ee9c304d1a89ab4b74fd2dc4da|1537670165000|1537670165000; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)