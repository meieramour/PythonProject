from flask import Flask
import mysql.connector

app1 = Flask(__name__)
yhteys = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "lentokentat",
    user = "ace",
    password = "qwerty123456"
)
@app1.route("/kenttä/<icao>")
def k(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    pyquest = yhteys.cursor()
    pyquest.execute(sql, (icao,))
    tulos = pyquest.fetchone()
    if tulos is not None:
        return {
            "ICAO": icao,
            "Name": tulos[0],
            "Municipality": tulos[1]
        }
    else:
        return {"error": "Airport not found"}, 404
if __name__ == "__main__":
    app1.run(port=3000)