class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('There is not such a floor in this house.')
        else:
            for i in range(1, new_floor + 1):
                print(i)


first_house = House('West Pines', 16)
second_house = House('Grove Street', 2)
first_house.go_to(7)
second_house.go_to(5)
first_house.go_to(0)
second_house.go_to(2)

print(f'We have built new houses: {first_house.name} and {second_house.name}!')
