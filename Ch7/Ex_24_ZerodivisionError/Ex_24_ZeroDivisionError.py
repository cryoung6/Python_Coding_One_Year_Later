from bs4 import BeautifulSoup
from urllib.request import urlopen
usd, gbp, gbpex = 10.0, 20.0, 0.00
html2 = urlopen('https://usd.fxexchangerate.com')
soup2 = BeautifulSoup(html2, 'lxml')
tables2 = soup2.findChildren('td')
try:
    gbpex = float(tables2[3].string[:6])
    gbp = gbp/gbpex
    print("gbp converted to USD is:", gbp)
except ZeroDivisionError:
    print('ZeroDivisionError where gbpex is:', gbpex)
