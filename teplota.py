#úloha #8 - teplota.py

teplotaC = int(input("vložte teplotu v C a stlačte ENTER"))

def c2f():
    x = teplotaC*(9/5)+32
    return x

print(teplotaC,"C =", float(c2f()), "F")
