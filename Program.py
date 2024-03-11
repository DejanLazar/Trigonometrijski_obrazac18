import AziMethods
""" Ovo je primer Trigonometrrijskog obrasca broj 18, naime unosom koordinate prvih ta;aka, direkcionog ugla prve tacke
kao i ugla iymedju tacke koje se dogleda i ka kojoj se racuna, i duzinom izmedju dve tacke da se sracunaju koordinate te tacke
pocinje unosom broja tacaka koje se unose i na taj nacin racuna. Ulazni parametar mora da bude direkcioni ugao jer se on racuna u odnosu
na drugu poznatu tacku, te on se ne racuna u skript.
"""
#Unos broj tacaka
n = int(input("unesite broj poligonskih tacaka: "))
#Unos prvog direkcionog ugla u vidu tuple, a celobrojne vrednosti se odvajaju tackom
v = AziMethods.angle.Azimuth()
#Kreiranje istance klase Point sa ulaznim parametrima koordinata X i Y pocetne tacke
tacka = AziMethods.Point([41000,71000,v])

#loop ya broj tacaka i ispis koordinata
for i in range(n):
    tacka.NewPoint()
    print(f'Tacka {i+2}')
    print(tacka)

