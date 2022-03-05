# Michael Vaden, mtv2eva
import requests
import sys

url = "https://yfapi.net/v6/finance/quote"

argv = sys.argv[1]

stocks = argv.split(",")

headers = {
    'x-api-key': "VQC0wRwpPB7SN3nOlW4UT3XhN2X1H9Kf2w5Yb8Mi"
}

for i in range(len(stocks)):
    querystring = {"symbols": stocks[i]}
    response = requests.request("GET", url, headers=headers, params=querystring)

    stock_json = response.json()
    try:
        name = stock_json['quoteResponse']['result'][0]['longName']
        price = stock_json['quoteResponse']['result'][0]['regularMarketPrice']
        print(name, ": ", price)

    except:
        print("Incorrect ticker input")