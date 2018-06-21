import requests
import json
import csv

## Consume Data from the EZB (European Central Bank)
##TODO Create Account on page https://fixer.io/ to have access json for currency exchange
url  = ""

response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]
print("Date:", date, "\n")
rates = parsed["rates"]

## Give out the currency exchange rate in USD, EUR, GBP

bases = ["USD", "EUR", "GBP"]

with open('rates.csv', 'w+') as f:  # Use 'wb' mode in python 2
    w = csv.DictWriter(f, ['date', 'base', 'currency', 'rate'])
    w.writeheader()
    for base in bases:
        ##TODO Add fixer.io data
        url =  "" + base
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)

        rates = parsed["rates"]

        for currency, rate in rates.items():
            w.writerow({'date': date,'base': base, 'currency':currency, 'rate':rate})