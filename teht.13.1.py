from flask import Flask

app = Flask(__name__)
@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    a = True
    if luku < 2:
        a = False
    else:
        for i in range (2, luku):
            if luku % i == 0:
                a = False
                break
    return {"Number": luku, "isPrime": a}
if __name__ == "__main__":
    app.run(port=3000)