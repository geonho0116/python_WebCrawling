import requests
from bs4 import BeautifulSoup

def get_bs_obj(search):
    if search:
        url="https://www.wevity.com/?c=find&s=1&gub=1&cidx=21+&mode=&sp=name&sw="+search
    else:
        url="https://www.wevity.com/?c=find&s=1&gub=1&cidx=21"
    result=requests.get(url)
    bs_obj=BeautifulSoup(result.content,"html.parser")
    return bs_obj

def get_list():
    search=input("검색어를 입력하세요(최근 15개의 공모전 조회:엔터):")
    bs_obj=get_bs_obj(search)
    ul_con=bs_obj.find("ul",{"class":"list"})
    con_tits=ul_con.findAll("div",{"class":"tit"})
    con_organ=ul_con.findAll("div",{"class":"organ"})
    con_day=ul_con.findAll("div",{"class":"day"})
    n=len(con_tits)
    for i in range(n):
        con_tit=con_tits[i].find("a")
        if con_tit:
            print("공모전명{0}:".format(i),con_tit.text)
            print("주최기관{0}:".format(i),con_organ[i].text)
            print("남은기간{0}:".format(i),con_day[i].text.strip())
            print("링크주소{0}:".format(i),"https://www.wevity.com/"+con_tits[i].find("a")["href"])


while True:
    get_list()