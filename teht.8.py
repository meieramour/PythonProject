import mysql.connector
from geopy import distance

icao = input("Anna ICAO-koodi: ")
yhteys = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "lentokentat",
    user = "ace",
    password = "qwerty123456"
)
sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
pyquest = yhteys.cursor()
pyquest.execute(sql)
tulos = pyquest.fetchall()
if pyquest.rowcount > 0:
    for rivi in tulos:
        print(f"{rivi[0]}, {rivi[1]}")
else:
    print("ICAO-koodi ei olemassa.")                    #1


koodi = input("Anna maakoodin: ")
sql = f"SELECT type, COUNT(type) FROM airport WHERE iso_country = '{koodi}' GROUP BY type"
pyquest = yhteys.cursor()
pyquest.execute(sql)
tulos = pyquest.fetchall()
if pyquest.rowcount > 0:
    for rivi in tulos:
        print(f"{rivi[0]}: {rivi[1]}")
else:
    print("Maakoodi ei olemassa.")                      #2


icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")
sql1 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}'"
sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao2}'"
pyquest = yhteys.cursor()
pyquest.execute(sql1)
tulos1 = pyquest.fetchall()
pyquest = yhteys.cursor()
pyquest.execute(sql2)
tulos2 = pyquest.fetchall()
dist = distance.distance(tulos1[0], tulos2[0])
print(f"Distance is {dist.kilometers} kilometers.")


