# len() - find how much is the leigth in the list
# isalpha - checks if input is letters
# isnumeric - checks if input is numbers

# from random import *
# sõne="Programmeerimine"
# print(sõne)
# # read by letters
# sõne_list=list(sõne)
# print(sõne_list)
# # reverses
# sõne_list.reverse()
# print(sõne_list)
# # finds input letters
# print(sõne_list.index("P"))
# # how many in a list
# print(len(sõne_list))
# # How many in a word
# print(len(sõne))
# # counts letters in m
# kogus_m=sõne_list.count("m")
# # deletes in m range letters "m"
# for m in range(kogus_m):
#     sõne_list.remove("m")
# # we are inserting numeric in the end of the list
# tähed=randint(1, 6)
# for i in range(tähed):
#     while 1:
#         try:
#             t=input("Sisesta täht: ")
#             if t.isalpha(): break
#         except:
#             print("On vaja täht!")
#     sõne_list.append(input(t))
# print(sõne_list)


# tähed=randint(1, 6)
# for i in range(tähed):
#     while 1:
#         try:
#             t=input("Sisesta täht: ")
#             if t.isalpha(): break
#         except:
#             print("On vaja täht!")
#     while 1:
#         try:
#             ind=input("Sisesta index: ")
#             if ind.isnumeric() & int(ind)<len(sõne_list): break
#         except:
#             print("On vaja index!")
#     sõne_list.insert(int(ind), t)
# print(sõne_list)
# def function(e):
#     return len(e)
# # sorts the list by the function
# sõne_list.sort(reverse=True, key=function)
# print(sõne_list)

# # work that I have to finish at home
# # just a test
# word = "andestav"
# word_list = list(word)
# print(word_list)
# # first
# word_list.title()
# print(word_list)
# # second
# word_list.capitalize()
# print(word_list)
# # third
# if word_list.isnumeric():
#     print("YAY!")
# else:
#     print("See on kõik, MA plahvatan!")
# # fourth
# word_list.capitalize()
# print(word_list)
# # fifth
# word_list.swapcase()
# print(word_list)
# # sixth
# word_list.rjust(7, fillchar="scatman")
# print(word_list)
# # seventh
# word_list.ljust(7, fillchar="scatman")
# print(word_list)
# # eight
# word_list.center(20)
# print(word_list)
# # ninth
# word_list.zfill(10)
# print(word_list)
# # tenth
# if word_list.isspace():
#     print("YAY!")
# else:
#     print("See on kõik, MA plahvatan!")


# print("1. title")
# print("2. capitalize")
# print("3. isnumeric")
# print("4. len")
# print("5. swapcase")
# print("6. rjust")
# print("7. ljust")
# print("8. center")
# print("9. zfill")
# print("10. isspace")
# print()

# try:
#     question_func=int(input("Sisesta milline funktion te tahate?: "))
#     if question_func > 10 & question_func <= 0:
#         print("Vale! Provi uuesti")
#     else:
#         print("Väga hea!")
# except:
#     print(">:/")

# while True:
#             if question_func==1:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 worduser_list.title()
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==2:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 worduser_list.capitalize()
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==3:
#                 worduser=input("Sisesta sinu sõna (proovi kirjutamine numberidega ja numprideta): ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 if worduser_list.isnumeric():
#                     print("YAY!")
#                 else:
#                     print("See on kõik, MA plahvatan!")
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==4:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 len(worduser_list)
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==5:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 worduser_list.swapcase()
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break
        
#             elif question_func==6:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 putwhateveryouwantidc=input("Sisesta sinu fillchar: ")
#                 worduser_list.rjust(100, fillchar=putwhateveryouwantidc)
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==7:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 putwhateveryouwantidc=input("Sisesta sinu fillchar: ")
#                 worduser_list.ljust(100, fillchar=putwhateveryouwantidc)
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==8:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 putwhatevernumberyouwantidc=input(int("Sisesta sinu fillchar: "))
#                 worduser_list.center(putwhatevernumberyouwantidc)
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==9:
#                 worduser=input("Sisesta sinu sõna: ")
#                 print(worduser)
#                 worduser_list = list(worduser)
#                 putwhatevernumberyouwantidc=input(int("Sisesta sinu fillchar: "))
#                 worduser_list.zfill(putwhatevernumberyouwantidc)
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     question_func=int(input("Sisesta milline funktion te tahate?: "))
#                     if question_func > 10 & question_func <= 0:
#                         print("Vale! Provi uuesti")
#                 elif IWANTMOOORE == "ei":
#                     break

