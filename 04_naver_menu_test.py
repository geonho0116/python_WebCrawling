import urllib.request
import bs4

url="https://www.naver.com/"
html=urllib.request.urlopen(url)

bs_obj=bs4.BeautifulSoup(html,"html.parser")

ul = bs_obj.find("ul", {"class":"an_l"}) #중괄호 안에 조건을 지정

lis = ul.findAll("li") # 리스트에 저장된다. [<li></li>,<li></li>]

for li in lis:
    a_tag=li.find("a") #a_tag=li.find("a",{"class":"an_a"})
    span=a_tag.find("span",{"class":"an_txt"})
    print(span.text)
    # print(a_tag.text)


# for li in ul:
    # print(li)
