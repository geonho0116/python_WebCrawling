from urllib.request import urlopen
import bs4

url="https://news.naver.com/"
html=urlopen(url)

bs_obj=bs4.BeautifulSoup(html.read(),"html.parser")

ul=bs_obj.find("ul",{"class":"hdline_article_list"})
lis = ul.findAll("li")

for li in lis:
    a_tag=li.find("a")
    print(a_tag.text)
#titles = [li.find("a").text for li in lis]