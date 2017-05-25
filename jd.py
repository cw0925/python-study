import re
import urllib.request

def craw(url, page):

	# req = urllib.request.Request(url)
	# req.add_header('User-Agent':'')
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    # print(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    resutl1 = re.compile(pat1).findall(html1)
    resutl1 = resutl1[0]
    # print(resutl1)

    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg|png">'
    imagelist = re.compile(pat2).findall(resutl1)
    print(imagelist)

    x = 1

    for imageurl in imagelist:
        imagename = "/Users/afarsoft/Desktop/images/" + str(page)+str(x)+".jpg"
        imageurl = "http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
            x += 1

for i in range(1, 80):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    # print(url)
    craw(url, i)

