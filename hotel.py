#uloha #6 - hotel.py

numPpl = int(input("vložte počet osôb a stlačte ENTER"))
numNghts = int(input("vložte počet nocí a stlačte ENTER"))

noc = 30
strava = 15

def cena(types):
    a = types*numPpl
    return a

for i in range(numNghts):
    x=cena(noc)*(i+1)
    y=cena(strava)*(i+1)
    spolu=(x+y)

def nights():
  if numNghts == 1:
    return("noc")
  elif numNghts < 5:
    return("noci")
  else:
    return("nocí")

print("za", numNghts ,nights(),"zaplatíte:")
print("spolu za ubytovanie:", x,"€ ,spolu za stravu",y, "€ ,ubytovanie + strava spolu:",spolu,"€")
