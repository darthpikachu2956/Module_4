class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(*args)
        return super(House, cls).__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        if self.name in House.houses_history:
            House.houses_history.remove(self.name)
            print(f'{self.name} is demolished but it will be saved in the history.')

    def __str__(self):
        return f'Name: {self.name}, number of floors: {self.number_of_floors}'


first_house = House('West Pines', number_of_floors=16)
print(House.houses_history)
second_house = House('Grove Street', number_of_floors=2)
print(House.houses_history)
third_house = House('Kunstkamera', number_of_floors=11)
print(House.houses_history)

del second_house
print(House.houses_history)
del third_house
print(House.houses_history)
