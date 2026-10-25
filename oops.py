class coffee:

    # constructor
    def __init__(self, type,size, has_sugar, type_of_milk):
        self.type = type
        self.size = size
        self.has_sugar = has_sugar
        self.type_of_milk = type_of_milk
        if type == "Americano":
            self.type_of_milk = None
        else:
            self.type_of_milk = type_of_milk

coffee_for_mithul = coffee("Americano", "small", True, None)
coffee_for_smitha = coffee("Latte", "large", False, "soy milk")

print(coffee_for_mithul.__dict__)
print(coffee_for_smitha.__dict__)