# Ovdje implementujemo rad sa krisnikom

import os
from random import randint
import datetime
import admin
from tabulate import tabulate

korisnici_niz = []
niz_hotela = []
sobe = []
sobe_trazenog_hotela = []
trenutno_prijavljen_korisnik = {}
niz_rezervacija = []
niz_rezervacija_apdejt = []
niz_rezervacija_provjera =[]

def korisnik():

    println()
    print("Odabrali ste opciju korisnik! \n")
    print("1) Registracija")
    print("2) Prijava na postojeći nalog\n")

    unos = input("Odaberite opciju: ")


    if unos == "1":
        kreiraj_korisnika()

    elif unos == "2":
        trenutno_prijavljen_korisnik = {}
        while trenutno_prijavljen_korisnik == {}:
            trenutno_prijavljen_korisnik = prijava_korisnika()

            if (trenutno_prijavljen_korisnik == {}):
                print("Nepostojeći nalog, molimo pokušajte ponovo!")

        # print(korisnik['ime'])
        opcije_korsinika()
    
    else:
        println()
        print("Unijeli ste nepostojeću opciju, molimo vas unesite jednu od navedenih opcija ponovo")


# ----- REGISTRACIJA KORISNIKA -----

def kreiraj_korisnika():

    println()
    print("Molimo unesite vaše podatke: \n")
    ime = input("Ime: ")
    prezime = input("Prezime: ")
    korisnicko_ime = input("Korisničko ime: ")
    lozinka = input("Lozinka: ")
    telefon = input("Kontakt telefon: ")
    email = input("E-mail adresa: ")
    uloga = "korisnik"

    korisnik_podaci = {}
    korisnik_podaci ['ime'] = ime
    korisnik_podaci ['prezime'] = prezime
    korisnik_podaci ['korisnicko_ime'] = korisnicko_ime
    korisnik_podaci ['lozinka'] = lozinka
    korisnik_podaci ['telefon'] = telefon
    korisnik_podaci ['email'] = email
    korisnik_podaci ['uloga'] = uloga
 

    prenos = korisnik2Str(korisnik_podaci)
    target = open("korisnici.txt", "a")
    target.write(prenos + "\n")
    target.close
    println()
    print("Registracija uspješno izvršena!")



def korisnik2Str(korisnik):

    pisani_format = korisnik['ime'] + "|" + korisnik['prezime'] + "|" + korisnik['korisnicko_ime'] + "|" + korisnik['lozinka'] + "|" + korisnik['telefon'] + "|" + korisnik['email'] + "|" + korisnik['uloga'] 
    return pisani_format

# ----- PRIJAVA KORISNIKA -----

def str2Korisnik(red):

    korisnik_podaci = {}

    dio = red.split("|")
    korisnik_podaci["ime"] = dio[0]
    korisnik_podaci["prezime"] = dio[1]
    korisnik_podaci["korisnicko_ime"] = dio[2]
    korisnik_podaci["lozinka"] = dio[3]
    korisnik_podaci["telefon"] = dio[4]
    korisnik_podaci["email"] = dio[5]
    korisnik_podaci["uloga"] = dio[6]

    return korisnik_podaci


def ucitaj(nazivFajla):

    korisnici_niz.clear()
    target = open(nazivFajla, "r")

    # Ubacujemo podatke iz fajla u niz 
    for red in target.readlines():
        korisnici_niz.append(str2Korisnik(red))

    target.close()



def prijava_korisnika():

    ucitaj("korisnici.txt")
    println()
    print("Molimo unesite vaše korisničko ime i lozinku \n")

    korisnicko_ime = input("Korisničko ime: ")
    lozinka = input("Lozinka: ")

    korisnik = {}

    for info in korisnici_niz:
        if info['korisnicko_ime'] == korisnicko_ime and info['lozinka'] == lozinka:
            print("Dobrodošao ", info['ime'])
            korisnik = info
            trenutno_prijavljen_korisnik.update(info)

    
    return korisnik


# ------- SVE FUNKCIJE/OPCIJE KOJE IMA KORISNIK: -------- 

