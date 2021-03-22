# Rad sa administratorom

import korisnici
import recepcija
from tabulate import tabulate

trenutno_prijavljen_admin = {}
administratori = []
niz_hotela_admin = []
niz_soba = []
niz_recepcionara = []


def administrator():

    korisnici.println()
    print("Odabrali ste opciju adminstrator! \n")
    prijava_admina()
    

def prijava_admina():
    provjera = True
    while provjera == True:
        korisnici.println()
        kor_ime = input("Unesite korisničko ime: ")
        lozinka = input("Unesite lozinku: ")

        ucitaj_admine("administratori.txt")

        #print(administratori)

        for i in administratori:
            if lozinka == i['lozinka'] and kor_ime == i['korisnicko_ime']:
                trenutno_prijavljen_admin = i
                provjera = False

        if provjera == True:
            print("Ne postoji traženi administrator, molimo ponovite unos!")
    korisnici.println()
    print("Dobrodošao ", trenutno_prijavljen_admin['ime'])

    if provjera == False:
        
        opcije_admina() 

def opcije_admina():
    opcija = ""
    while opcija != "7":
        korisnici.println()
        print("Odaberite neku od opcija:\n")
        print("1) Dodavanje hotela")
        print("2) Dodavanje recepcionara")
        print("3) Ažuriranje hotela")
        print("4) Brisanje hotela")
        print("5) Brisanje recepcionara")
        print("6) Pretraga recepcionara")
        print("7) Odjava\n")


        opcija = input("Odaberite opciju: ")

        if opcija == "1":
            dodavanje_hotela()
        elif opcija == "2":
            dodavanje_recepcionara()
        elif opcija == "3":
            azuriranje_hotela()
        elif opcija == "4":
            brisanje_hotela()
        elif opcija == "5":
            brisanje_recepcionara()
        elif opcija == "6":
            pretraga_recepcionara()
        elif opcija == "7":
            korisnici.println()
            print("Odjavili sa aplikacije!")
        else:
            korisnici.println()
            print("Unijeli ste nepostojeću opciju!")
            
    

def ucitaj_admine(nazivFajla):

    administratori.clear()
    target = open(nazivFajla, "r")

    # Ubacujemo podatke iz fajla u niz 
    for red in target.readlines():
        administratori.append(str2Admin(red))

    target.close()


def str2Admin(red):

    admin_podaci = {}

    dio = red.split("|")
    admin_podaci["ime"] = dio[2]
    admin_podaci["prezime"] = dio[3]
    admin_podaci["korisnicko_ime"] = dio[0]
    admin_podaci["lozinka"] = dio[1]
    admin_podaci["email"] = dio[4]
    
    return admin_podaci


def dodavanje_hotela():
    korisnici.println()
    print("Odabrali ste opciju dodavanja hotela. \n")
    print("Molimo unesite informacije:")
    id_hotela = korisnici.random_cifre(6)
    ime = input("Ime hotela: ")
    adresa = input("Adresa hotela: ")
    bazen = input("Da li hotel ima bazen? ")
    restoran = input("Da li hotel ima restoran? ")
    ocjena = input("Početna ocjena hotela: ")

    hotel_podaci = {}
    hotel_podaci['id'] = id_hotela
    hotel_podaci['ime'] = ime
    hotel_podaci['adresa'] = adresa
    hotel_podaci['bazen'] = bazen
    hotel_podaci['restoran'] = restoran
    hotel_podaci['ocjena'] = ocjena

    prenos = hotel2Str(hotel_podaci)
    target = open("hoteli.txt", "a")
    target.write(prenos + "\n")
    target.close()

def hotel2Str(hotel):
    pisani_format = str(hotel['id']) + "|" + hotel['ime'] + "|" + hotel['adresa'] + "|" + hotel['bazen'] + "|" + hotel['restoran'] + "|" + hotel['ocjena'] 
    return pisani_format


