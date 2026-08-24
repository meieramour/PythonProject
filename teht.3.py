pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.") #1

hyttiluokka = input("Anna hyttiluokka (LUX, A, B, C): ")

if hyttiluokka == "LUX":
    print("Parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("Ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("Ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("Ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka") #2

sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.") #3

vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")
elif vuosi % 100 == 0:
    print("Vuosi ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.") #4