def opcije_korsinika():
    unos = ""
    while unos != "7":
        apdejt_rezervacija()
        println()
        print("\n1) Pretraga hotela")
        print("2) Pregled hotela")
        print("3) Rezervacija")
        print("4) Pregled rezervacija")
        print("5) Ocijeni hotel")
        print("6) Prikaži najbolje hotele")
        print("7) Odjava \n")
        unos = input("Odaberite neku od opcija: ")

        if unos == "1":
            pretraga_hotela()
        
        elif unos == "2":
            pregled_hotela()

        elif unos == "3":
            rezervisi()

        elif unos == "4":
            pregled_rezervacija()

        elif unos == "5":
            ocjenivanje_hotela()
        
        elif unos == "6":
            prikazi_najbolje_hotele()

        elif unos == "7":
            trenutno_prijavljen_korisnik.clear()
            odjava()



def pregled_hotela():
    
    println()
    print("Pronađni hoteli: \n")
    ucitaj_hotele("hoteli.txt")


    header = niz_hotela[0].keys()
    rows =  [x.values() for x in niz_hotela]
    print (tabulate(rows, header, tablefmt='grid'))



def ucitaj_hotele(nazivFajla):

    niz_hotela.clear()
    target = open(nazivFajla, "r")

    for red in target.readlines():
        niz_hotela.append(str2Hotel(red))
    target.close()


def str2Hotel(red):

    hotel_podaci = {}

    dio = red.split("|")
    hotel_podaci["id"] = dio[0]
    hotel_podaci["ime"] = dio[1]
    hotel_podaci["adresa"] = dio[2]
    hotel_podaci["bazen"] = dio[3]
    hotel_podaci["restoran"] = dio[4]
    hotel_podaci["ocjena"] = dio[5]

    return hotel_podaci


def ocjenivanje_hotela():

    ucitaj_hotele("hoteli.txt")
    println()
    print("Odaberite hotel koji želite da ocijenite: \n")

    # Dodavanje atributa redni broj kako bi mogli da odaberemo koji hotel zelimo da ocjenimo
    # Atribute se dodaje u novi niz i ne utice na generalni niz hotela
    novi_niz = []
    for index, i in enumerate(niz_hotela):
        #print(index, ")", i)
        i["redni broj"] = index
        novi_niz.append(i)


    header = novi_niz[0].keys()
    rows =  [x.values() for x in novi_niz]
    print (tabulate(rows, header, tablefmt='grid'))

    

    unos = eval(input("\nOdaberite redni broj hotela: "))

    odabrani_hotel = niz_hotela[unos]
    niz_hotela.pop(unos)
    ocjena_hotela = odabrani_hotel["ocjena"]
    br_prenos = eval(ocjena_hotela[0] + ocjena_hotela[1] + ocjena_hotela[2])
    print(" ")
    ocjena_korisnik = eval(input("Unesite ocjenu od 1 do 5: "))
    ukupna_ocjena = (br_prenos + ocjena_korisnik)/2

    odabrani_hotel['ocjena'] = str(ukupna_ocjena)

    niz_hotela.append(odabrani_hotel)

    target = open("hoteli.txt", "a+")
    target.truncate(0)

    for i in niz_hotela:
        target.write(admin.hotel2Str(i))



def odjava():
    println()
    print("Odjavili ste se sa vašeg profila!\n")
    

