from config import db
from models.city import City
import requests
from bs4 import BeautifulSoup

def update_population():
    URL = "https://pl.wikipedia.org/wiki/Lista_miast_w_Polsce"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "wikitable sortable"})

    if table:
        rows = table.find_all("tr")[1:]  # Pomijamy nagłówek

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 5:
                city_name = cols[1].text.strip()
                population = cols[3].text.strip().replace("\u202f", "").replace(" ", "").replace("\xa0", "")

                try:
                    population = int(population)
                except ValueError:
                    continue  # Pomijamy, jeśli nie da się sparsować

                city = City.query.filter_by(name=city_name).first()

                if city:
                    # Aktualizujemy tylko parametr "populacja"
                    city.parameters["populacja"] = population
                else:
                    # Tworzymy nowe miasto z parametrem "populacja"
                    city = City(name=city_name, parameters={"populacja": population})
                    db.session.add(city)

        db.session.commit()
        print("Populacja miast została zaktualizowana!")
