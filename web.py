import requests
import bs4
res = requests.get('https://poojaseenu1999.github.io/epiczoowild/')

soup = bs4.BeautifulSoup(res.text, 'lxml')


for i in soup.select('img'):
    print(i)