def rezervisi():
    uslov = " "
    while uslov != "1":
        println()
        hotel_za_rezervaciju = input("Koji hotel želite da rezervišete: ")
        datum_prijave = input("Unesite datum dolaska u formatu yyyy-mm-dd : ")
        datum_odjave = input("Unesite datum odlaska u formatu yyyy-mm-dd : ")


        id_trazenog_hotela = ""
        odabrani_hotel = {}
        ucitaj_hotele("hoteli.txt")
        for i in niz_hotela:
            ime1 = i['ime']
            if  ime1.lower() == hotel_za_rezervaciju.lower() :
                id_trazenog_hotela = i["id"]
                odabrani_hotel = i


        println()        
        
        sobe_trazenog_hotela.clear()
        sobe.clear()
        #  Ispis soba (menija) kako bi korisnik izabrao sobu koju zeli 
        ucitavanje_soba("sobe.txt")
        
        for index, i in enumerate(sobe):
            if i['hotelID'] == id_trazenog_hotela:
                sobe_trazenog_hotela.append(i)

        novi_niz = []
        for index, i in enumerate(sobe_trazenog_hotela):
            i["redni broj"] = index
            novi_niz.append(i)
                
        print(" ")
        print("Odaberite neku od soba u traženom hotelu: \n")

        #for index, i in enumerate(sobe_trazenog_hotela):
            #print(index, ")", i)

        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    

        print(" ")
        unos = eval(input("Odaberite sobu: "))
        odabrana_soba = novi_niz[unos]

        uslov = provjera_zauzetosti(odabrana_soba['hotelID'], odabrana_soba['sobaID'], datum_prijave, datum_odjave)



    #print("\nOdabrali ste sobu: ", odabrana_soba, "\n" ) 


    # Generisanje ID-a rezervacije
    id_rezervacije = random_cifre(6)
    
    
    # Uzimanje vremena kreiranja rezervacije 
    x = datetime.datetime.now()
    

    # Generisanje cijene rezervacije
    cijena_rez = 0

    datum_od = datetime.datetime.strptime(datum_odjave, '%Y-%m-%d' )
    datum_pr = datetime.datetime.strptime(datum_prijave, '%Y-%m-%d' )
    delta = datum_pr - datum_od
    br_dana = delta.days

    cijena_rez = abs(br_dana * eval(odabrana_soba['cijena']))
    # Generisanje rezervacije
    # 
    # Proba da li je memorisan korisnik prazan ili je poopunjen

    # PRenos ocjene se radi zato sto imamo \n negdje u originalnom stringu iz odabrani_hotel['ocjena']
    prenos = odabrani_hotel['ocjena']
    ocjena = prenos[0] + prenos [1] + prenos[2]  
    

    rezervacija = {}
    rezervacija['idRezervacije'] = id_rezervacije
    rezervacija['idHotela'] = odabrana_soba['hotelID']
    rezervacija['idSobe'] = odabrana_soba['sobaID']
    rezervacija['datumPrijave'] = datum_prijave
    rezervacija['datumOdjave'] = datum_odjave
    rezervacija['korisnik'] = trenutno_prijavljen_korisnik["korisnicko_ime"]
    rezervacija['status'] = "rezervisano"
    rezervacija['ocjenaHotela'] = ocjena
    rezervacija['vrijemeKreiranja'] = x
    rezervacija['cijenaRezervacije'] = cijena_rez

    #print("Vaša rezervacija: ")
    #print(rezervacija)

    #  GENERISANJE STRINGA ZA UPIS U FAJL rezervacije.txt
    pisani_format_rezervacije = str(rezervacija['idRezervacije']) + "|" + rezervacija['idHotela'] + "|" + rezervacija['idSobe'] + "|" + rezervacija['datumPrijave'] + "|" + rezervacija['datumOdjave'] + "|" + rezervacija['korisnik'] + "|" + rezervacija['status']  + "|" + str(rezervacija['vrijemeKreiranja']) + "|" + rezervacija['ocjenaHotela'] + "|" + str(rezervacija['cijenaRezervacije'])
    

    # Upisivanje rezervacije u fajl rezervacije.txt
    target = open("rezervacije.txt", 'a')
    target.write(pisani_format_rezervacije)
    target.close()

    print("Rezervacija uspješno kreirana!")



def provjera_zauzetosti(idHotela, idSobe, datumPrijave, datumOdjave):

    datum_odjave = datetime.datetime.strptime(datumOdjave, '%Y-%m-%d' )
    datum_prijave = datetime.datetime.strptime(datumPrijave, '%Y-%m-%d' )

    ucitaj_rezervacije_provjera('rezervacije.txt')

    vrijednost = "1"

    for i in niz_rezervacija_provjera:
        if i['idHotela'] == idHotela and i['idSobe'] == idSobe:

            # Konvertovanje u datum 
            datumDolaska =  datetime.datetime.strptime(i['datumPrijave'], '%Y-%m-%d' )
            datumOdlaska =  datetime.datetime.strptime(i['datumOdjave'], '%Y-%m-%d' )
            
            if datum_prijave < datumDolaska and datum_odjave < datumDolaska:
                print(" ")
                # print("Soba je slobodna u trazenom periodu! -- manji datum")
                
            elif datum_prijave > datumOdlaska and datum_odjave > datumOdlaska:
                print(" ")
                # print("Soba je slobodna u trazenom periodu! -- veci datum")
                

            else:
                print("Soba je zauzeta u traženom periodu!")
                print("Molimo unesite drugi period rezervacije!")
                vrijednost = "2"
                break

    return vrijednost


