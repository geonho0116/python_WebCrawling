#시고저종, 봉차트(candle chart) 받아오기

import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url="https://finance.naver.com/item/main.nhn?code="+company_code#005930 삼성전자의 코드
    result=requests.get(url)
    bs_obj=BeautifulSoup(result.content,"html.parser")
    return bs_obj

#bs_obj를 받아 price를 return하는 함수
def get_price(company_code):
    bs_obj=get_bs_obj(company_code)
    td_first=bs_obj.find("p",{"class":"no_today"})
    blind=td_first.find("span",{"class":"blind"})
    return {"close":close, "high":high}
# company_codes = ["005930","000660","005680"]
# for item in company_codes:
#     print(get_price(item))
# print("삼성전자: "+get_price("005930")) #삼성전자
# print("sk하이닉스: "+get_price("000660")) #sk하이닉스
# print("삼영전자: "+get_price("005680")) #삼영전자

#봉차트 받아오기

def get_candle_chart_data(company_code):
    bs_obj=get_bs_obj(company_code)
    td_first=bs_obj.find("td",{"class":"first"})
    blind=td_first.find("span",{"class":"blind"})
    #close 종가(전일)
    close=blind.text
    return close

candle_chart_data = get_candle_chart_data("000660")
print(candle_chart_data)