def dodavanje_recepcionara():
    korisnici.println()
    print("Odabrali ste opciju dodavanja recepcionara. \n")
    print("Unesite podatke recepcionara: \n")

    korisnicko_ime = input("Korisničko ime: ")
    lozinka = input("Lozinka: ")
    ime = input("Ime: ")
    prezime = input("Prezime: ")
    telefon = input("Kontakt telefon: ")
    email = input("e-mail: ")
    uloga = "recepcionar"
    id_hotela = input("ID hotela u kome je zaposlen: ")

    recepcionar_podaci = {}
    recepcionar_podaci['korisnicko_ime'] = korisnicko_ime
    recepcionar_podaci['lozinka'] = lozinka
    recepcionar_podaci['ime'] = ime
    recepcionar_podaci['prezime'] = prezime
    recepcionar_podaci['telefon'] = telefon
    recepcionar_podaci['email'] = email
    recepcionar_podaci['uloga'] = uloga
    recepcionar_podaci['id_hotela'] = id_hotela

    prenos = recepcionar2Str(recepcionar_podaci)
    target = open("recepcionari.txt", "a")
    target.write(prenos + "\n")
    target.close

def recepcionar2Str(recepcionar):
    pisani_format = recepcionar['korisnicko_ime'] + "|" + recepcionar['lozinka'] + "|" + recepcionar['ime'] + "|" + recepcionar['prezime'] + "|" + recepcionar['telefon'] + "|" + recepcionar['email'] + "|" + recepcionar['uloga'] + "|" + recepcionar['id_hotela']
    return pisani_format

def azuriranje_hotela():
    korisnici.println()
    print(" ")
    print("1) Ažuriranje ponude postojećih hotela")
    print("2) Dodavanje soba u postojeće hotele")
    print("3) Nazad\n")
    izbor = input("Odaberite opciju: ")

    if izbor == "1":
        azuriranje_ponude()
    elif izbor == "2":
        dodavanje_sobe_u_hotel()
    elif izbor == "3":
        print(" ")
    else:
        korisnici.println()
        print("Odabrali ste nepostojeću opciju!\n")

def azuriranje_ponude():
    korisnici.println()
    print("Ažriranje ponude hotela")

    ucitaj_hotele("hoteli.txt")

    print("Odaberite koji hotel želite ažurirati:")
    novi_niz = []
    for index, i in enumerate(niz_hotela_admin):
        i["redni broj"] = index
        novi_niz.append(i)

    header = novi_niz[0].keys()
    rows =  [x.values() for x in novi_niz]
    print (tabulate(rows, header, tablefmt='grid'))

    odabir = eval(input("Odaberite redni broj hotela: "))

    odabrani_hotel = niz_hotela_admin[odabir]
    niz_hotela_admin.pop(odabir)

    korisnici.println()

    print("Ova opcija vam omogućava izmjenu bazena i restorana. \n")

    bazen = input("Da li hotel posjeduje bazen? (da/ne) ")
    restoran = input("Da li hotel posjeduje restoran? (da/ne) ")
    print(" ")
    odabrani_hotel["bazen"] = restoran
    odabrani_hotel["restoran"] = bazen

    niz_hotela_admin.append(odabrani_hotel)

    target = open("hoteli.txt", "a+")
    target.truncate(0)

    for i in niz_hotela_admin:
        target.write(hotel2Str(i))

    target.close()




def dodavanje_sobe_u_hotel():
    korisnici.println()
    print("Dodavanje novih soba u hotele. \n")

    ucitaj_hotele("hoteli.txt")

    print("Odaberite u koji hotel želite dodati smještaj? \n")
    for index, i in enumerate(niz_hotela_admin):
        print(index, ")", i['ime'])
    
    odabir_hotela = eval(input("Odaberite hotel: "))

    trazeni_hotel = niz_hotela_admin[odabir_hotela]

    print(trazeni_hotel['id'], trazeni_hotel['ime'])

    # Algoritam za generisanje ID sobe koji ce povecavati za 1 najveci ID sobe u tom hotelu!

    ucitaj_sobe("sobe.txt")

    najveci_id_sobe = 0
    for i in niz_soba:
        if eval(i['sobaID']) > najveci_id_sobe:
            najveci_id_sobe = eval(i["sobaID"])

    #print("Najveci ID sobe u odabranom hotelu je ", najveci_id_sobe)
    id_sobe = najveci_id_sobe + 1
    
    korisnici.println()
    print(" ")
    print("\nUnesite informacije o smještaju: ")
    br_kreveta = input("Broj kreveta: ")
    cijena_nocenja = input("Cijena nocenja: ")
    tip_smjestaja = input("Tip smještaja (soba/apartman): ")
    klima = input("Da li smještaj ima klimu? (da/ne): ")
    tv = input("Da li smještaj ima tv? (da/ne): ")

    # Pretvaranje unesenih informacija u string

    str_soba = trazeni_hotel['id'] + "|" + str(id_sobe) + "|" + br_kreveta + "|" + cijena_nocenja + "|" + tip_smjestaja + "|" + klima + "|" + tv 
    print("Uspjesno dodata soba -> ", str_soba)

    target = open("sobe.txt", "a")
    target.write(str_soba)
    target.close()




