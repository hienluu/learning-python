from typing import Dict, List, Optional, Set
from abc import ABC, abstractmethod
from dataclasses import dataclass
import time
import uuid
from enum import Enum


class VehicleType(Enum):
    CAR = 2,
    MOTOCYCLE = 1,
    LARGE = 3

class SpotType(Enum):
    CAR = 2,
    MOTOCYCLE = 1,
    LARGE = 3



class Ticket:
    def __init__(self,  spotId: str, vehicleType: VehicleType, entry_time: int):
        self.id = str(uuid.uuid4())
        self.spotId = spotId
        self.vehicleType = vehicleType
        self.entry_time = entry_time

    def get_id(self) -> str:
        return self.id
    
    def get_spot_id(self) -> str:
        return self.spotId
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicleType
    
    def get_entry_time(self) -> int:
        return self.entry_time

class ParkingSpot:
    def __init__(self, spotId: str, spotType: SpotType):
        self.spotId = spotId
        self.spotType = spotType
        

    def get_spot_id(self) -> str:
        return self.spotId
    
    def get_spot_type(self) -> SpotType:
        return self.spotType
    


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, ticket: Ticket, exitTime: int) -> float:
        pass


class ParkingLot:
    def __init__(self, spots: List[ParkingSpot], hourly_rate_cents: int):
        self._spots = spots
        self._hourly_rate_cents = hourly_rate_cents
        self._occupied_spot_ids: Set[str] = set()
        self._active_tickets: Dict[str, Ticket]

    def enter(self, vehicleType: VehicleType) -> Optional[Ticket]:
        # find an available spot for the vehicle type
        spot = self._find_available_spot(vehicleType)
        if spot is None:
            raise Exception("Parking lot is full for this vehicle type")
        
        # book keeping - add to occupied spots 
        # this set is used to quickly check for available spots without having to iterate through the list of spots each time
        self._occupied_spot_ids.add(spot.get_spot_id())

        # create a ticket
        ticket_id = str(uuid.uuid4())
        entry_time = int(time.time() * 1000) # current time in milliseconds
        ticket = Ticket(spot.get_spot_id(), vehicleType, entry_time)

        # add to active tickets for tracking
        self._active_tickets[ticket_id] = ticket
        return ticket

    def exit(self, ticket_id: str):
        if ticket_id is None or ticket_id == "":
            raise ValueError("Invalid ticket ID")
        
        ticket = self._active_tickets.get(ticket_id)
        if ticket is None:
            raise ValueError("Ticket not found")
        
        exit_time = int(time.time() * 1000) # current time in milliseconds
        fee = self._compute_fee(ticket.entry_time(), exit_time)

        
        self._occupied_spot_ids.discard(ticket.get_spot_id())
        del self._active_tickets[ticket_id]


    def _map_vehicle_to_spot(self, vehicleType: VehicleType) -> Optional[ParkingSpot]:
        if vehicleType == VehicleType.MOTOCYCLE:
            return SpotType.MOTOCYCLE
        elif vehicleType == VehicleType.CAR:
            return SpotType.CAR
        elif vehicleType == VehicleType.LARGE:
            return SpotType.LARGE
        
        raise ValueError
    
    def _find_available_spot(self, vehicleType: VehicleType) -> Optional[ParkingSpot]:
        required_spot_type = self._map_vehicle_to_spot(vehicleType)
        for spot in self._spots:
            if spot.get_spot_type() == required_spot_type and spot.get_spot_id() not in self.occupied_spot_ids:
                return spot
        return None
    

    def _compute_fee(self, entry_time: int, exit_time: int) -> int:
        duration_ms = exit_time - entry_time
        duration_hours = duration_ms / (1000 * 60 * 60) # convert milliseconds to hours

        # round up to the next hour if there's any remaining time
        if duration_ms % (1000 * 60 * 60) > 0:
            duration_hours += 1 

        fee_cents = int(duration_hours * self._hourly_rate_cents)
        return fee_cents