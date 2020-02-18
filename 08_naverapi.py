#네이버 api token 발급받기
#네이버개발자센터
#json을 보기 쉽게 해주는 곳-> json tree
import os
import sys
import urllib.request
client_id = "dnogUSKTMPAovSEL4NNw"
client_secret = "of5rOpfUt2"
encText = urllib.parse.quote("에어컨")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)