def brisanje_hotela():
    ucitaj_hotele("hoteli.txt")
    hotel_za_brisanje = {}
    korisnici.println()
    print("\nOdaberite koji hotel želite da izbrište iz liste hotela: ")
    novi_niz = []
    for index, i in enumerate(niz_hotela_admin):
        i["redni broj"] = index
        novi_niz.append(i)
        # print(index, ")", i)

    header = novi_niz[0].keys()
    rows =  [x.values() for x in novi_niz]
    print (tabulate(rows, header, tablefmt='grid'))

    print(" ") 
    unos_za_brisanje = eval(input("Odaberite redni broj hotela: "))
    hotel_za_brisanje = niz_hotela_admin[unos_za_brisanje]
    niz_hotela_admin.pop(unos_za_brisanje)

    

    # Dio za ciscenje fajla a zatim za upisivanje nove liste
    target = open("hoteli.txt", 'a+')
    target.truncate(0)

    
    for i in niz_hotela_admin:
        info = i['id'] + "|" + i['ime'] + "|" + i['adresa'] + "|" + i['bazen'] + "|" + i['restoran'] + "|" + i['ocjena']
        target.write(info)

    target.close()
    korisnici.println()
    print("Uspjesno izbrisan hotel! ")

    # Kreiranje logickog brisanja uz pomoc fajla za istoriju hotela
    target = open("istorijahotela.txt", "a+")
    target.write(str(hotel_za_brisanje))
    target.close()


def ucitaj_hotele(nazivFajla):

    niz_hotela_admin.clear()
    target = open(nazivFajla, "r")

    for red in target.readlines():
        niz_hotela_admin.append(korisnici.str2Hotel(red))
    target.close()

def ucitaj_sobe(nazivFajla):

    niz_soba.clear()
    target = open(nazivFajla, "r")

    for red in target.readlines():
        niz_soba.append(korisnici.str2Soba(red))
    target.close()



def brisanje_recepcionara():

    # Pristupanje llisti recepcionara u drugom fajlu
    recepcija.ucitaj_recepcionare("recepcionari.txt")
    # Nema potrebe za globalnom listom recepcionari
    recepcionari = recepcija.svi_recepcionari
    print(recepcionari)
    korisnici.println()
    print("\nOdaberite recepcionara koga želite izbrisati: \n")
    novi_niz = []
    for index, i in enumerate(recepcionari):
        i["redni broj"] = index
        novi_niz.append(i)
        #print(index, ")", i)
    print(" ")

    header = novi_niz[0].keys()
    rows =  [x.values() for x in novi_niz]
    print (tabulate(rows, header, tablefmt='grid'))

    rec_brisanje = eval(input("Odaberite redni broj recepcionara za brisanje: ")) 
    recepcionari.pop(rec_brisanje)

    target = open("recepcionari.txt", 'a+')
    target.truncate(0)

    for i in recepcionari:
        info = i['korisnicko_ime'] + "|" + i['lozinka'] + "|" + i['ime'] + "|" + i['prezime'] + "|" + i['telefon'] + "|" + i['email'] + "|" + i['uloga'] + "|" + i['id_hotela']
        target.write(info)

    target.close()



def pretraga_recepcionara():
    
    korisnici.println()
    print("Odaberite uslov po kome želite pretraživati recepcionare: \n")
    print("1) Ime i Prezime ")
    print("2) Korisničko ime ")
    print("3) Svi recepcionari jednog hotela ")
    print("4) Pretraga po više kriterijuma \n")

    unos = input("Odaberite opciju: ")

    if unos == "1":
        korisnici.println()
        print(" ")
        ime = input("Unesite ime recepcionara:")
        prezime = input("Unesite prezime recepcionara: ")
        pretrag_ime_prezime(ime, prezime)
    
    elif unos == "2":
        korisnici.println()
        print(" ")
        username =  input("Unesite korisničko ime recepcionara: ")
        pretraga_username(username)

    elif unos == "3":
        recepcionari_po_hotelima()

    elif unos == "4":
        pretraga_recepcionara_po_vise_kriterijuma()

    else:
        print("Pogrešan unos!")


