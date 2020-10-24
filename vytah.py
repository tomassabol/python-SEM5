nPpl = int(input("Zadajte počet osôb a stlačte ENTER "))

totalWeight = 0

for i in range(nPpl):
    totalWeight += int(input("Zadajte hmotnosť jednotlivých osôb a zakaždým stlačte ENTER"))

if totalWeight <= 250:
    print("\U0001F7E2 , výťah nieje preťažený")
else:
    print("\U0001F534 , výťah je preťažený")
    
