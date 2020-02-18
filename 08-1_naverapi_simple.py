import requests
from urllib.parse import urlparse

keyword="디퓨저"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                        headers={"X-Naver-Client-Id":"dnogUSKTMPAovSEL4NNw",
                                "X-Naver-Client-Secret":"of5rOpfUt2"
                               })
json_obj=result.json()
print(json_obj)