def pretrag_ime_prezime(ime, prezime):

    korisnici.println()
    recepcija.ucitaj_recepcionare("recepcionari.txt")
    niz_recepcionara = recepcija.svi_recepcionari

    provjera = False
    novi_niz = []
    for index, i in enumerate(niz_recepcionara):
        if i["ime"] == ime and i["prezime"] == prezime:
            novi_niz.append(i)
            provjera = True
            break

    if provjera == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))
    
    if provjera == False:
        korisnici.println()
        print("Ne postoji traženi recepcionar! ")

def pretraga_username(username):
    korisnici.println()
    recepcija.ucitaj_recepcionare("recepcionari.txt")
    niz_recepcionara = recepcija.svi_recepcionari

    provjera = False
    novi_niz = []
    for index, i in enumerate(niz_recepcionara):
        if i["korisnicko_ime"] == username:
            novi_niz.append(i)
            #print(index, ")", i) 
            provjera = True
            break

    if provjera == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if provjera == False:
        korisnici.println()
        print("Ne postoji traženi recepcionar!")


def recepcionari_po_hotelima():
    korisnici.println()
    print("Odaberite hotel u kome želite vršiti pretragu recepcionara: \n")
    ucitaj_hotele("hoteli.txt")

    novi_niz = []
    for index, i in enumerate(niz_hotela_admin):
        i["redni broj"] = index
        novi_niz.append(i)
        #print(index, ")", i)

    header = novi_niz[0].keys()
    rows =  [x.values() for x in novi_niz]
    print (tabulate(rows, header, tablefmt='grid'))

    odabir = eval(input("Odaberite hotel: "))
    odabrani_hotel = niz_hotela_admin[odabir]

    #print("Odabrali ste hotel: ", odabrani_hotel)

    recepcija.ucitaj_recepcionare("recepcionari.txt")
    niz_recepcionara = recepcija.svi_recepcionari
    #print(niz_recepcionara)

    novi_niz2 = []
    for i in niz_recepcionara:
        prenos = i['id_hotela']
        string_hotela = prenos[0] + prenos[1] + prenos[2] + prenos[3] + prenos[4] + prenos[5] 
        #print(string_hotela)
        #print(odabrani_hotel['id'])
        #print(odabrani_hotel['id'] == string_hotela)
        if odabrani_hotel['id'] == string_hotela:
            novi_niz2.append(i)
        
    header = novi_niz2[0].keys()
    rows =  [x.values() for x in novi_niz2]
    print (tabulate(rows, header, tablefmt='grid'))


def pretraga_recepcionara_po_vise_kriterijuma():
    korisnici.println()
    print("Ukoliko želite da preskočite određeni kriterijum unesite - \n")
    ime = input("Unesite ime recepcionara: ")
    prezime = input("Unesite prezime recepcionara: ")
    kor_ime = input("Unesite korisničko ime recepcionara: ")
    id_hotela = input("Unesite id hotela u kome je recepcionar zaposlen: ")
    pretraga_vkr(ime, prezime, kor_ime, id_hotela)




def pretraga_vkr(ime, prezime, kor_ime, id_hotela):
    korisnici.println()
    recepcija.ucitaj_recepcionare("recepcionari.txt")
    niz_recepcionara = recepcija.svi_recepcionari

    postoji = False
    novi_niz = []
    for i in niz_recepcionara:
        prenos_id = i['id_hotela']
        final_id = prenos_id[0] + prenos_id[1] + prenos_id[2] + prenos_id[3] + prenos_id[4] + prenos_id[5]
        if (ime == i['ime'] or ime == "-") and (i['prezime'] == prezime or prezime == "-") and (i["korisnicko_ime"] == kor_ime or kor_ime == "-") and (final_id == id_hotela or id_hotela == "-"):
            novi_niz.append(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        korisnici.println()
        print("Ne postoji recepcionar sa traženim osobinama!")