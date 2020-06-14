from bs4 import BeautifulSoup as bs
import sys
import requests

URL = 'https://www.atomy.com:449/ca/Home/'
LOGIN_ROUTE = 'Account/Login?rpage=Home/Product/MallMain'

HEADERS ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 'origin': URL, 'referer': URL + LOGIN_ROUTE}

s = requests.session()

login_payload = {
    'userId': '<username>',
    'userPw': '<password>',
    '__RequestVerificationToken': '<verifycationtoken from dev tools>'
}

login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)

cookies = login_req.cookies

soup = bs(s.get(URL + 'Product/ProductView?GdsCode=' + sys.argv[1]).text, 'html.parser')
print(soup)
