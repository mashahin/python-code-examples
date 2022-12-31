# Python class
class Investor1:

    def __init__(self, name: str, age: int, cash: float) -> None:
        self.name = name
        self.age = age
        self.cash = cash

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"


i1 = Investor1("John", 30, 12000)
print(i1)  # It prints the object <__main__.Investor1 object at 0x0000018A1E675DF0>
