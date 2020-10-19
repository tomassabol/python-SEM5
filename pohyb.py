s = int(input('Zadaj dráhu vozíčka v metroch a stlač ENTER:'))
t = int(input('Zadaj čas v sekundách, za ktorý ju vozíček prejde a stlač ENTER:'))

def rychlost():
    v = s/t
    return round(v,2)

print("Rýchlosť vozíčka je", rychlost() , "m/s")
