class Microwave:
    def __init__(self, brand:str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.is_on = False

    # for users
    def __str__(self) -> str:
        return f"brand={self.brand}, power_rating={self.power_rating}, is_on={self.is_on}"

    # for developers    
    def __repr__(self) -> str:
        return f"Microwave(brand={self.brand}, power_rating={self.power_rating}, is_on={self.is_on})"


    def is_powered_on(self) -> bool:
        return self.is_on

    def turn_on(self) -> None:
        if self.is_on:
            print("Microwave is already on")
        else:
            self.is_on = True
            print("Microwave is now on")

    def turn_off(self) -> None:
        if self.is_on == False:
            print("Microwave is already off")
        else:
            self.is_on = False
            print("Microwave is now off")

    def run(self, seconds: int) -> None:
        # only run when it is already on
        if self.is_on:
            print(f"Running {self.brand} for {seconds} seconds")
        else:
            print("Microwave is not on, please turn it on first")



smeg: Microwave = Microwave("Smeg", "B")
print(smeg)
print(f"Brand: {smeg.brand}")
print(f"Power Rating: {smeg.power_rating}")

smeg.turn_on()
print(f"Is on: {smeg.is_powered_on()}")
smeg.turn_on()
smeg.turn_off()
print(f"Is on: {smeg.is_powered_on()}")
smeg.run(10)

smeg.turn_on()
smeg.run(10)

print(smeg)
print(repr(smeg))
"""
bosch: Microwave = Microwave("Bosch", "A")
print(bosch)
print(f"Brand: {bosch.brand}")
print(f"Power Rating: {bosch.power_rating}")
"""