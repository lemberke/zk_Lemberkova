# Zkouška z úvodu do programování
# Úloha 5: Uzávorkování samohlásek
# Eva Lemberková, MOBIBO, 2. ročník

#an exception against opening an empty or non-existing file
try:
    with open("5_vstupni_text.txt", encoding = "utf-8") as f:
        assert(len(f.readlines()) > 0)
except FileNotFoundError:
    print("The file you are trying to open does not exist.")
    quit()
except AssertionError:
    print("You are opening an empty file.")
    quit()

#opening input file "5_vstupni_text.txt" for reading and loading it to the variable "text"
with open("5_vstupni_text.txt", encoding = "utf-8") as f:
        text = f.read()

#class "Character", which contains static list of the vowels
class Character:
    vowels = ["a", "á", "e", "ě", "é", "i", "í", "o", "ó", "u", "ů", "ú", "y", "ý"]

#inicialization of the class
    def __init__(self, character):
            self.__character = character

#method isVowel compares the actual charecter with the list "vowels" and if the character is a vowel it returns "True"
    def isVowel(self):
        if self.__character in Character.vowels:
            return True
        else:
             return False

#opening an output file "5_vystupni_text.txt" for writing      
with open("5_vystupni_text.txt", "w", encoding = "utf-8") as f:  
#going through the characters in the text and dividing them to categories according to the previous chararacter and according to the output of the function "isVowel" 
#according to the category, the brackets are printed or not to the output file
    previous_vowel = False
    for character in text:
        ch = Character(character.lower()) #all characters are represented as lower
   
        if ch.isVowel() == True and previous_vowel == False:
            f.write("(" + character)
            previous_vowel = True
        
        elif ch.isVowel() == True and previous_vowel == True:
            f.write(character)
            previous_vowel = True

        elif ch.isVowel() == False and previous_vowel == True:
            f.write(")" + character) 
            previous_vowel = False 

        else:
            f.write(character)
            previous_vowel = False

#adds a bracket if the last character of the text is a vowel
    if previous_vowel == True:
         f.write(")")
            



    