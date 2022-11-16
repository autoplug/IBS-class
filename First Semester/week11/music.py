from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    # An abstract method is a method that has a declaration but does not have an implementation.
    @abstractmethod
    def play(self):
        pass


class StringedInstrument(Instrument):

    def __init__(self, name, numberOfStrings):
        super().__init__(name)
        self.numberOfStrings = numberOfStrings
    # overriding abstract method

    def play(self):
        self.sound()

    def sound(self):
        pass


class ElectricGuitar(StringedInstrument):
    def __init__(self):
        pass


guitar = ElectricGuitar()
