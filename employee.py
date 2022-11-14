#class called employee. hourly_wage,hours_per_week, position, name
#method that calculates yearly salary

class employee:
    def __init__(self,hourly_wage,hours_per_week, position, name):
        self.hourly_wage = hourly_wage
        self.hours_per_week = hours_per_week
        self.position = position
        self.name = name

    def __str__(self):
        
        print("===Employee info====")
        print(f"Name: {self.name}")
        print(f"Hours worked: {self.hours_per_week}")
        print(f"Position: {self.position}")
        print(f"Hourly Wage: {self.hourly_wage}")
        print(f"Income: {self.income()}")
        return ''

    def income(self):
        #self.income = self.hours_per_week*self.hourly_wage*(365/7)
        return self.hours_per_week*self.hourly_wage*(365/7)


    #change value functions
    
    def changeHourly_wage(self,new_hourly_wage):
        self.hourly_wage = new_hourly_wage
    def changePosition(self,new_position):
        self.position = new_position
    def changeHours_per_week(self,new_hours_per_week):
        self.hours_per_week = new_hours_per_week
    def changeName(self,new_name):
        self.name = new_name