def ucitaj_rezervacije_provjera(nazivFajla):

    niz_rezervacija_provjera.clear()
    target = open(nazivFajla, 'r')

    for red in target.readlines():
        niz_rezervacija_provjera.append(str2Rez(red))
    target.close()



def prikazi_najbolje_hotele():
    println()
    print("Prikaz hotela po najboljoj prosječnoj ocjeni: \n")

    # Redanje hotela u odnosu na prosjecnu ocjenu
    # algoritam za sortitanje odradjen preko lambda izraza

    sortirani_hoteli = []
    ucitaj_hotele("hoteli.txt")
    sortirani_hoteli = niz_hotela

    sortirana_lista = sorted(sortirani_hoteli, key=lambda k: k['ocjena'], reverse=True)
    

    header = sortirana_lista[0].keys()
    rows =  [x.values() for x in sortirana_lista]
    print (tabulate(rows, header, tablefmt='grid'))


        
def pregled_rezervacija():
    println()
    print("Vaše rezervacije: \n")

    kor_ime_prijevljenog = trenutno_prijavljen_korisnik['korisnicko_ime']

    ucitaj_rezervacije("rezervacije.txt")
    novi_niz = []
    for i in niz_rezervacija:
        if kor_ime_prijevljenog == i['korisnik']:
            novi_niz.append(i)

    header = novi_niz[0].keys()
    rows =  [x.values() for x in novi_niz]
    print (tabulate(rows, header, tablefmt='grid'))

    # Ucitati fajl istorija rezervacija i naci one koje se poklapaju sa username trenutnog korisnika
    # Ispisati rezervacije tabelarno 

def pretraga_hotela():
    println()
    print("\n1) Pretraga po jednom kriterijumu")
    print("2) Pretraga po više kriterijuma\n")

    unos = input("Odaberite opciju: ")

    if unos == "1":
        pretraga_jedan_kriterijum()

    elif unos == "2":
        pretraga_po_vise_kriterijuma()

    else:
        print("Unijeli ste nepostojeću opciju")


def pretraga_jedan_kriterijum():
    # Pretraga hotela samo po nazivu (po jednom kriterijumu)
    println()
    print(" ")
    ime_hotela = input("Unesite ime hotela: ")
    trazeni_hotel = {}
    ucitaj_hotele("hoteli.txt")
    for i in niz_hotela:
        ime1 = i['ime']
        
        if  ime1.lower() == ime_hotela.lower() :
            print("Postoji hotel: ", ime_hotela)
            trazeni_hotel = i
            break

    prazan_provjera = bool(trazeni_hotel)
    println()
    print(" ")
    if prazan_provjera == True:
        print("Tražili ste hotel: ", trazeni_hotel["ime"])
        print("Informacije o hotelu: ")
        print("ID hotela: ", trazeni_hotel["id"])
        print("Adresa: ", trazeni_hotel['adresa'])
        print("Hotel posjeduje bazen -> ", trazeni_hotel["bazen"])
        print("Hotel posjeduje restoran -> ", trazeni_hotel["restoran"], "\n")  

    else:
        print("Ne postoji traženi hotel!")

# ----------- PRETRAGA PO VISE KRITERIJUMA -------------        

def pretraga_po_vise_kriterijuma():
    println()
    print("Ukoliko želite da preskočite određeni kriterijum unesite znak - \n")
    naziv = input("Ime hotela: ")
    adresa = input("Adresa hotela: ")
    ocjena = input("Ocjena hotela: ")
    print(" ")
    ucitaj_hotele("hoteli.txt")

    postoji = False

    for i in niz_hotela:
        prenos = i['ocjena']
        hot_ocjena = prenos[0] + prenos[1] + prenos[2]  
        if(i['ime'] == naziv or naziv == "-") and (i['adresa'] == adresa or adresa == "-") and (hot_ocjena == ocjena or ocjena == "-"):
            print(i)
            postoji = True


    if postoji == False:
        print("Ne postoji traženi hotel!")



    # Osmisliti kako omoguciti da odabere koje kriterijume zeli 


