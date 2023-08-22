from json import load
with open("C:\\Users\\user\\Desktop\\python_codes\\currencyExchange\\db copy.json","r",encoding="UTF-8") as f:
    data=load(f)
rates=data.get("conversion_rates")

amount=int(input("Enter an amount:>"))
fromCurrencycode=input("enter source currency code:>")
toCurrencycode=input("enter designation currency code:>")
fro=rates.get(fromCurrencycode)
to=rates.get(toCurrencycode)
EU=3(amount/fro)*to
print(EU)

