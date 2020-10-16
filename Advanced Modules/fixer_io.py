import requests

api_key = "ee82a76f0ef185a9ef8d8c88be7f08d2"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

first_currency = input("First Currency:")
second_currency = input("Second Currency:")
amount = int(input("Amount:"))

response = requests.get(url)

infos = response.json()

firstValue = infos["rates"][first_currency]
secondValue = infos["rates"][second_currency]

print((secondValue / firstValue) * amount)