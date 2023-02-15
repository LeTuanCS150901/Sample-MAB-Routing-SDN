# Example usage of RouteCost class
from RouteCost.route_cost import RouteCost
route_cost = RouteCost()

# Example input data
list_of_dicts = [
    {"src": "A", "dst": "B", "cost": 10.0},
    {"src": "B", "dst": "A", "cost": 20.0},
    {"src": "A", "dst": "B", "cost": 15.0},
    {"src": "C", "dst": "D", "cost": 5.0}
]

list_of_dicts_2 = [
    {"src": "A", "dst": "B", "cost": 3},
    {"src": "B", "dst": "A", "cost": 4},
    {"src": "A", "dst": "B", "cost": 5},
    {"src": "C", "dst": "D", "cost": 6}
]


# Call the process_data method
route_cost.update_route_cost(list_of_dicts)
route_cost.update_route_cost(list_of_dicts_2)
