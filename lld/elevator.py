# "Design an elevator control system for a building. The system should handle multiple elevators, 
# floor requests, and move elevators efficiently to service requests."
# https://www.youtube.com/watch?v=9UI4ikKP3Ws

# approach:
# requirements -> entities -> class design -> implementation -> extensibility


# entities:
# - elevator_system
#   - managing one or more elevators
#   - handling floor requests (floor, direction)
# - elevator
#   - current floor
#   _ direction (up, down, idle)
#   - request_queue

class ElevatorDirection(Enum):
    UP = "up"
    DOWN = "down"
    IDLE = "idle"

# pick up is from the outside the elevator
# destination is for the inside the elevator (no need for direction)
class RequestType(Enum):
    PICK_UP = "pick_up"
    PICK_DOWN = "pick_down"
    DESTINATION = "destination"
    
class ElevatorRequest:
    def __init__(self, floor:int, direction: Direction):
        self.floor =floor
        self.direction = direction
    
    def __str__(self) -> str:
        return f"Floor: {self.floor}, Direction: {self.direction}"

    def get_floor(self) -> int:
        return self.floor

    def get_direction(self) -> Direction:
        return self.direction

class Elevator:
    def __init__(self, id: int):
        self.id = id
        # basic queue for now: FIFO
        self.request_queue: list[ElevatorRequest] = []
        self.direction: Direction = Direction.IDLE
        self.current_floor: int = 0

    def add_request(self, request: ElevatorRequest) -> None:
        self.request_queue.append(request)

    # at every tick, determine the elevator's next move
    # possible moves based on the request queue:
    # if no requests, the elevator should remain idle
    # if there are requests:
    # - simple/naive: process the next quest in the queue
    # - optimal: go the next cloest stop in the direction of the request
    # - 
    def step(self) -> None:
        if request_queue is empty:
            self.direction = Direction.IDLE
            return
        
        target = self.request_queue[0]
        if target.direction == Direction.UP:
            self.direction = Direction.UP
        elif target.direction == Direction.DOWN:
            self.direction = Direction.DOWN
        
        if target.floor > self.current_floor:
            self.current_floor += 1
        elif target.floor < self.current_floor:
            self.current_floor -= 1
        
        # if arrived at the target floor, remove it from the queue
        if (target.floor == self.current_floor):
            self.request_queue.pop(0)


class ElevatorSystem:
    def __init__(self, elevators: list[Elevator]):
        self.elevators = elevators

    # figure out which elevator to send the request to
    # there are a few rules to consider when deciding which one is the best elevator:

    def request_elevator(self, floor: int, direction: Direction) -> Elevator:

        # edge cases:
        if floor < 0:
            raise ValueError("Floor cannot be negative")

        if direction not in [Direction.UP, Direction.DOWN]:
            raise ValueError("Invalid direction")

        # core logic
        request = ElevatorRequest(floor, direction)
        best_elevator = select_best_elevator(floor, direction)
        if best_elevator is None:
            raise ValueError("No elevator found for the request")

        best_elevator.add_request(request)
        return best_elevator


    # helper method to select the best elevator for the request
    # options (closest elevator, closest elevator in the direction, consider all the requests)
    def _select_best_elevator(self, floor: int, direction: Direction) -> Elevator:
        # implement the closest elevator in the direction

        
        best_elevator:Elevator = find_closestelevator_moving_towards_floor(floor, direction)
        if best_elevator is not None:
            return best_elevator

        best_elevator = find_closest_idle_elevator(floor, direction)
        if best_elevator is not None:
            return best_elevator

        return find_closest_elevator(floor, direction)


    def _find_closest_idle_elevator(self, requested_floor: int, requested_direction: Direction) -> Elevator:
        min_distance: int = sys.maxsize
        for elevator in self.elevators:
            if elevator.direction != Direction.IDLE:
                continue # continue to the next elevator

            distance = abs(elevator.current_floor - requested_floor)
            if distance < min_distance: # closer or not
                min_distance = distance
                best_elevator = elevator

        return best_elevator

    def _find_closest_elevator(self, requested_floor: int, requested_direction: Direction) -> Elevator:
        min_distance: int = sys.maxsize
        for elevator in self.elevators:
            distance = abs(elevator.current_floor - requested_floor)
            if distance < min_distance:
                min_distance = distance
                best_elevator = elevator

        return best_elevator


    def _find_closest_elevator_moving_towards_floor(self, requested_floor: int, requested_direction: Direction) -> Elevator:
        min_distance: int = sys.maxsize
        for elevator in self.elevators:
            if elevator.direction != requested_direction:
                continue # continue to the next elevator

            # if the elevator is moing the same direction, check to see it is is moving towards the floor or away from it
            # the logic will be based on the direction of the requested direction
            if direction == Direction.UP:
                if elevator.current_floor > requested_floor:  # already higher the requested floor
                    continue
            elif direction == Direction.DOWN:
                if elevator.current_floor < requested_floor: # already lower than the requested floor
                    continue

            distance = abs(elevator.current_floor - floor)
            if distance < min_distance:
                min_distance = distance
                best_elevator = elevator

        return best_elevator

    

    # simulate the elevator system by moving the elevators one tick at a time
    def step(self) -> None:
        for elevator in self.elevators:
            elevator.step()

    