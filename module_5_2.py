class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Name: {self.name}, number of floors: {self.number_of_floors}'

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('There is not such a floor in this house.')
        else:
            for i in range(1, new_floor + 1):
                print(i)


first_house = House('West Pines', 16)
second_house = House('Grove Street', 2)
print(first_house)
print(second_house)
print(len(first_house))
print(len(second_house))
