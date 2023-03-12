def l100kmtompg(liters):
    #100000mt/1609,344mt=100KM en millas
    millasX100km=100000/1609.344
    galonXlitro=liters/3.785411784
    return millasX100km/galonXlitro

def mpgtol100km(miles):
    #millasX100Km
    x100km=miles*1.609344/100
    return 3.785411784/x100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))



