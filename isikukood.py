from datetime import date
ID = input("Palun sisestage oma isikukood: ")


def validate_id(isikukood):
    global e_arv
    if len(isikukood) != 11:
        raise ValueError("Isikukood peab olema 11 tähemärki pikk!")
    e_arv = isikukood[0:1]
    if e_arv < "1" or e_arv > "6":
        raise ValueError("Sisestage korrektne isikukood (esimene number 1-6)")


def getiddata(isikukood):
    validate_id(isikukood)

    global sugu
    global saLopp
    global skPaev
    global skNumber
    global jarjekorranumber
    global kontrollnumber
    global synnipaev
    global prgAasta

    saLopp = isikukood[1:3]
    skPaev = isikukood[5:7]
    skNumber = isikukood[3:5]
    jarjekorranumber = isikukood[7:10]
    kontrollnumber = isikukood[10]

    if e_arv in ('1', '3', '5'):
        sugu = "mees"
    if e_arv in ('2', '4', '6'):
        sugu = "naine"

    if e_arv in ('1', '2'):
        synnipaev = skPaev + "/" + skNumber + "/" + "18" + saLopp
    if e_arv in ('3', '4'):
        synnipaev = skPaev + "/" + skNumber + "/" + "19" + saLopp
    if e_arv in ('5', '6'):
        synnipaev = skPaev + "/" + skNumber + "/" + "20" + saLopp

    # 30 päevaga kuud, kui isikukoodis skPaev on suurem kui 30, kood peatatakse.
    if skNumber in ('04', '06', '09', '11'):
        if skPaev > "30":
            raise ValueError("Sellel kuul ei ole rohkem kui 30 päeva!")

    # 31 päevaga kuud, kui isikukoodis skPaev on suurem kui 31, kood peatatakse.
    if skNumber in ('01', '03', '05', '07', '08', '10', '12'):
        if skPaev > "31":
            raise ValueError("Sellel kuul ei ole rohkem kui 31 päeva!")

    # Veebruaris on liigaastatel 1 päev rohkem, kui skPaev ei klapi, kood peatatakse.
    liigaasta(int(synnipaev[6:11]))
    if liigaasta is True:
        if skPaev > "29":
            raise ValueError("Sellel kuul ei ole rohkem kui 29 päeva!")
    if liigaasta is False:
        if skPaev > "28":
            raise ValueError("Sellel kuul ei ole rohkem kui 28 päeva!")

    # Inimene ei saa sündida tulevikus
    prgAasta = date.today().year

    if int(synnipaev[6:11]) > prgAasta:
        raise ValueError("Inimene ei saa sündida tulevikus")


def liigaasta(aasta):
    global liigaasta

    if (aasta % 4) == 0:
        if (aasta % 100) == 0:
            if (aasta % 400) == 0:
                liigaasta = True
            else:
                liigaasta = False
        else:
            liigaasta = True
    else:
        liigaasta = False


getiddata(ID)

print("Sündinud                 " + synnipaev)
print("Sugu                     " + sugu)
print("Teie järjekorranumber on " + jarjekorranumber)
print("Teie kontrollnumber on   " + kontrollnumber)
