# Zkouška z úvodu do programování
# Úloha 67: Test, jestli se bod nachází uvnitř, vně nebo na hraně konvexního mnohoúhelníku
# Eva Lemberková, MOBIBO, 2. ročník

import turtle

#vytvori se class "Point", kde je kazdy objekt charakterizovan souradnicemi x a y
class Point:
    def __init__(self, souradnice_x, souradnice_y):
        self.__souradnice_x = souradnice_x 
        self.__souradnice_y = souradnice_y

    #metoda "getx()" umoznuje ziskat souradnici x z objektu tridy "Point"  
    def getx(self):
        return self.__souradnice_x

    #metoda "gety()" umoznuje ziskat souradnici y z objektu tridy "Point"  
    def gety(self):
        return self.__souradnice_y

#vytvori se class Line, ktera je charakterizovana dvema body
class Line:
    def __init__(self, bod_A, bod_B):
        self.__bod_A = bod_A
        self.__bod_B = bod_B

    #po dosazeni souradnic x a y obou bodu, jsou podle vzorce vypocitany koeficienty, pomoci kterych muze byt primka vyjadrena obecne
        self.a = self.__bod_A.gety() - self.__bod_B.gety()
        self.b = self.__bod_A.getx() - self.__bod_B.getx()
        self.c = ((self.__bod_A.getx())*(self.__bod_B.gety())) - ((self.__bod_A.gety())*(self.__bod_B.getx()))

    #funkce "poloha_bodu_k_hrane" ma parametry souradnice teziste (T) a analyzovany bod(B) a urci, jestli jakou polohu ma analyzovany bod vuci polorovine dane tezistem a hranou
    def poloha_bodu_k_hrane(self, T, B):    
        poloha_teziste = self.a*T.getx() + self.b*T.gety() + self.c #vyjadrena rovnice poloroviny dane hranou a tezistem
        poloha_bodu = self.a*B.getx() + self.b*B.gety() + self.c #vyjadrena rovnice poloroviny dane hranou a bodem

        #pokud jsou hodnoty rovnice poloroviny po dosazeni souradnic teziste a bodu obe zaporne nebo obe kladne, znamena to ze lezi ve stejne polorovine a tedy uvnitr mnohouhelniku -> funkce vraci string "uvnitr" 
        if (poloha_teziste < 0 and poloha_bodu < 0) or (poloha_teziste > 0 and poloha_bodu > 0):
            return "uvnitr"

        #pokud je hodnota promenne "poloha_bodu" rovna nule, znamena to, ze bod lezi na primce, jejiz soucasti je hrana -> funkce vraci string "hrana"  
        elif poloha_bodu == 0:
            return "hrana"

        #ve zbytku pripadu to znamena, ze se bod nachazi vne -> funkce vraci string "vne"      
        else:
            return "vne"
        
#vytvori se trida "Polygon" charakterizovana neurcitym poctem vrcholu mnohouhelniku
class Polygon:
    def __init__(self, *v): 
        self.__pocet_vrcholu = len(v)

        #pokud je vrcholu mene nez 3, je vyvolana vyjimka, protoze dany utvar neni mnohouhelnik
        if len(v) < 3:
            raise Exception("Zadany utvar neni mnohouhelnik, protoze ma mene nez 3 vrcholy")
        
        self.__vrcholy = v

        #vytvori se seznam hran, kam se pridaji vsechny hrany mnohouhelniku
        self.seznam_hran = []
        for i, vrchol in enumerate(self.__vrcholy):
            self.seznam_hran.append(Line(self.__vrcholy[i-1],vrchol))

        #je inicializovano teziste daneho polygonu pomoci funkce "najdi_teziste"
        self.__T = self.najdi_teziste()

    #metoda "najdi_teziste" pomoci vzorce vypocita teziste daneho mnohouhelniku       
    def najdi_teziste(self):
        soucet_x = 0
        soucet_y = 0
        for item in self.__vrcholy:
            soucet_x = soucet_x + item.getx()    
            soucet_y = soucet_y + item.gety()  

        tx = soucet_x/self.__pocet_vrcholu
        ty = soucet_y/self.__pocet_vrcholu

        return Point(tx,ty)
    
    #metoda "poloha_bodu" provede pro kazdou hranu metodu "poloha_bodu_k_hrane" a podle kombinace vysledku u konkretniho polygonu urci polohu bodu vuci mnohouhelniku
    def poloha_bodu(self, hledany_bod):
        bod_na_hrane = 0
        for hrana in self.seznam_hran:
            poloha = hrana.poloha_bodu_k_hrane(self.__T, hledany_bod)

            #pokud se bod nachazi vne alespon vuci jedne polorovine dane hranou a tezistem, znamena to, ze lezi vne mnohouhelniku
            if poloha == "vne":
                return "Bod leží vně mnohoúhelníku."

            elif poloha == "hrana":
                bod_na_hrane += 1

        #pokud se bod nachazi na primce dane hranou a uvnitr alespon jedne dalsi poloroviny dane hranou a tezistem, znamena to, ze lezi na hrane
        if bod_na_hrane > 0:
            return "Bod leží na hraně mnohoúhelníku."
        
        #ve zbytku pripadu to znamena, ze bod lezi uvnitr mnohouhelniku
        else:
            return "Bod leží uvnitř mnohouhelníku."
        
#vyjimka proti otevreni prazdneho nebo neexistujiciho souboru
try:
    with open("67_vrcholy_a_bod.txt", encoding = "utf-8") as f:
        assert(len(f.readlines()) > 0)
except FileNotFoundError:
    print("Soubor, který chcete otevřít, neexistuje.")
    quit()
except AssertionError:
    print("Ve vstupním souboru nejsou žádná data.")
    quit()

#otevreni souboru "67_vrcholy_a_bod.txt" pro cteni a nacteni jeho obsahu do promenne "data"       
with open("67_vrcholy_a_bod.txt", encoding = "utf-8") as f:
    data = f.read()

    #ulozeni dat do seznamu
    seznam_dat = data.split("\n")

    #vytvoreni seznamu bodu, do ktereho jsou pridany body ze seznamu "seznam_dat", ale jsou prevedene do tridy "Point"
    seznam_bodu = []
    for bod in seznam_dat:
        x, y = bod.split(",")
        seznam_bodu.append(Point(float(x),float(y)))

    #vytvoreni objektu "bod" tridy "Point", ktery je v seznamu bodu umisten jako posledni a predstavuje bod, jehoz polohu chceme zjistit        
    bod = seznam_bodu[-1]

    #vytvoreni objektu "polygon" tridy "Polygon", ktery je charakterizovan seznamem bodu od nulteho prvku po predposledni a tyto prvky predstavuji jeho vrcholy
    polygon = Polygon(*seznam_bodu[0:-1])

    print(polygon.poloha_bodu(bod))

    #nakresleni mnohouhelniku
    for vrchol in polygon._Polygon__vrcholy:
        turtle.setpos(vrchol.getx(),vrchol.gety())
    turtle.setpos(polygon._Polygon__vrcholy[0].getx(),polygon._Polygon__vrcholy[0].gety())

    #nakresli hledany bod
    turtle.penup()
    turtle.setpos(bod.getx(),bod.gety())
    turtle.pendown()
    turtle.dot()

    #nakresli teziste
    turtle.penup()
    turtle.setpos(polygon._Polygon__T.getx(),polygon._Polygon__T.gety())
    turtle.pendown()
    turtle.dot("red")

    turtle.exitonclick()






