from datetime import datetime

"""
Robots class - using dunder methods aka magic methods

These methods let you make your custom classes behave like built-in types. 

 - __str__: Defines string representation for print() and str()
 - __repr__: Defines "official" string representation, used in the console
 - __add__
 - __sub__
 - __mul__
 - __div__
 - __mod__
 - __pow__
 - __len__
"""

class Robot:
    def __init__(self, name: str, build_year: int):
        print("Initializing Robot\n")
        self.name = name
        self.build_year = build_year

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case "short":
                return f"{self.name} ({self.build_year})"
            case "long":
                return f"Robot(name={self.name}, build_year={self.build_year})"
            case "caps":
                return f"{self.name.upper()} ({self.build_year})"
            case _:
                return self.__str__()

    def introduce(self) -> None:
        print(f"Hello, my name is '{self.name} and I was built in {self.build_year}")

    def get_age(self   ) -> int:
        return datetime.now().year - self.build_year

    @classmethod
    def update_year(cls, year: int) -> None:
        print(f"Updating year to {year}")
        cls.build_year = year

    @classmethod
    def from_dict(cls, robot_info: dict) -> 'Robot':
        return cls(robot_info["name"], robot_info["build_year"])

class ChefRobot(Robot):
    def __init__(self, name: str, build_year: int, speciality: str):
        super().__init__(name, build_year)
        self.speciality = speciality

    def introduce(self) -> None:
        super().introduce()
        print(f"My speciality is {self.speciality}")

def main() -> None:
    print("========== Starting main ==========")
    bot1 = Robot("Robot1", 2020)
    bot2 = Robot("Robot2", 2021)

    print("--------------------------------")
    bot1.introduce()
    print(f"{bot1.name} is {bot1.get_age()} years old")
    bot1.update_year(2026)
    print(f"{bot1.name} is {bot1.get_age()} years old")

    print("--------------------------------")
    bot2.introduce()
    print(f"{bot2.name} is {bot2.get_age()} years old")


    print("--------------------------------")
    bot2 = Robot.from_dict({"name": "Robot3", "build_year": 1990})
    bot2.introduce()

    print("--------------------------------")
    italianChef = ChefRobot("ChefRobot1", 2020, "Italian")
    italianChef.introduce()

    print("------------ Formatting --------------------")
    print(f"short: {bot1:short}")
    print(f"long: {bot1:long}")
    print(f"caps: {bot1:caps}")
    

# when running the file directly, the code below will be executed
# when importing the file, the code below will not be executed
if __name__ == "__main__":
    main()