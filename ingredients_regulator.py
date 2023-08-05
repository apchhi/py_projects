## Сook ingredients regulator 

# for 48 buns:
buns = 48

# glass
sugar = 1.5
oil = 1
flour = 2.75

print("This is the cook program. Сook ingredients regulator. Enter how many bund you wand and cook will show ingredients.\n")

class ingredients:
    def __init__(self, how_buns):
        self.how_buns = how_buns

    def ingted_sugar(self):
        self.bun_sugar = (sugar / buns) * self.how_buns
        return self.bun_sugar

    def ingred_oil(self):
        self.bun_oil = (oil / buns) * self.how_buns
        return self.bun_oil
    
    # muka
    def ingred_flour(self):
        self.bun_flour = (flour / buns) * self.how_buns
        return self.bun_flour

while True:
    how_buns = input("Enter how many buns: ")
    if how_buns == "stop":
        print("\nExit from program a cook. Bye! ")
        break 
        
    all_ingred = ingredients(float(how_buns))

    sugar_resilt = all_ingred.ingted_sugar()
    oil_result = all_ingred.ingred_oil()
    flour_result = all_ingred.ingred_flour()

    print(f"For one bread you need: {sugar_resilt:.2f} glass sugar, {oil_result:.2f} glass oil, {flour_result:.2f} glass flour\n") 
    
