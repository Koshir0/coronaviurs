from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/")
def index():
    request = requests.get("https://www.worldometers.info/coronavirus/")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find(class_="maincounter-number")
    conronaRate = element.text
    return render_template("index.html",  conronaRate = conronaRate)


@app.route("/aboutvirus")
def aboutvirus():
    return render_template("aboutvirus.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/aboutcorona")
def aboutcorona():
    return render_template("aboutcorona.html")

@app.route("/ar")
def ar():
    request = requests.get("https://www.worldometers.info/coronavirus/")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    numberlist = []
    for span in soup.find_all("div", class_="maincounter-number"):
        numberlist.append(span.get_text())
    # print(numberlist[0])
    obj = {"cases":numberlist[0],
            "deaths": numberlist[1]}
    # element = soup.find("div", class_="maincounter-number")
    # conronaRate = element.text
    # death = element.next_element
    # death = soup.find_next_element("div", class_="maincounter-number")
    return render_template("indexar.html", obj = obj)


@app.route("/aboutvirusar")
def aboutvirusar():
    return render_template("aboutvirusar.html")

@app.route("/aboutusar")
def aboutusar():
    return render_template("aboutusar.html")

@app.route("/aboutcoronaar")
def aboutcoronaar():
    return render_template("aboutcoronaar.html")