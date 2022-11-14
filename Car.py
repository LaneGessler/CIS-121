#class car

class car:

    def __init__(self,number_of_wheels,engine,model,year):
    #when car called this function will be run 
        self.number_of_wheels = number_of_wheels
        self.engine = engine
        self.model = model
        self.year = year
        #self refers to the variables in our class
        #needs self every time

    def __str__(self):
        print("===Car Info===")
        print(f"wheels: {self.number_of_wheels}")
        print(f"engine: {self.engine}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        return ''
        #needs this return statement with nothing in it so it doesnt make an error

    def changeYear(self,new_year):
        self.year = new_year

    def changeEngine(self,new_engine):
        self.engine = new_engine