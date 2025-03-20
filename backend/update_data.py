from CitiesData.population import update_population
from CitiesData.costOfLiving import update_cost_of_living
from CitiesData.salary import update_salary
from CitiesData.costRestaurant import update_restaurant_cost

def update_data():
    update_population()
    update_restaurant_cost()
    update_salary()
    update_cost_of_living()