# Python class
from dataclasses import dataclass
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

    def __lt__(self, other) -> bool:
        return self.cash < other.cash


i1 = Investor1("John", 25, 10000)
i2 = Investor1("Anna", 30, 15000)
i3 = Investor1("Bob", 70, 800000)
i4 = Investor1("John", 25, 9000)
print(i1)
print(i1 == i4)  # compare name
print(i1 > i4)  # compare cash amount


# Python Data classes let you access inbuilt functionality


@ dataclass(order=True)
class Investor2:
    name: str
    age: int
    cash: float = field(repr=False, default=0)


i5 = Investor2("John", 25, 10000)
i6 = Investor2("Anna", 30)
i7 = Investor2("John", 25, 9000)
print(i5)
print(i6)
print(i5 == i7)  # compare classes
print(i5 > i7)  # compare cash amount
