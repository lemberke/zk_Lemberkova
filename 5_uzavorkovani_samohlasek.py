# Zkouška z úvodu do programování
# Úloha 5: Uzávorkování samohlásek
# Eva Lemberková, MOBIBO, 2. ročník

#výjimka proti otevření prázdného nebo neexistujícího souboru
try:
    with open("5_vstupni_text.txt", encoding = "utf-8") as f:
        assert(len(f.readlines()) > 0)
except FileNotFoundError:
    print("Soubor, který chcete otevřít, neexistuje.")
    quit()
except AssertionError:
    print("Ve vstupním souboru nejsou žádná data.")
    quit()

#otevření vstupního souboru "5_vstupni_text.txt" pro čtení a načtení ho do proměnné "text"
with open("5_vstupni_text.txt", encoding = "utf-8") as f:
        text = f.read()

#vytvoření třídy "Character", která obsahuje statický seznam samohlásek
class Character:
    vowels = ["a", "á", "e", "ě", "é", "i", "í", "o", "ó", "u", "ů", "ú", "y", "ý"]

#inicializace třídy
    def __init__(self, character):
            self.__character = character

#metoda isVowel porovnává načtený znak se seznamem samohlásek a rozhodne, jestli je daný znak samohláska
    def isVowel(self):
        if self.__character in Character.vowels:
            return True
        else:
             return False

#otevření souboru "5_vystupni_text.txt" pro psaní       
with open("5_vystupni_text.txt", "w", encoding = "utf-8") as f:  
#procházení jednotlivých znaků v souboru a jejich rozdělění do 4 kategorií podle dvou aspektů (jestli jsou to samohlásky a jestli i předchozí znak byl samohláska) 
#na základě zařazení do konkrétní kategorie se vypíší/nevypíší závorky do výstupního souboru 
    previous_vowel = False
    for znak in text:
        ch = Character(znak.lower()) #všechny znaky jsou procházeny jako malá písmena
   
        if ch.isVowel() == True and previous_vowel == False:
            f.write("(" + znak)
            previous_vowel = True
        
        elif ch.isVowel() == True and previous_vowel == True:
            f.write(znak)
            previous_vowel = True

        elif ch.isVowel() == False and previous_vowel == True:
            f.write(")" + znak) 
            previous_vowel = False 

        else:
            f.write(znak)
            previous_vowel = False

#připíše na konec textu závorku, pokud je posledním znakem samohláska
    if previous_vowel == True:
         f.write(")")
            



    