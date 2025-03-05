# Create a class named Mobile with attributes ModelName,Company,Price and with
# methods:set_attributes, print_details and can_afford

class Mobile :
    def __init__(self, ModelName , Company , Price):
        print(f"Inside initializer of {self}")
        self.ModelName = ModelName
        self.Company = Company
        self.Price = Price

    def setting(self, ModelName , Company , Price):
        self.ModelName = ModelName
        self.Company = Company
        self.Price = Price

    def getting(self):
        return self.__dict__
    
mobile1 =Mobile("S2","Hyundai","100000")

print(f"The values are {mobile1.getting()}")

mobile1.setting("s3","Suzuki","545055")

print(f"The updated values are {mobile1.getting()}")

print
