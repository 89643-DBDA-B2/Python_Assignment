class Painting:
    def calculatePaintingCost(self):
        pass

class FlatPainting(Painting):
    def __init__(self, noOfRooms):
        self.noOfRooms = noOfRooms
    
    def calculatePaintingCost(self):
        return self.noOfRooms * 10000

class BuildingPainting(Painting):
    def __init__(self, noOfFlats):
        self.noOfFlats = noOfFlats
    
    def calculatePaintingCost(self):
        return self.noOfFlats * 25000


    flat_painting = FlatPainting(5)
    

    building_painting = BuildingPainting(8)

print("Flat Painting Cost:", flat_painting.calculate_building_painting_cost())  
print("Building Painting Cost:", building_painting.calculatePaintingCost()) 
