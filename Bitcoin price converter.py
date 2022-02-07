from forex_python.converter import CurrencyRates
a = CurrencyRates()

# logic block(currency conversion from usd to inr)
rs = a.convert("USD", "INR", 1.50)
print(rs)

#Bitcoin price converter
from forex_python.bitcoin import BtcConverter
b = BtcConverter()

# logic block(Bitcoins conversion from usd btc to inr rs)
r1 = b.convert_to_btc(50, "USD")
r2 = b.convert_btc_to_cur(5, "INR")
print(r1, r2, end="\n")

