class Acura:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
class RDX(Acura):
    def __init__(self, selfParking, make, model, year):
        Acura.__init__(self, make, model, year)
        self.selfParking = selfParking

RDX = RDX(True, "Acura", "AWD", "2020")
print(RDX.selfParking)
print(RDX.make)
print(RDX.model)
print(RDX.year)
