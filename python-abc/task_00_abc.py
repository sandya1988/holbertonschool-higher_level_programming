#!/usr/bin/python3from abc import ABC, abstractmethodclass Animal(ABC):    """Abstract base class representing an Animal."""    @abstractmethod    def sound(self):        """Abstract method to be implemented by subclasses.        Returns:            str: The sound made by the animal.        """        passclass Dog(Animal):    """Class representing a Dog, subclass of Animal."""    def sound(self):        """Returns the sound made by the dog.        Returns:            str: The sound 'Bark'.        """        return "Bark"class Cat(Animal):    """Class representing a Cat, subclass of Animal."""    def sound(self):        """Returns the sound made by the cat.        Returns:            str: The sound 'Meow'.        """        return "Meow"
