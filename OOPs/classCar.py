class Car:

    wheels = 4 #class variable

    def __init__ (self, make, model, year, color):


        self.make = make    # Instance variable
        self.model = model  # Instance variable
        self.year = year    # Instance variable
        self.color= color   # Instance variable
        print(f"Company name: {make} model: {model} year: {year} and color:{color} ")
