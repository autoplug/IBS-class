class Resident:
    def __init__(self, name):
        self.name = name


class Flat:
    residents = []
    capacity = 0

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} flat has {self.capacity} residents."

    def add(self, resident):
        if not isinstance(resident, Resident):
            raise ValueError
        if self.capacity <= len(self.residents):
            print("The flat is full.")
            return
        self.residents.append(resident)

    def remove(self, name):
        index = -1
        for resident_index in range(len(self.residents)):
            if self.residents[resident_index].name == name:
                index = resident_index
        if index >= 0:
            self.residents.pop(index)
            self.capacity -= 1


flat1 = Flat('FLT1', 3)
jane = Resident('Jane')
john = Resident('John')
kate = Resident('Kate')
kyle = Resident('Kyle')
flat1.add(jane)
flat1.add(john)
flat1.add(kate)
print(flat1)  # should print: FLT1 flat has 3 residents.
flat1.add(kyle)  # should print: The flat is full.
print(flat1)  # should print: FLT1 flat has 3 residents.
flat1.remove('Jane')
print(flat1)  # should print: FLT1 flat has 2 residents.
flat1.remove('Jane')
print(flat1)  # should print: FLT1 flat has 2 residents.
