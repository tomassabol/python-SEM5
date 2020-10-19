#uloha #4

pocetZnamok = int(input("vložte počet známok a stlačte ENTER"))

sucetZnamok=0

for i in range(pocetZnamok):
    sucetZnamok += float(int(input("vložte známky z testov a zakaždým stlačte ENTER ")))

def priemerTestov():
    priemer=sucetZnamok/pocetZnamok
    return priemer

print("priemer tvojich známok je", priemerTestov())
print("tvoja vysledná známka bude", round(priemerTestov()))
