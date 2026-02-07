from typing import Final, Self
from datetime import datetime

number: int = 5
decimal: float = 2.5
text: str = "Hello, World!"
boolean: bool = True

names: list[str] = ["John", "Jane", "Jim", "Jill"]
coordinates: tuple[int, int] = (1, 2)
unique_numbers: set[int] = {1,4, 9, 4}
data: dict[str, int] = {"apple": 1, "banana": 2, "cherry": 3}

VERSION: Final[str] = "1.0.0"
VERSION = "2.0.0"

class Car:
    def __init__(self, make: str, model: str, year: int, color: str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self) -> None:
        print(f"Driving {self.make} {self.model} {self.year}")

    def __str__(self) -> str:
        return f"Car(make={self.make}, model={self.model}, year={self.year}, color={self.color})"

    def __add__(self, other: Self) -> 'Car':        
        return Car(self.make + other.make, self.model + other.model, self.year + other.year, self.color + other.color)




def show_date() -> None: 
    print("Today's date is:")
    print(datetime.now())


print(number)
print(decimal)
print(text)
print(boolean)
print(names)
print(coordinates)
print(unique_numbers)
print(data) 
print(VERSION)

show_date()
show_date()

print ("-" * 20 )
volvo: Car  = Car("Volvo", "XC90", 2024, "Red")
volvo.drive()  

print ("-" * 20 )
bmw: Car = Car("BMW", "X5", 2025, "Blue")
bmw.drive() 

print(bmw.make)
bmw.make = "Mercedes"
print(bmw.make)

print(bmw)

print ("volvo + bmw --------------------------------"  )
print(volvo + bmw)