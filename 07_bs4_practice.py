import bs4

html_str="""
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
        <div>
            <ul>
                <li>open</li>
                <li>close</li>
            </ul>
        </div>
    </body>
</html>
"""
bs_obj= bs4.BeautifulSoup(html_str,"html.parser")
#tag:태그 ex) <ul></ul> <li></li> <div></div> <a></a>
#property:속성 ex) class="greet" class="reply" href title src
#property value:속성값 ex)greet reply
#<a href="www.naver.com">네이버</a>
#태그-<a></a> 속성-href 속성값-www.naver.com
#
#
hello=bs_obj.find("li")
lis=bs_obj.findAll("li")
# for li in lis:
#     print(li.text)
ul_reply=bs_obj.findAll("ul",{"class":"reply"})
lis1=ul_reply.findAll("li")
print(lis1)