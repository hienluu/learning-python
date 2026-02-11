from enum import Enum
from typing import Optional


class SpotSize(Enum):
    REGULAR = "regular"
    MOTORCYCLE = "motorcycle"
    LARGE = "large"


def get_spot_size(size: str) -> Optional[SpotSize]:
    try:
        return SpotSize(size)
    except ValueError:
        return None

print("==== Enum Example ====")
print(SpotSize.REGULAR)
print(SpotSize.MOTORCYCLE)
print(SpotSize.LARGE)

print("\n==== Get Spot Size ====")
print(get_spot_size("regular"))
print(get_spot_size("motorcycle"))
print(get_spot_size("large"))