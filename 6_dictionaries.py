
countries_rates = {"Colombia":5,
                   "Spain":5,
                   "Mexico":3,
                   "Malaysia":4,
                   }



countries_rates_mod = countries_rates.copy()
print(countries_rates_mod.keys())
print(countries_rates_mod.values())
print(countries_rates_mod.items())


countries_rates_mod.pop("Spain")

print(countries_rates_mod.popitem())
print(countries_rates_mod.get("Colombia"))
print(countries_rates)
print(countries_rates_mod)

markets: dict[str, dict[str, float | int]] = {"US":{"AAPL":150.89,
                 "AMZN":125.23,
                 "NVDA":155.23,
                 "O":57.55},
           "EUR":{"SAP":50.09,
                 "NOVO":15.13,
                 "DGE":95.25,
                 "SIEM":15.29},
           "APAC":{"NIKEI":1585,
                   "SHANGAI":1960,
                   "BURSA":1578}}

print(markets.items())
print(markets["US"]["AAPL"])




