import requests
from bs4 import BeautifulSoup

url_stats = 'https://sg.finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://sg.finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://sg.finance.yahoo.com/quote/{}/financials?p={}'
url_quotes = 'https://sg.finance.yahoo.com/quote/{}?p={}'

stock = 'TSLA'

response = requests.get(url_quotes.format(stock, stock))
soup = BeautifulSoup(response.text, 'html.parser')

# full_table = soup.select('#quote-summary > div.D\(ib\).W\(1\/2\).Bxz\(bb\).Pstart\(12px\).Va\(t\).ie-7_D\(i\).ie-7_Pos\(a\).smartphone_D\(b\).smartphone_W\(100\%\).smartphone_Pstart\(0px\).smartphone_BdB.smartphone_Bdc\(\$seperatorColor\) > table > tbody > tr:nth-child(1) > td.C\(\$primaryColor\).W\(51\%\)')
# print(full_table)
