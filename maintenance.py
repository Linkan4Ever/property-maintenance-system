class Maintenance:
    def __init__(self, location, starttime, endtime, cost, description, esttechservtime, name):
        self.location = location
        self.starttime = starttime
        self.endtime = endtime
        self.cost = cost
        self.description = description
        self.esttechservtime = esttechservtime
        self.name = name

main_1 = Maintenance("Badrum", "2022-01-01", "2022-01-02", 4000, "testbeskrivning", 20, "Renovering av badrum")

print(main_1.cost)


def create():
    print("Creating new maintenance post.")

def edit():
    print("Editing maintenance post.")
