# from urllib import request
import urllib.request

with urllib.request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    # print('Data:', data.decode('utf-8'))
    print(f.info(),f.getcode(),f.geturl())