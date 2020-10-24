currency = str(input("Vložte druh meny (USD alebo EUR)"))


def eur2usd():
    usd = eurToUsd * 1.19
    return usd


def usd2eur():
    eur = usdToEur * 0.84
    return eur


if currency == "EUR" or currency == "eur":
    eurToUsd = float(input("vložte hodnotu €"))
    print(eurToUsd, "€ =", eur2usd(), "$")
elif currency == "USD" or currency == "usd":
    usdToEur = float(input("vložte hodnotu €"))
    print(usdToEur, "$ =", usd2eur(), "€")
else:
    print("ZADANÁ NESPRÁVNA HODNOTA")
    
