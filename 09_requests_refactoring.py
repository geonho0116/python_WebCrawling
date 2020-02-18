#리팩토링:구조를 이쁘게 바꾸면서 기능은 유지하는 것
#crawling
import requests
from bs4 import BeautifulSoup
#url을 넣어서 bs_obj를 리턴하는 함수
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj=BeautifulSoup(result.content,"html.parser")
    return bs_obj
#회사코드를 입력하면 주가를 알려주는 함수
def get_price(company_code):
    url="https://finance.naver.com/item/main.nhn?code="+company_code
    bs_obj=get_bs_obj(url)
    no_today = bs_obj.find("p",{"class":"no_today"})
    blind=no_today.find("span",{"class":"blind"})
    return blind.text

price_samsung = get_price("005930") 
price_sk_hynix=get_price("000660")
print(price_samsung)
print(price_sk_hynix)
