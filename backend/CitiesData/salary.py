import requests
from bs4 import BeautifulSoup
from config import db
from models.city import City
from unidecode import unidecode

city_mapping = {
    "Warszawa": "Warsaw",
    "Kraków": "Krakow-Cracow",
    "Wrocław": "Wroclaw",
    "Łódź": "Lodz",
    "Poznań": "Poznan",
    "Gdańsk": "Gdansk",
    "Szczecin": "Szczecin",
    "Lublin": "Lublin",
    "Bydgoszcz": "Bydgoszcz",
    "Białystok": "Bialystok"
}

def get_salary(city_name):
    base_url = "https://www.numbeo.com/cost-of-living/in/"
    formatted_city = city_mapping.get(city_name, unidecode(city_name).replace(" ", "-"))
    url = f"{base_url}{formatted_city}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Nie udało się pobrać danych dla {city_name}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    salary_table = soup.find("table", {"class": "data_wide_table"})
    if not salary_table:
        print(f"Nie znaleziono tabeli salary dla miasta {city_name}")
        return None  

    rows = salary_table.find_all("tr")[63:64]
    price = None  

    for row in rows:
        cols = row.find_all("td", {"class": "priceValue"})
        if cols:
            price_text = cols[0].text.strip().replace("zł", "").replace(",", "")
            price = float(price_text)

    if price is None:
        print(f"Nie udało się znaleźć zarobków dla {city_name}")
        return None

    return round(price, 2)


def update_salary():
    with db.session.begin():
        cities = City.query.all()
        for city in cities:
            new_salary = get_salary(city.name)
            if new_salary:
                # Odczytujemy aktualne 'parameters' (jeśli istnieje)
                if city.parameters is None:
                    city.parameters = {}  # Inicjalizujemy pusty słownik, jeśli brak parametrów
                # Dodajemy zarobki do parametrów
                city.parameters['salary'] = new_salary
                print(f"Zaaktualizowano zarobki dla miasta {city.name}")
    db.session.commit()
