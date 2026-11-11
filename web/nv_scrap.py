import requests as req
from bs4 import BeautifulSoup

response = req.get('https://news.naver.com')

print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

content = soup.select('.cnf_news_item')

print(content[0].text)

print("=== class로 선택, 반복문으로 텍스트 출력===")
for c in content:
    print(c.text)
    
