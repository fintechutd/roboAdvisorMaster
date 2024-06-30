## News API key: 79d0212e281147e4bb2f1898ad5a5708

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'country=us&'
       'from=2024-04-04&'
       'sortBy=popularity&'
       'apiKey=79d0212e281147e4bb2f1898ad5a5708')

response = requests.get(url)

print (response.json())