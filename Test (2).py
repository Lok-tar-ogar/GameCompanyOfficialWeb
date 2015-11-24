from pyDes import *
import base64
import urllib
import urllib.parse
import sys
import http.cookiejar


def test():
    # This should not produce any unexpected errors or exceptions
    from time import time
    from binascii import unhexlify as unhex
    from binascii import hexlify as dohex
    data = "123123"
    k = des("MV03ND.f", ECB, "\0\0\0\0\0\0\0\0",
            pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
    print("Encrypted: %r" % d)
    a = base64.b64encode(d)
    print("%r" % a)
    url = "http://123.59.24.94:8093/login"
    postdata = {'userName': '123', 'pwd': '123', 'sign': a}
    #postdata = postdata.encode('utf-8')
    res = res = urllib.request.urlopen(url, postdata)
    print(res)

if __name__ == '__main__':
    test()
