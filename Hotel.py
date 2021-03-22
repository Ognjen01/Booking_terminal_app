# PROJEKAT SISTEM HOTELA, APLIKACIJA ZA REZERVACIJE "Travellino"
# Ognjen Lazic SR 13/2020

import korisnici
import recepcija
import admin
import datetime
import tabulate

def main():
    
    print("\nDOBRODOŠLI U \"TRAVELLINO\"")
    

    unos = ""
 
    while unos != "4":
        korisnici.println()
        prikazi_meni()

        unos = input("Odaberite opciju: ")

        if unos == "1":
            korisnici.korisnik()
            

        elif unos == "2":
            recepcija.recepcionar()

        elif unos == "3":
            admin.administrator()

        elif unos == "4":
            izlaz()

        else:
            korisnici.println()
            print("\nUnijeli ste pogrešnu opciju, molimo unesite jednu od navedenih opcija ponovo...\n")
            korisnici.println()



def izlaz():
    korisnici.println()
    print("Izašli ste iz aplikacije!\n")

def prikazi_meni():

        print("Odaberite neku od stavki iz menija:  \n")
        print("1) Prijava ili registracija korisnika")
        print("2) Prijava kao recepcionar")
        print("3) Prijava kao administrator")
        print("4) Izlaz iz aplikacije \n")
        

if __name__ == "__main__":
    main()