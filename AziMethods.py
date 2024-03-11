import math
#ovde su staticke metode koje koristim
class angle:
    #Pretvaranje tuple sa uglovima u radijanma
    @staticmethod
    def Ang2Rad(angle):
        return round(math.radians(angle[0]+ angle[1]/60+angle[2]/3600),20)
    #Pretvaranje radijana u tuple uglova (stepen, minut,sekund)
    @staticmethod
    def Rad2Ang(angle):
        _angle = math.degrees(angle)
        _D = int(round(_angle,0))
        _M = int(round(((_angle-_D)*60),0))
        _S = int(round(((_angle-_D-_M/60)*3600),0))
        return((_D,_M,_S))
    #Unis novog direkcionog ugla
    @staticmethod
    def Azimuth():
        while True:
            try:
                angle =  tuple(map(int, input("Unesite direkcioni ugao u obliku D,M,S: ").split('.')))
                if (angle[0] >=360 and angle[0] <0 ) or (angle[1] >=60 and angle[1] <0 ) or (angle[2]>=60 and angle[1] <0 ):
                    raise Exception ("Niste dobro uneli vrednosti ugolova")
                else:
                    return angle
            except ValueError:
                print("Potrebno je uneti celobrojne vrednosti uglova")
    #racunanje sledeceg direkcionog ugla sledece tagle prelomni plus direkcioni, i ako je taj ybir veci od 180 oduzima se 180, ako nije dodaje se 180
    @staticmethod
    def nextAzimuth( direkcioni, prelomni):
        if (prelomni+direkcioni) >= round(math.pi,20):
            direkcioni = direkcioni+prelomni- round(math.pi,20)
            return direkcioni
        else:
            direkcioni = direkcioni+prelomni + round(math.pi,20) 
            return direkcioni
    
    
#Klasa Tacka    
class Point:
    
    def __init__(self, tup):
        self.tup = tup
        #ne unosi se cetvrti elemenat liste, ali da mi ne bi izbacivao gresku konstruktorom sam je odmah appendovao
        self.tup.append(0)  
    #Stampanje info o tacki
    def __str__(self):
        return f'Koordinata X je {self.tup[0]}, dok je koordinata Y {self.tup[1]}, Azimuth ka predhodnoj tački je {self.tup[2]}, dok je prelomni ugao u ovoj tacki {self.tup[3]}' 
    
    def NewPoint(self):
        #Unos distance izmedju date tacke i sledece tacke
        distanca = float(input("Unesite duzinu poligonskog vlaka: "))
        #Unos prelomnog ugla na datoj tacki
        self.tup[3] = angle.Azimuth() 
        #Racunanje direkcionog ugla ka sledecoj tacki               
        self.tup[2] = angle.Rad2Ang(angle.nextAzimuth(angle.Ang2Rad(self.tup[2]),angle.Ang2Rad(self.tup[3])))
        #Racunanje x i y promena ka sledecoj tacki
        x = math.cos(angle.Ang2Rad(self.tup[2]))*distanca
        y = math.sin(angle.Ang2Rad(self.tup[2]))*distanca
        print("Promena po X iznosi: ",round(x,2))
        print("Promena po Y iznosi: ",round(y,2))
        #Racunanje vrednosti sledece tacke
        self.tup[0] = round(self.tup[0]+x,2)
        self.tup[1] = round(self.tup[1]+y,2)
        return [self.tup[0],self.tup[1],self.tup[2], self.tup[3]]
    
