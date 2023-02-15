from Database.LinkCostDB import MongoDbHandler


class RouteCost:
    def __init__(self):
        # data base route cost
        self.db = MongoDbHandler(database="SDN_data", collection="Route_Cost")
        self.db.remove_all()

    def update_route_cost(self, list_of_dicts):
        for route in list_of_dicts:
            # Define the filter to find the document with the matching "src" and "dst" values
            filter_route = {"src": route["src"], "dst": route["dst"]}

            result_route = self.db.find_data(filter_route)

            # neu link khong ton tai trong DB thi chen link vao DB
            if result_route == False:
                new_route = {
                    "src": route["src"],
                    "dst": route["dst"],
                    "avg_cost": route['cost'],
                    "count": 1
                }
                self.db.insert_one_data(new_route)
                print("insert")
            # neu tim thay link trong DB thi update cost 
            else:
                new_count = result_route['count'] + 1
                new_total_cost = result_route['avg_cost'] + route['cost']
                update_avg_cost = new_total_cost / new_count
                update = {
                    "$set": {"avg_cost": update_avg_cost, "count": new_count}}
                self.db.update_data(filter_route, update)

    