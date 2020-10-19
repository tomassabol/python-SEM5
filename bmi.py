#uloha #5 - \bmi.py

h = int(input("vložte výšku v CM a stlačte ENTER"))
w  = int(input("vložte váhu v kg a stlačte ENTER"))

def BMI():
    a= w/((h/100)*(h/100))
    return round(a,2)

print("BMI pri výške", h, "m a hmotnosti", w, "kg je", BMI())
