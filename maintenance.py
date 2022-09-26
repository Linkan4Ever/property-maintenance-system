class Maintenance:
    def __init__(self, location, startTime, endTime, cost, description, esttechservlife, name):
        self.location = location
        self.starttime = startTime
        self.endtime = endTime
        self.cost = cost
        self.description = description
        self.esttechservlife = esttechservlife
        self.name = name
        self.timeCreated = 

maint_1 = Maintenance("Badrum", "2022-01-01", "2022-01-02", 4000, "testbeskrivning", 20, "Renovering av badrum")

print(maint_1.cost)


def create():
    print("Creating new maintenance post.")

def edit():
    print("Editing maintenance post.")