#             elif question_func==10:
#                 worduser=input("Sisesta sinu sõna (Proovi ja sisesta tühidega ja tühideta): ")
#                 print(worduser)
#                 if worduser_list.isspace():
#                     print("YAY!")
#                 else:
#                     print("See on kõik, MA plahvatan!")
#                 print(worduser_list)
#                 IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
#                 if IWANTMOOORE == "ja":
#                     print("1. title")
#                     print("2. capitalize")
#                     print("3. isnumeric")
#                     print("4. len")
#                     print("5. swapcase")
#                     print("6. rjust")
#                     print("7. ljust")
#                     print("8. center")
#                     print("9. zfill")
#                     print("10. isspace")
#                     print()
#                     try:
#                         question_func=int(input("Sisesta milline funktion te tahate?: "))
#                         if question_func > 10 & question_func <= 0:
#                             print("Vale! Provi uuesti")
#                         else:
#                             print("Väga hea!")
#                     except:
#                         print(">:/")
#                 elif IWANTMOOORE == "ei":
#                     break


def string_operations():
    while True:
        print("\nMenüü funktsioonide jaoks stringidega ja loenditega töötamiseks:")
        print("1. Stringide ühendamine")
        print("2. Stringi jagamine tühikutega")
        print("3. Kontroll, kas string sisaldab ainult numbreid")
        print("4. Kontroll, kas string on suurtähtedega")
        print("5. Stringi osa asendamine")
        print("6. Alamstringi otsimine stringist")
        print("7. Stringi teisendamine suurtähtedeks")
        print("8. Stringi teisendamine väiketähtedeks")
        print("9. Märgi esinemissageduse loendamine")
        print("10. Sõnade loendi sorteerimine")
        print("0. Väljumine")
        
        choice = input("Valige toimingu number: ")
        
        if choice == "1":
            s1 = input("Sisestage esimene string: ")
            s2 = input("Sisestage teine string: ")
            print("Ühendatud string:", s1 + s2)
            """See funktsioon ühendab kaks stringi üheks tervikuks."""
        
        elif choice == "2":
            s = input("Sisestage string: ")
            print("Sõnade loend:", s.split())
            """See funktsioon jagab stringi sõnadeks tühikute järgi."""
        
        elif choice == "3":
            s = input("Sisestage string: ")
            print("Sisaldab ainult numbreid:", s.isdigit())
            """See funktsioon kontrollib, kas string sisaldab ainult numbreid."""
        
        elif choice == "4":
            s = input("Sisestage string: ")
            print("Kõik märgid on suurtähed:", s.isupper())
            """See funktsioon kontrollib, kas kõik stringi märgid on suurtähed."""
        
        elif choice == "5":
            s = input("Sisestage string: ")
            old = input("Sisestage asendatav alamstring: ")
            new = input("Sisestage uus alamstring: ")
            print("Asendatud string:", s.replace(old, new))
            """See funktsioon asendab stringi määratud osa uue alamstringiga."""
        
        elif choice == "6":
            s = input("Sisestage string: ")
            sub = input("Sisestage otsitav alamstring: ")
            print("Esimese esinemise indeks:", s.find(sub))
            """See funktsioon otsib stringist alamstringi ja tagastab selle esimese esinemise indeksi."""
        
        elif choice == "7":
            s = input("Sisestage string: ")
            try:
                number = float(s)  
                print(f"String on number: {number}")  
            except ValueError:  
                print("String ei ole number.")  
            """See funktsioon proovib teisendada stringi arvuks. Kui teisendamine ei õnnestu, väljastatakse veateade."""
        
        elif choice == "8":
            n = int(input("Sisestage stringide arv: "))  
            strings = [input(f"Sisestage string {i+1}: ") for i in range(n)]  
            prefix = strings[0]  
            for string in strings[1:]:  
                while not string.startswith(prefix):  
                    prefix = prefix[:-1]  
            print("Ühine eellause:", prefix)  
            """See funktsioon leiab kõikide sisestatud stringide ühise eellause, võrreldes neid järjestikku."""
        
        elif choice == "9":
            s = input("Sisestage string: ")  
            unique_chars = len(set(s))  
            print("Ainulaadsete märkide arv:", unique_chars)  
            """See funktsioon arvutab, kui palju ainulaadseid märke on stringis, kasutades set()-i."""
        
        elif choice == "10":
            s = input("Sisestage string: ")  
            words = s.split()  
            print("Sõnade arv:", len(words))  
            """See funktsioon jagab stringi sõnadeks ja loendab, kui palju sõnu stringis on."""
        
        elif choice == "0":
            print("Programmist väljumine.")
            """See käsk lõpetab programmi töö."""
            break
        
        else:
            print("Vale sisestus, proovige uuesti.")
            """See sõnum teatab kasutajale, kui ta sisestas vale toimingu numbri."""

if __name__ == "__main__":
    string_operations()
    """Käivitatakse programmi põhifunktsioon."""
        elif choice == "0":
            print("Programmist väljumine.")
            """See käsk lõpetab programmi töö."""
            break
        
        else:
            print("Vale sisestus, proovige uuesti.")
            """See sõnum teatab kasutajale, kui ta sisestas vale toimingu numbri."""

if __name__ == "__main__":
    string_operations()
    """Käivitatakse programmi põhifunktsioon."""
