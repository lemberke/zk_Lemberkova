#vyjimka proti otevreni prazdneho nebo neexistujiciho souboru
try:
    with open("5_vstupni_text.txt", encoding = "utf-8") as f:
        assert(len(f.readlines()) > 0)
    with open("5_vstupni_text.txt", encoding = "utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("Soubor, který chcete otevřít, neexistuje.")
    quit()
except AssertionError:
    print("Ve vstupním souboru nejsou žádná data.")
    quit()

#vytvoreni tridy "Character", ktera obsahuje staticky seznam samohlasek
class Character:
    vowels = ["a", "á", "e", "ě", "é", "i", "í", "o", "ó", "u", "ů", "ú", "y", "ý"]

#inicializace
    def __init__(self, character):
            self.__character = character

#metoda isVowel porovnava nacteny znak se seznamem samohlasek a rozhodne, jestli je dany znak samohlaska
    def isVowel(self):
        if self.__character in Character.vowels:
            return True

#otevreni souboru "5_vystupni_text.txt" pro psani       
with open("5_vystupni_text.txt", "w", encoding = "utf-8") as f:  
#prochazeni jednotlivych znaku v souboru a pokud to jsou samohlasky, napisi se do souboru ohranicene zavorkami a pokud to jsou jine znaky, napisi se do souboru v nezmenenne podobe     
    for znak in text:
        ch = Character(znak.lower())
        if ch.isVowel() == True:
            f.write("(" + znak + ")")
        else:
            f.write(znak)



    