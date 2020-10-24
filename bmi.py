h = int(input("vložte výšku v CM a stlačte ENTER"))
w = int(input("vložte váhu v kg a stlačte ENTER"))

def BMI():
    a= w/((h/100)*(h/100))
    if a <= 18.5:
        print("Podváha")
    elif a >= 18.5 and a <= 24.9:
        print("Normálna hmotnosť")
    elif a >= 25 and a <= 29.9:
        print("Nadváha")
    else:
        print("Obezita")
    return round(a, 2)

print("BMI pri výške", h, "m a hmotnosti", w, "kg je", BMI())
