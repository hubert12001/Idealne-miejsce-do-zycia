from config import db
from models import City
import requests
from bs4 import BeautifulSoup

def update_population():
    URL = "https://pl.wikipedia.org/wiki/Lista_miast_w_Polsce"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "wikitable sortable"})

    if table:
        rows = table.find_all("tr")[1:]

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 5:
                city_name = cols[1].text.strip()
                population = cols[3].text.strip().replace("\u202f", "").replace(" ", "")

                # Czy miasto jest już w bazie?
                city = City.query.filter_by(name=city_name).first()

                if city:
                    # Jeśli istnieje, aktualizujemy populację
                    city.population = int(population)
                else:
                    # Jeśli nie istnieje, dodajemy nowe miasto
                    city = City(name=city_name, population=int(population))
                    db.session.add(city)

        db.session.commit()  # Zapisujemy zmiany do bazy
        print("Populacja miast została zaktualizowana!")
