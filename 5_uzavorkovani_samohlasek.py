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

class Character:
    vowels = ["a", "á", "e", "ě", "é", "i", "í", "o", "ó", "u", "ů", "ú", "y", "ý"]

    def __init__(self, character):
            self.__character = character

    def isVowel(self): #metoda
        if self.__character in Character.vowels:
            return True
        
with open("5_vystupni_text.txt", "w", encoding = "utf-8") as f:       
    for znak in text:
        ch = Character(znak.lower())
        if ch.isVowel() == True:
            f.write("(" + znak + ")")
        else:
            f.write(znak)



    