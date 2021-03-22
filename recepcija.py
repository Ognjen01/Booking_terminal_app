# Ovdje implementujemo rad sa recepcionarom 
import datetime
import korisnici
from tabulate import tabulate

svi_recepcionari = []
trenutno_prijavljen_recepcionar = {}
sobe = []

def recepcionar():

    korisnici.println()
    print("Odabrali ste opciju recepcionar! \n")
    prijava_recepcionara()


def prijava_recepcionara():
    print("Molimo unesite korisničko ime i lozinku: \n")
    provjera = True
    while provjera == True:
    
        kor_ime = input("Korisničko ime: ")
        lozinka = input("Lozinka: ")

        ucitaj_recepcionare("recepcionari.txt")

        recepcionar = {}
        for i in svi_recepcionari:
            if lozinka == i['lozinka'] and kor_ime == i['korisnicko_ime']:
                trenutno_prijavljen_recepcionar.update(i)
                provjera = False

        if provjera == True:
            korisnici.println()
            print("Nepostojeci nalog, molimo pokusajte ponovo!")

    korisnici.println()
    print("Dobrodošli ", trenutno_prijavljen_recepcionar['ime'])

    if provjera == False:
        opcije_recepcionara() 


def ucitaj_recepcionare(nazivFajla):

    svi_recepcionari.clear()
    target = open(nazivFajla, "r")

    for red in target.readlines():
        svi_recepcionari.append(str2Recepcionar(red))
    target.close()


def str2Recepcionar(red):
   

    rec_podaci = {}
    dio = red.split("|")

    rec_podaci['korisnicko_ime'] = dio[0]
    rec_podaci['lozinka'] =  dio[1]
    rec_podaci['ime'] =  dio[2]
    rec_podaci['prezime'] =  dio[3]
    rec_podaci['telefon'] =  dio[4]
    rec_podaci['email'] =  dio[5]
    rec_podaci['uloga'] =  dio[6]
    rec_podaci['id_hotela'] =  dio[7]

    return rec_podaci


def opcije_recepcionara():
    unos = ""
 
    while unos != "4":
        korisnici.println()
        print("\nOdaberite neku od opcija: \n")
        print("1) Pretraga soba")
        print("2) Pretraga rezervacija")
        print("3) Kreiraj izvještaj")
        print("4) Izlaz \n")

        unos = input("Unesite neku od opcija: ")

        if unos == "1":
            pretraga_soba()

        elif unos == "2":
            pretraga_rezervacija()
        
        elif unos == "3":
            izvjestaj()

        elif unos == "4":
            odjava()

        else:
            korisnici.println()
            print("Unijeli ste nepostojeću opciju! ")
            print("Molimo ponovite unos")

def pretraga_soba():
    korisnici.println()
    print("Odabrali ste pretragu soba \n")
    print("1) Pretaraga po jednom kriterijumu")
    print("2) Pretaraga po više kriterijuma\n")
    odabir = input("Odaberite opciju: ")

    if odabir == "1":
        korisnici.println()
        print("\nOdabrali ste pretragu po jednom kriterijumu. ")
        print("Odaberite po kom kriterijumu želite pretragu: \n")
        print("1) Pretraga po hotelu")
        print("2) Pretraga po broju kreveta")
        print("3) Pretraga po cijeni")
        print("4) Smještaji koji imaju TV")
        print("5) Smještaji koji imeju klimu")
        print("6) Pretraga po tipu smještaja\n")


        unos = input("Odaberite opciju:")

        if unos == "1":
            pretraga_po_hotelima()
        elif unos == "2":
            pretraga_br_kreveta()
        elif unos == "3":
            pretraga_cijena()
        elif unos == "4":
            pretraga_tv()
        elif unos == "5":
            pretraga_klima()
        elif unos == "6":
            pretraga_tip()
        else:
            korisnici.println()
            print("Unijeli ste nepostojeću opciju! ")



    elif odabir == "2":
        korisnici.println()
        print("Odabrali ste pretargu po više kriterijuma: \n")
        pretraga_soba_po_vise_kriterijuma()
        

    else:
        print("Odabrali ste nepostojecu opciju!")


# --------- PRETRAGE SOBA PO JEDNOM KRITERIJUMU --------------        

