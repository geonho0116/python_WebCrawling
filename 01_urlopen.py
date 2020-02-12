#네이버 첫 페이지 받아오기

import urllib.request

url="https://www.naver.com/"
html= urllib.request.urlopen(url)

print(html.read())
