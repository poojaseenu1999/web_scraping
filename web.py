import requests
import bs4
res = requests.get('https://poojaseenu1999.github.io/epiczoowild/')
res.text
soup = bs4.BeautifulSoup(res.text, 'lxml')
hi =  soup.select('title')
print(hi.text)
for i in soup.select('title'):
    print(i.text)
