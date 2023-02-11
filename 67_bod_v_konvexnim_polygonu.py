import turtle

#vrcholy mnohouhelniku
vrcholy = [(0,0),(100,0),(100,100),(0,100)]

#hledany bod
b = (-100,30)

def najdi_teziste(seznam_vrcholu):
    pocet_stran = len(seznam_vrcholu)

    soucet_x = 0
    soucet_y = 0
    for item in seznam_vrcholu:
        soucet_x = soucet_x + item[0]   
        soucet_y = soucet_y + item[1]  

    tx = soucet_x/pocet_stran
    ty = soucet_y/pocet_stran

    return tx,ty

T = najdi_teziste(vrcholy)


#nakresleni mnohouhelniku
for vrchol in vrcholy:
    turtle.setpos(vrchol)
turtle.setpos(vrcholy[0])

#nakresli hledany bod
turtle.penup()
turtle.setpos(b)
turtle.pendown()
turtle.dot()

#nakresli teziste
turtle.penup()
turtle.setpos(T)
turtle.pendown()
turtle.dot("red")

turtle.exitonclick()

#vyjadri obecnou primku hrany
def primka_obecne(bod1, bod2):
    a = bod1[1] - bod2[1]
    b = bod1[0] - bod2[0]
    c = ((bod1[0])*(bod2[1])) - ((bod1[1])*(bod2[0]))
    koeficienty = [a,b,c]

    return koeficienty

#nevim jak to udelat
# def vytvor_hrany(seznam_vrcholu):
#     seznam_hran = []
#     for item in seznam_vrcholu:
#         hrana = []

hrany = [[(0,0),(100,0)],[(100,0),(100,100)], [(100,100),(0,100)],[(0,100),(0,0)]]

#vraci True pokud je bod ve stejne polorovine jako teziste
def poloha_bodu_k_hrane(teziste, koeficienty, bod):
    xt = teziste[0]
    yt = teziste[1]

    xb = bod[0]
    yb = bod[1]

    a = koeficienty[0]
    b = koeficienty[1]
    c = koeficienty[2]

    poloha_teziste = a*xt + b*yt + c
    poloha_bodu = a*xb + b*yb + c

    if (poloha_teziste < 0 and poloha_bodu < 0) or (poloha_teziste > 0 and poloha_bodu > 0):
        return True
    
    elif poloha_bodu == 0:
        return "hrana" #doresiiiiiit
    
    else:
        return False

 
seznam_boolu = []
for hrana in hrany:
    k = primka_obecne(hrana[0], hrana[1])
    bool = poloha_bodu_k_hrane(T,k,b)
    seznam_boolu.append(bool)

def bod_uvnitr(seznam):
    prvni_prvek = seznam[0]
    je_stejny = True
    for item in seznam:
        if prvni_prvek != item:
            je_stejny =  False
            break
    if je_stejny == True:
        return True
    else:
        return False

if bod_uvnitr(seznam_boolu) == True:
    print("Zadaný bod se nachází uvnitř konvexního mnohoúhelníku.")

else:
    print("Zadaný bod se nachází vně konvexního mnohoúhelníku.")



