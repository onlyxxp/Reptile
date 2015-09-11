import urllib
import urllib2
import re
from bs4 import BeautifulSoup


def regixs():
    global m
    m = re.match(r'[a-b0-9*]{16}', '  6d9adab06a*2e*ea  ')
    if m:
        print "m.groups():", m.group()
    else:
        print "not match"


def proxy(enable=False):
    global enable_proxy, proxy_handler, null_proxy_handler, opener
    enable_proxy = enable
    proxy_handler = urllib2.ProxyHandler({"http": 'apn.5bird.com:57413'})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)


def requestUrl(url, values, post):
    global data, headers, request, response
    data = urllib.urlencode(values)
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
               'Referer': 'http://www.zhihu.com/articles',
               'Content-Type': 'application/x-www-form-urlencoded'
    }

    print url+"?"+data
    if post:
        request = urllib2.Request(url, data, headers)
    else:
        request = urllib2.Request(url+"?"+data)


    try:
        response = urllib2.urlopen(request)
        print response.read()
        return response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason


def main():
    proxy(True)

    global values, url, data, headers, request, response
    values = {"username": "1016903103@qq.com", "password": "XXXX"}
    url = "http://www.t66y.com"
    html = requestUrl(url, values, False)

    soup = BeautifulSoup(html)
    print soup.prettify()

    regixs()
main()