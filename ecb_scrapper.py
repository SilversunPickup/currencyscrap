import requests
import json
import csv

#Consume Data from the EZB (European Central Bank)
url  = "http://api.fixer.io/latest?=USD"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]
print("Date:", date, "\n")

rates = parsed["rates"]

#Give out the currency exchange rate in USD, EUR, GBP

bases = ["USD", "EUR", "GBP"]

for base in bases:
    url = "http://api.fixer.io/latest?base=" + base
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    rates = parsed["rates"]

    for currency, rate in rates.items():
        print(date, base, currency, rate)

x = 4
print(x)