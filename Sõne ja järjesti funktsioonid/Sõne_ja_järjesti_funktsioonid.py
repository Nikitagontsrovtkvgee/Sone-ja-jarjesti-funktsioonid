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
            print("Suurtähtedega string:", s.upper())
            """See funktsioon teisendab kõik stringi märgid suurtähtedeks."""
        
        elif choice == "8":
            s = input("Sisestage string: ")
            print("Väiketähtedega string:", s.lower())
            """See funktsioon teisendab kõik stringi märgid väiketähtedeks."""
        
        elif choice == "9":
            s = input("Sisestage string: ")
            char = input("Sisestage märk: ")
            print("Märgi esinemissagedus:", s.count(char))
            """See funktsioon loendab, mitu korda määratud märk stringis esineb."""
        
        elif choice == "10":
            words = input("Sisestage sõnade loend komaga eraldatult: ").split(', ')
            print("Sorteeritud loend:", sorted(words))
            """See funktsioon sorteerib sõnade loendi tähestikulises järjekorras."""
        
        elif choice == "0":
            print("Programmist väljumine.")
            break
            """See käsk lõpetab programmi töö."""
        
        else:
            print("Vale sisestus, proovige uuesti.")
            """See sõnum teatab kasutajale, kui ta sisestas vale toimingu numbri."""

if __name__ == "__main__":
    string_operations()
    """Käivitatakse programmi põhifunktsioon."""
