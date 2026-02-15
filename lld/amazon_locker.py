# https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/amazon-locker
# https://youtu.be/s6nGkoGJhXk (low level design)

# Design a locker system like Amazon Locker where delivery drivers can 
# deposit packages and customers can pick them up using a code.

# requirements -> entities -> class design -> implementation -> extensibility
# entities (state, behavior)
# implementation: seudo code or exact
# extensibility: how the desing could evolve w/ additiona capability

###### requirements ######
# questions to asks 3 categories: 
#     (main capabilities, error handling, scope boundary (in/out))
# main capabilities: 
# - compartment sizes
# - how do customers get the code
# rules & completions
#
# error handling
# - unique access code
# - how long do the codes last
# - what if all comparments are full of a given size?

###### entities ######
# needed objects and how they interact w/ each other
# - look for the nouns in the requirements
# - package (is it in scope or out)
# - comparments, 
# - locker
# - access code
# scope boundary (in/out)

from enum import Enum
from datetime import datetime, timedelta
import uuid

class CompartmentState(Enum):
    EMPTY = "empty"
    OCCUPIED = "occupied"
    RESERVED = "reserved"
    OUT_OF_SERVICE = "out of service"

class CompartmentSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class Compartment:
    def __init__(self, size: CompartmentSize):
        self.size = size
        self.state = CompartmentState.EMPTY

    def __str__(self) -> str:
        return f"Compartment(size={self.size}, state={self.state})"
    def isOccupied(self) -> bool:
        return self.state == CompartmentState.OCCUPIED

    def markOccupied(self) -> None:
        self.state = CompartmentState.OCCUPIED

    def markFree(self) -> None:
        self.state = CompartmentState.EMPTY

    def getSize(self) -> CompartmentSize:
        return self.size

    def open(self) -> None:
        ...


class AccessCode:
    def __init__(self, code: str, expiration_date: datetime, compartment: Compartment):
        self.code = code
        self.expiration_date = expiration_date
        self.comparment = compartment

    def getCompartment(self) -> Compartment:
        return self.comparment

    def getCode(self) -> str:
        return self.code

    def isExpired(self) -> bool:
        # expiration date represents a future date
        # if the current date is greater than the expiration date, the code is expired
        return datetime.now() >= self.expiration_date


class Locker: 
    # either can specify # of compartments with various sizes or
    # let caller build the list of compartments and let the locker manage them
    # good idea to separate out the compartment build logic from the locker class
    def __init__(self, compartments: list[Compartment]):
        self.comparments = compartments
        self.access_token_mapping:dict[str, AccessCode] = {}


    def _getAvailableCompartment(self, requested_size: CompartmentSize) -> Compartment:
        sizesInOrder = [CompartmentSize.SMALL, CompartmentSize.MEDIUM, CompartmentSize.LARGE]
        # start from this size and go up
        startIndex = sizesInOrder.index(requested_size)
        for i in range(startIndex, len(sizesInOrder)):
            size = sizesInOrder[i]
            for compartment in self.comparments:
                if compartment.getSize() == size and not compartment.isOccupied():
                    return compartment
        return None

    def _generateAccessCode(self, compartment: Compartment) -> AccessCode:
        # generate a random access code
        access_code_string = str(uuid.uuid4())
        print(f"Generated access code: {access_code_string}")
        access_code = AccessCode(access_code_string, datetime.now() + timedelta(days=10), compartment)
        return access_code

    def _clearDeposit(self, access_code: AccessCode) -> None:
        compartment = access_code.getCompartment()
        compartment.markFree()
        self.access_token_mapping.pop(access_code.getCode(), None)

    # return the access code for the compartment
    def depositPackage(self, size: CompartmentSize) -> str:
        print(f"Depositing package of size: {size}")
        # find the first available compartment of the given size
        compartment = self._getAvailableCompartment(size)
        print(f"Available compartment: {compartment}")
        if compartment is None:
            raise Exception("No available compartment of the given size")

        print(f"Marking compartment as occupied: {compartment.getSize()}")
        # mark the compartment as occupied
        compartment.open()
        compartment.markOccupied()

        # generate a new access code
        access_code = self._generateAccessCode(compartment)
        print(f"Access code in depositPackage: {access_code.getCode()}")
        self.access_token_mapping[access_code.getCode()] = access_code
        return access_code.getCode()

    # return None because it just open the right compartment for customer to pick it up
    def pickupPackage(self, access_code_str: str) -> None:
        print(f"Picking up package with access code: {access_code_str}")
        if access_code_str is None or access_code_str.strip() == "":
            raise Exception("Invalid access code string")
        
        # look up the access code from the mapping
        access_code = self.access_token_mapping[access_code_str]
        if not access_code:
            raise Exception("No compartment found for the given access code")

        if access_code.isExpired():
            raise Exception("Access code has expired")

        compartment = access_code.getCompartment()
        compartment.open()
        self._clearDeposit(access_code)
       
       

    def openExpiredCompartments(self) -> None:
        count:int = 0
        for access_code in self.access_token_mapping.values():
            if access_code.isExpired():
                count += 1
                compartment = access_code.getCompartment()
                compartment.open()
                compartment.markFree()
                self.access_token_mapping.pop(access_code.getCode(), None)

        print(f"Found and opened {count} expired compartments")

def main(): 
    print("===== Amazon Locker System =====")
    compartments = [Compartment(CompartmentSize.SMALL), Compartment(CompartmentSize.MEDIUM), Compartment(CompartmentSize.LARGE)]
    locker = Locker(compartments)

    print("\n --------- Depositing a package ---------")
    print("Depositing package of size SMALL")
    access_code = locker.depositPackage(CompartmentSize.SMALL)
    print(f"Access code: {access_code}")
   
    print("\n --------- Picking up package with invalid access code ---------")
    try:
        locker.pickupPackage("abc")
    except Exception as e:
        print(f"Expecting this error: Error: Invalid access code string, but got: {e}")


    print("\n --------- Picking up package ---------")
    locker.pickupPackage(access_code)

    print("\n --------- Picking up package again ---------")
    try:
        locker.pickupPackage(access_code)
    except Exception as e:
        print(f"Expecting this error: Error: No compartment found for the given access code, but got: {e}")

    print("\n --------- Opening expired compartments ---------")
    locker.openExpiredCompartments()


if __name__ == "__main__":
    main()