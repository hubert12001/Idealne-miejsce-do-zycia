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

def get_restaurant_cost(city_name):
    base_url = "https://www.numbeo.com/cost-of-living/in/"
    formatted_city = city_mapping.get(city_name, unidecode(city_name).replace(" ", "-"))
    url = f"{base_url}{formatted_city}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Nie udało się pobrać danych dla {city_name}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")

    restaurant_table = soup.find("table", {"class": "data_wide_table"})
    if not restaurant_table:
        print(f"Nie znaleziono tabeli 'Restaurant' dla {city_name}")
        return None 

    prices = []
    rows = restaurant_table.find_all("tr")[1:9]
    for row in rows:
        cols = row.find_all("td", {"class": "priceValue"})
        if cols:
            price_text = cols[0].text.strip().replace("zł", "").replace(",", ".")
            try:
                price = float(price_text)
                prices.append(price)
            except ValueError:
                continue
    if not prices:
        print(f"Nie udało się znaleźć cen restauracja dla {city_name}")
        return None
    
    avg_restaurant_cost = sum(prices) / len(prices)
    return round(avg_restaurant_cost, 2)

def update_restaurant_cost():
    with db.session.begin():
        cities = City.query.all()
        for city in cities:
            new_cost = get_restaurant_cost(city.name)
            if new_cost:
                city.parameters['restaurant_cost'] = new_cost
                print(f"Zaktualizowano restauracje {city.name}: {new_cost} PLN")

        db.session.commit()