import requests

url = "https://bdl.stat.gov.pl/api/v1/data/by-variable/3643?format=json&year=2009&year=2010&year=2011&unit-parent-id=010000000000&unit-level=2"
response = requests.get(url)
data = response.json()

for wojewodztwo in data['results']:
        name = wojewodztwo['name']
        print(f"Województwo: {name}")
        
        # Wypisanie wartości dla każdego roku
        for value in wojewodztwo['values']:
            year = value['year']
            val = value['val']
            print(f" Rok: {year}, Wartość: {val}")