def pretraga_po_hotelima():
    korisnici.ucitaj_hotele("hoteli.txt")
    hoteli = korisnici.niz_hotela
    korisnici.println()
    print("Molimo odaberite hotel: \n")

    hot_niz = []
    for index, i in enumerate(hoteli):
        i["redni broj"] = index
        hot_niz.append(i)
        #print(index, ")", i)
    print(" ")

    header = hot_niz[0].keys()
    rows =  [x.values() for x in hot_niz]
    print (tabulate(rows, header, tablefmt='grid'))

    odabir = eval(input("Odaberite hotel: "))
    odabrani_hotel = hoteli[odabir]

    korisnici.sobe.clear()
    korisnici.ucitavanje_soba("sobe.txt")
    sobe = korisnici.sobe
    korisnici.println()

    postoji = False

    novi_niz = []

    for i in sobe:
        if i["hotelID"] == odabrani_hotel['id']:
            novi_niz.append(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        print("Jos uvijek nije dodata niti jedna soba u trazeni hotel!")
    

def pretraga_br_kreveta():
    korisnici.println()
    br_kreveta =  eval(input("Traženi broj kreveta: "))

    korisnici.sobe.clear()
    korisnici.ucitavanje_soba("sobe.txt")
    sobe = korisnici.sobe

    novi_niz = []
    postoji = False
    for i in sobe:
        if i["brKreveta"] == str(br_kreveta):
            novi_niz.append(i)
            #print(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))
    
    if postoji == False:
        korisnici.println()
        print("Ne postoji soba po trazenom uslovu!")


def pretraga_cijena():
    korisnici.println()
    maksimalna_cijena =  eval(input("\nUnesite gornji cjenovni limit: "))

    korisnici.sobe.clear()
    korisnici.ucitavanje_soba("sobe.txt")
    sobe = korisnici.sobe

    novi_niz = []
    postoji = False
    for i in sobe:
        if eval(i["cijena"]) <= maksimalna_cijena:
            novi_niz.append(i)
            #print(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        korisnici.println()
        print("Ne postoji soba po trazenom uslovu!")


def pretraga_tv():
    korisnici.println()
    izbor = input("Da li želite sobu sa TV-om: ")
    print(" ")

    korisnici.sobe.clear()
    korisnici.ucitavanje_soba("sobe.txt")
    sobe = korisnici.sobe

    novi_niz = []
    postoji = False
    for i in sobe:
        vr = i['tv']
        vr.split('\n')
        if vr[0] == izbor[0]:
            novi_niz.append(i)
            #print(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        korisnici.println()
        print("Ne postoji soba po trazenom uslovu!")


def pretraga_klima():
    korisnici.println()
    izbor = input("Da li želite sobu sa klimom: ")
    print(" ")

    korisnici.sobe.clear()
    korisnici.ucitavanje_soba("sobe.txt")

    sobe = korisnici.sobe

    novi_niz = []
    postoji = False
    for i in sobe:
        
        if i['klima'] == izbor:
            novi_niz.append(i)
            #print(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        korisnici.println()
        print("Ne postoji soba po trazenom uslovu!")

def pretraga_tip():
    korisnici.println()
    izbor = input("Koji tip smještaja želite? (soba/apartman): ")
    print(" ")

    korisnici.sobe.clear()
    korisnici.ucitavanje_soba("sobe.txt")
    sobe = korisnici.sobe

    novi_niz = []
    postoji = False
    for i in sobe:
        
        if i['tip'] == izbor:
            novi_niz.append(i)
            #print(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        korisnici.println()
        print("Ne postoji soba po trazenom uslovu!")


# ------------ RETRAGA SOBA PO VISE KRITERIJUMA ---------------

def pretraga_soba_po_vise_kriterijuma():
    korisnici.println()
    print("Ukoliko želite da preskočite određeni kriterijum unesite - \n")
    id_hotela1 = input("ID hotela: ")
    br_kreveta1 = input("Broj kreveta u sobi: ")
    cijena1 = input("Cijena noćenja: ")
    tv1 = input("Da li smještaj treba da ima tv? (da/ne): ")
    klima1 = input("Da li smještaj treba da ima klimu? (da/ne): ")
    tip1 = input("Koji je tip traženog smještaja? (soba/apartman): ")

    korisnici.sobe.clear()
    korisnici.ucitavanje_soba("sobe.txt")
    niz_soba = korisnici.sobe

    postoji = False
    novi_niz =[]

    for i in niz_soba:
        prenos = i['tv']
        ima_tv = prenos[0] + prenos[1]

        if (id_hotela1 == i['hotelID'] or id_hotela1 == "-") and (cijena1 == i['cijena'] or cijena1 == "-") and (tv1 == ima_tv or tv1 == "-") and (klima1 == i['klima'] or klima1 == "-") and (tip1 == i['tip'] or tip1 == "-") and (br_kreveta1 == i['brKreveta'] or br_kreveta1 == "-"):
            novi_niz.append(i)
            # print(i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        print("Ne postoji tražena soba! ")



def pretraga_rezervacija():
    korisnici.println()
    print("Odabrali ste pretragu rezervacija \n")
    print("1) Pretaraga po jednom kriterijumu")
    print("2) Pretaraga po više kriterijuma\n")
    odabir = input("Odaberite opciju: ")

    if odabir == "1":
        korisnici.println()
        print("Odabrali ste pretragu po jednom kriterijumu: ")
        print("Odaberite po kom kriterijumu želite pretragu: \n")

        print("1) Pretraga po statusu rezervacije")
        print("2) Pretraga po korisniku")
        print("3) Pretraga po datumu prijave i odjava")
        print("4) Pretraga po datumu kreiranja\n")

        
        
        unos = input("Odaberite opciju:")

        if unos == "1":
            pretraga_po_statusu_rez()
        elif unos == "2":
            pretraga_korisnik()
        elif unos == "3":
            pretraga_datum_pr_od()
        elif unos == "4":
            pretraga_datum_kreiranja()
        
        else:
            korisnici.println()
            print("Unijeli ste nepostojeću opciju! ")



    elif odabir == "2":
        korisnici.println()
        print("Odabrali ste pretargu po više krierijuma: \n")
        pretraga_rezervacija_vise_kriterijuma()

    else:
        print("Odabrali ste nepostojecu opciju!")



# ------------- PRETRAGA REZERVACIJA PO JEDNOM KRITERJUMU ----------------

def pretraga_po_statusu_rez():
    korisnici.println()
    status = input("Molimo unesite željeni status rezrvacije (rezervisano/ u toku/ istekla): ")
    print(" ")
    korisnici.niz_rezervacija.clear()
    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    novi_niz = []
    postoji = False
    for index, i in enumerate(niz_rez):
        if status == i['status']:
            novi_niz.append(i)
            #print(index,")", i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        print("Ne postoji rezervacija sa trazenim uslovom!")


def pretraga_korisnik():
    korisnici.println()
    korisnik = input("Molimo unesite korisničko ime korisnika: ")
    print(" ")

    korisnici.niz_rezervacija.clear()
    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    novi_niz = []
    postoji = False
    for index, i in enumerate(niz_rez):
        if korisnik == i['korisnik']:
            novi_niz.append(i)
            #print(index,")", i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))
    

    if postoji == False:
        print("Ne postoji rezervacija sa trazenim uslovom!")



def pretraga_datum_pr_od():
    korisnici.println()
    datum_prijave = input("Molimo unesite zakazani datum prijave (yyyy-mm-dd): ")
    datum_odjave = input("Molimo unesite zakazani datum odjave (yyyy-mm-dd): ")
    print(" ")

    korisnici.niz_rezervacija.clear()
    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    novi_niz = []
    postoji = False
    for index, i in enumerate(niz_rez):
        #pr = datetime.date(i['datumPrijave'])
        #od = datetime.date(i['datumOdjave'])
        if datum_prijave == i['datumPrijave'] and datum_odjave == i['datumOdjave']:
            novi_niz.append(i)
            #print(index,")", i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))
    
    if postoji == False:
        print("Ne postoji rezervacija sa trazenim uslovom!")


def pretraga_datum_kreiranja():
    korisnici.println()
    datum_kreiranja = input("Unesite datum kreiranja rezervacije (yyyy-mm-dd): ")
    print(" ")

    korisnici.niz_rezervacija.clear()
    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    novi_niz = []
    postoji = False
    for index, i in enumerate(niz_rez):
        date_time_obj = datetime.datetime.strptime(i['vrijemeKreiranja'], '%Y-%m-%d %H:%M:%S.%f')
        datum = str(date_time_obj.date())
        #print(datum, datum_kreiranja)
        if datum_kreiranja == datum:
            novi_niz.append(i)
            #print(index,")", i)
            postoji = True

    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        print("Ne postoji rezervacija sa trazenim uslovom!")


# ---------- PRETRAGA REZERVACIJA PO VISE KRITERIJUMA --------------

def pretraga_rezervacija_vise_kriterijuma():
    korisnici.println()
    print("Ukoliko želite da preskočite određeni kriterijum unesite - \n")
    kor_ime = input("Unesite korisničko ime korisnika koji je kreirao rezervaciju: ")
    datum_prijave = input("Datum prijave (yyyy-mm-dd): ")
    datum_odjave = input("Datum odjave (yyyy-mm-dd): ")
    status = input("Trenutni status rezervacije (u toku/rezervisano/istekla): ")

    korisnici.niz_rezervacija.clear()
    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    novi_niz = []
    postoji = False
    korisnici.println()
    for i in niz_rez:
        if (kor_ime == i['korisnik'] or kor_ime == "-") and (datum_prijave == i['datumPrijave'] or datum_prijave =="-") and (datum_odjave == i['datumOdjave'] or datum_odjave == "-") and (status == i['status'] or status == "-"):
            novi_niz.append(i)
            #print(i)
            postoji = True

    
    if postoji == True:
        header = novi_niz[0].keys()
        rows =  [x.values() for x in novi_niz]
        print (tabulate(rows, header, tablefmt='grid'))

    if postoji == False:
        korisnici.println()
        print("Ne postoji tražena rezervacija! \n")




def izvjestaj():
    korisnici.println()
    print("Odaberite tip izvještaja koji želite da napravite: \n")
    print("1) Dnevni izvještaj")
    print("2) Sedmični izvještaj")
    print("3) Mjesečni izvještaj\n")

    unos = input("Odaberite opciju: ")

    if unos == "1":
        dnevni_izvjestaj()
    
    elif unos == "2":
        sedmicni_izvjestaj()
    
    elif unos == "3":
        mjesecni_izvjestaj()

    else:
        korisnici.println()
        print("Odabrali ste nepostojecu opciju!")


    # U izvjestaj idu: 
    # Lista realizovanih rezervacija za dati period
    # Ukupan broj realizovanih rez
    # Ukupan broj izdatih soba
    # Ukupna zarada za dati period
    # Prosjecna ocjena hotela za dati period

def dnevni_izvjestaj():
    korisnici.println()
    # IZVJESTAJ RADITI SAMO ZA HOTEL U KOJEM RADI RECEPCIONAR
    x = datetime.datetime.now()
    trenutni_datum = str(x.date())

    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    danasnje_rezervacije = []
    danasnji_prihod = 0
    brojac_rezervacija = 0


    strin = trenutno_prijavljen_recepcionar['id_hotela']
    potpun_id = strin[0] + strin[1] + strin[2] + strin[3] + strin[4] + strin[5] 

    for i in niz_rez:
        if potpun_id == i['idHotela'] and (i['datumPrijave'] == trenutni_datum or i['datumOdjave'] == trenutni_datum):
            danasnje_rezervacije.append(i)
            brojac_rezervacija = brojac_rezervacija + 1 
            if  i['datumOdjave'] == trenutni_datum:
                danasnji_prihod = danasnji_prihod + eval(i['cijenaRezervacije'])

    print("Današnje rezervacije: ")
    
    header = danasnje_rezervacije[0].keys()
    rows =  [x.values() for x in danasnje_rezervacije]
    print (tabulate(rows, header, tablefmt='grid'))


    print("Ukupno rezervacija danas -> ", brojac_rezervacija)
    print("Današnji prihod: ", danasnji_prihod, " eura")  


        


def sedmicni_izvjestaj():
    korisnici.println()
    print("Izvještaj za prethodnih sedam dana:\n")

    trenutni_datum = datetime.datetime.now()
    #trenutni_datum = x.datetime()

    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    # Formiranje datuma prije sedam dana
    datum_prije_7_dana = trenutni_datum - datetime.timedelta(days=7)

    print("\n",trenutni_datum)
    print(datum_prije_7_dana)

    # Formiranje id recepcioanara kako bi on gledao samo hotel kojem pripada
    strin = trenutno_prijavljen_recepcionar['id_hotela']
    potpun_id = strin[0] + strin[1] + strin[2] + strin[3] + strin[4] + strin[5]

    sedmicni_niz_rezervacija = []
    brojac_rezervacija = 0
    sedmicni_prihod = 0

    for i in niz_rez:

        if potpun_id == i['idHotela']:
        
            datum_prijave = datetime.datetime.strptime(i['datumPrijave'], '%Y-%m-%d')
            datum_odjave = datetime.datetime.strptime(i['datumOdjave'], '%Y-%m-%d')

            if datum_prijave > datum_prije_7_dana and datum_prijave < trenutni_datum:
                sedmicni_niz_rezervacija.append(i)
                brojac_rezervacija = brojac_rezervacija + 1

                if datum_odjave < trenutni_datum and datum_odjave > datum_prije_7_dana:
                    
                    # Dodajemo vrijednost prihodu u toj sedmici
                    sedmicni_prihod = sedmicni_prihod + eval(i['cijenaRezervacije'])
                    
                

            elif datum_odjave < trenutni_datum and datum_odjave > datum_prije_7_dana:
                sedmicni_niz_rezervacija.append(i)
                brojac_rezervacija = brojac_rezervacija + 1
                # Dodajemo vrijednost prihodu u toj sedmici
                sedmicni_prihod = sedmicni_prihod + eval(i['cijenaRezervacije'])
            

    print("Rezervacije realizovane ove sedmice -> ")

    
    header = sedmicni_niz_rezervacija[0].keys()
    rows =  [x.values() for x in sedmicni_niz_rezervacija]
    print (tabulate(rows, header, tablefmt='grid'))

    print("Ukupno rezervacija ove sedmice -> ", brojac_rezervacija)
    print("Sedmični prihod: ", sedmicni_prihod, " eura") 
 


def mjesecni_izvjestaj():
    korisnici.println()
    print("Izvještaj za prethodnih 30 dana:\n")

    trenutni_datum = datetime.datetime.now()
    #trenutni_datum = x.date()

    korisnici.ucitaj_rezervacije("rezervacije.txt")
    niz_rez = korisnici.niz_rezervacija

    # Formiranje datuma prije sedam dana
    datum_prije_30_dana = trenutni_datum - datetime.timedelta(days=30)

    print("\n",trenutni_datum)
    print(datum_prije_30_dana)

    # Formiranje id recepcioanara kako bi on gledao samo hotel kojem pripada
    strin = trenutno_prijavljen_recepcionar['id_hotela']
    potpun_id = strin[0] + strin[1] + strin[2] + strin[3] + strin[4] + strin[5]

    mjesecni_niz_rezervacija = []
    brojac_rezervacija = 0
    mjesecni_prihod = 0

    for i in niz_rez:

        if potpun_id == i['idHotela']:
        
            datum_prijave = datetime.datetime.strptime(i['datumPrijave'], '%Y-%m-%d')
            datum_odjave = datetime.datetime.strptime(i['datumOdjave'], '%Y-%m-%d')

            if datum_prijave > datum_prije_30_dana and datum_prijave < trenutni_datum:
                mjesecni_niz_rezervacija.append(i)
                brojac_rezervacija = brojac_rezervacija + 1

                if datum_odjave < trenutni_datum and datum_odjave > datum_prije_30_dana:
                    
                    # Dodajemo vrijednost prihodu u toj sedmici
                    mjesecni_prihod = mjesecni_prihod + eval(i['cijenaRezervacije'])
                    
                

            elif datum_odjave < trenutni_datum and datum_odjave > datum_prije_30_dana:
                mjesecni_niz_rezervacija.append(i)
                brojac_rezervacija = brojac_rezervacija + 1
                # Dodajemo vrijednost prihodu u toj sedmici
                mjesecni_prihod = mjesecni_prihod + eval(i['cijenaRezervacije'])
            

    print("Rezervacije realizovane u prethodnih 30 dana -> ")

    header = mjesecni_niz_rezervacija[0].keys()
    rows =  [x.values() for x in mjesecni_niz_rezervacija]
    print (tabulate(rows, header, tablefmt='grid'))

    print("Ukupno rezervacija u prethodnih 30 dana -> ", brojac_rezervacija)
    print("Ukupan prihod u prethodnih 30 dana: ", mjesecni_prihod, " eura") 



def odjava():
    korisnici.println()
    print("Odjavili ste se sa aplikacije!")