#uloha 10 - prevodnik.py

cm = int(input("Zadaj dĺžku v centimetroch a stlač ENTER"))

def cm2inch():
    a=cm/2.54
    return round(a,2)

def cm2ft():
    b=cm/30.48
    return round(b,2)

def cm2yd():
    c=cm/91.44
    return round(c,2)

def cm2mi():
    d=cm/161000
    return round(d,4)



print(cm,"cm=", cm2inch(),"inches,",cm2ft(),"feet,",cm2yd(),"yards and",cm2mi(),"miles")
