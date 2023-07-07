import requests
from bs4 import BeautifulSoup

res=requests.get('https://news.ycombinator.com/news')
# we get the page through requests
print("res",res) #-- returns 200 - the response of the html page
# print("res.text",res.text)
# Beautiful soup can parse html,xml etc
soup=BeautifulSoup(res.text,'html.parser')
# print("soup",soup)
# using soup we can target separate html eg:get  onlty the body content in a list
# print("soup.body",soup.body)
# get all the divs in the page
# print(soup.find_all('div'))

# get all the anchors in the page
# print("soup.a",soup.find_all('a'))

# use css selectors to get specific data
# print(soup.select('.titleline'))

# get the first from the page
links=soup.select('.titleline')
votes=soup.select('.score')
print(votes[0])