num1 = float(input("Vložte číslo"))
num2 = float(input("Opäť vložte číslo"))
fn = input("Vložte funkciu")


def result():
    if fn == "+":
        return (num1 + num2)
    elif fn == "-":
        return (num1 - num2)
    elif fn == "*":
        return (num1 * num2)
    elif fn == "/":
        return (num1 / num2)
    else:
        return ("\U000026A0 ZADANÁ NESPRÁVNA OPERÁCIA \U000026A0!")


print(result())
