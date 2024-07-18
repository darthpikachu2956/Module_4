class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Name: {self.name}, number of floors: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            raise ValueError("Can only compare to another House object or an integer.")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            raise ValueError("Can only compare to another House object or an integer.")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            raise ValueError("Can only compare to another House object or an integer.")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            raise ValueError("Can only compare to another House object or an integer.")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            raise ValueError("Can only compare to another House object or an integer.")

    def __add__(self, value):
        if isinstance(value, int):
            new_floors = self.number_of_floors + value
            return House(self.name, new_floors)
        else:
            raise ValueError("Can only add an integer value to number of floors.")

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            total_floors = self.number_of_floors + value
            return House(self.name, total_floors)


first_house = House('West Pines', 16)
second_house = House('Grove Street', 2)
print(first_house)
print(second_house)
print(first_house == second_house)

second_house = second_house + 14
print(second_house)
print(first_house == second_house)

first_house += 10
print(first_house)

second_house = 10 + second_house
print(second_house)

print(first_house > second_house)
print(first_house >= second_house)
print(first_house < second_house)
print(first_house <= second_house)
print(first_house != second_house)