# ------------- OPERACIJE SA SOBAMA ---------------

def ucitavanje_soba(nazivFajla):
    
    target = open(nazivFajla, "r")

    for red in target.readlines():
        sobe.append(str2Soba(red))

    target.close()

def str2Soba(red):
    
    soba_podaci = {}

    dio = red.split("|")
    soba_podaci["hotelID"] = dio[0]
    soba_podaci["sobaID"] = dio[1]
    soba_podaci["brKreveta"] = dio[2]
    soba_podaci["cijena"] = dio[3]
    soba_podaci["tip"] = dio[4]
    soba_podaci["klima"] = dio[5]
    soba_podaci["tv"] = dio[6]
    
    return soba_podaci

# ------------- OPERACIJE SA REZERVACIJAMA ---------------

# Generisanje random broja od 6 cifara za id rezervacije
 
def random_cifre(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Apdejtovanje rezervacija u  odnosu na trenutni datum

def apdejt_rezervacija():

    # Ova funkcija se izvrsava pri prijavljivanju korisnika kako bi imali...
    # ... apdejtovane informacije koje su sobe slobodne i u kom terminu!
    niz_rezervacija_apdejt.clear()
    ucitaj_rezervacije_apdejt("rezervacije.txt")

    trenutni_datum = datetime.datetime.today()
    

    for index, i in enumerate(niz_rezervacija_apdejt):
        datum_prijave = datetime.datetime.strptime(i['datumPrijave'], '%Y-%m-%d' )
        datum_odjave = datetime.datetime.strptime(i['datumOdjave'], '%Y-%m-%d' )

        # Provjera -> print(index, ")", i)

        if datum_prijave > trenutni_datum:
            # Provjera -> print("Rezervacija jos vazi")
            i["status"] = "rezervisano"

        elif datum_prijave < trenutni_datum and datum_odjave > trenutni_datum:
            # Provjera -> print("Rezervacija je u toku")
            i["status"] = "u toku"

        elif datum_odjave < trenutni_datum:
            # Provjera -> print("Rezervacija je istekla")
            i["status"] = "istekla"
    
    # Koristi se u slcaju provjere funkcije -> print(niz_rezervacija_apdejt)

    # Ciscenje fajla kako bi upisali nove apdejtvane podatke
    target = open("rezervacije.txt", 'a+')
    target.truncate(0)


    #Upisivanje apdejtovanih informacija u fajl
    for i in niz_rezervacija_apdejt:
        informacije = str(i['idRezervacije']) + "|" + i['idHotela'] + "|" + i['idSobe'] + "|" + i['datumPrijave'] + "|" + i['datumOdjave'] + "|" + i['korisnik'] + "|" + i['status']  + "|" + str(i['vrijemeKreiranja']) + "|" + i['ocjenaHotela'] + "|" + i['cijenaRezervacije']
        target.write(informacije)

    target.close()
    

def ucitaj_rezervacije_apdejt(nazivFajla):

    target = open(nazivFajla, 'r')

    for red in target.readlines():
        niz_rezervacija_apdejt.append(str2Rez(red))
    target.close()

# FUnkcija ucitava aktivne rezervacije i prosledjuje ih u niz niz_rezervacija
def ucitaj_rezervacije(nazivFajla):
    niz_rezervacija.clear()
    target = open(nazivFajla, 'r')

    for red in target.readlines():
        niz_rezervacija.append(str2Rez(red))
    target.close()

def str2Rez(red):

    rezervacija = {}

    dio = red.split("|")
    rezervacija['idRezervacije'] = dio[0]
    rezervacija['idHotela'] = dio[1]
    rezervacija['idSobe'] = dio[2]
    rezervacija['datumPrijave'] = dio[3]
    rezervacija['datumOdjave'] = dio[4]
    rezervacija['korisnik'] = dio[5]
    rezervacija['status'] = dio[6]
    rezervacija['vrijemeKreiranja'] = dio[7]
    rezervacija['ocjenaHotela'] = dio[8]
    rezervacija['cijenaRezervacije'] = dio[9]

    return rezervacija

def println():
    print("-------------------------------------")