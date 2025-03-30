from CitiesData.population import update_population
from CitiesData.costOfLiving import update_cost_of_living
from CitiesData.salary import update_salary
from CitiesData.costRestaurant import update_restaurant_cost
from CitiesData.apartmentRental import update_apartament_rental

def update_data():
    update_apartament_rental()
    update_population()
    update_restaurant_cost()
    update_salary()
    update_cost_of_living()