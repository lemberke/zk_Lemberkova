import turtle

class Point:
    def __init__(self, souradnice_x, souradnice_y):
        self.__souradnice_x = souradnice_x 
        self.__souradnice_y = souradnice_y

    def getx(self):
        return self.__souradnice_x
    
    def gety(self):
        return self.__souradnice_y

class Line:
    def __init__(self, bod_A, bod_B):
        self.__bod_A = bod_A
        self.__bod_B = bod_B

        self.a = self.__bod_A.getx() - self.__bod_B.gety()
        self.b = self.__bod_A.gety() - self.__bod_B.getx()
        self.c = ((self.__bod_A.getx())*(self.__bod_B.gety())) - ((self.__bod_A.gety())*(self.__bod_B.getx()))


    def poloha_bodu_k_hrane(self, teziste, bod):    
        poloha_teziste = self.a*teziste.getx() + self.b*teziste.gety() + self.c
        poloha_bodu = self.a*bod.getx() + self.b*bod.gety() + self.c

        if (poloha_teziste < 0 and poloha_bodu < 0) or (poloha_teziste > 0 and poloha_bodu > 0):
            return "uvnitr"
        
        elif poloha_bodu == 0:
            return "hrana"
        
        else:
            return "vne"
        

class Polygon:
    def __init__(self, *v): 
        self.__pocet_vrcholu = len(v)
        if len(v) < 3:
            raise Exception("Zadany utvar neni mnohouhelnik, protoze ma mene nez 3 vrcholy")
        
        self.__vrcholy = v

        self.seznam_hran = []
        for i, vrchol in enumerate(self.__vrcholy):
            self.seznam_hran.append(Line(self.__vrcholy[i-1],vrchol))

        self.__T = self.najdi_teziste()
            
    def najdi_teziste(self):
        soucet_x = 0
        soucet_y = 0
        for item in self.__vrcholy:
            soucet_x = soucet_x + item.getx()    
            soucet_y = soucet_y + item.gety()  

        tx = soucet_x/self.__pocet_vrcholu
        ty = soucet_y/self.__pocet_vrcholu

        return Point(tx,ty)
    
    def poloha_bodu(self, bod):
        bod_na_hrane = 0
        for hrana in self.seznam_hran:
            poloha = hrana.poloha_bodu_k_hrane(self.__T, bod)

            if poloha == "vne":
                return "Bod se nachazi vne mnohouhelniku."

            elif poloha == "hrana":
                bod_na_hrane += 1

        if bod_na_hrane > 0:
            return "Bod lezi na hrane."
        
        else:
            return "Bod se nachazi uvnitr mnohouhelniku."
        
with open("67_vrcholy_a_bod.txt") as f:
    data = f.read()
    seznam_dat = data.split("\n")
    seznam_bodu = []

    for bod in seznam_dat:
        x, y = bod.split(",")
        seznam_bodu.append(Point(float(x),float(y)))
            
    bod = seznam_bodu[-1]
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






