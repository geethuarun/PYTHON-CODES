rates={  
    "USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
    "BAM": 1.,
    "INR":82.0914
    }
#currency exchange rate aplcatn
amount=int(input("enter the amount:>"))
fromCurrencycode=input("enter source currency code:>")
toCurrencycode=input("enter designation currency code:>")
fro=rates.get(fromCurrencycode)
to=rates.get(toCurrencycode)
EU=(amount/fro)*to
print(EU)


