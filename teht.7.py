vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukausi = int(input("Anna kuukauden numero (1-12): "))
indeksi = (kuukausi % 12) // 3
print(vuodenajat[indeksi])                      #1

nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)                     #2

lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto: uusi, haku, tai lopeta: ")

    if toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ")

        if  icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif toiminto == "lopeta":
        break

