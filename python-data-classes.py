# Python class
from dataclasses import dataclass, field


class Investor1:

    def __init__(self, name: str, age: int, cash: float) -> None:
        self.name = name
        self.age = age
        self.cash = cash

    # We need to manually add desired functionality

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

    def __eq__(self, other) -> bool:
        return self.name == other.name


i1 = Investor1("John", 25, 10000)
i2 = Investor1("Anna", 30, 15000)
i3 = Investor1("Bob", 70, 800000)
i4 = Investor1("John", 25, 10000)  # same as i1
print(i1)
print(i1 == i4)


# Python Data classes let you access inbuilt functionality
# @ dataclass
# class Investor2:
