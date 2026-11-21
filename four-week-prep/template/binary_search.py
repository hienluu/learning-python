
# Searching array indices where the target might not exist? 
# Use lo = 0, hi = len(arr) (exclusive).
def binary_search(lo:int, hi:int, condition: callable) -> int:
    max_limit:int = hi
    while lo < hi:
        # mid point is the average of the left and right pointers, rounded down to the nearest integer
        # is the floor division operator. It divides two numbers and rounds the result down to the nearest whole integer, 
        # whereas a single / performs true (floating-point) division
        mid = (lo + hi) // 2
        if condition(mid):
            # moving to the left half by updating the right pointer
            hi = mid
        else:
            # moving to the right half by updating the left pointer
            lo = mid + 1
    # loop only terminates when lo == hi, 
    # meaning both pointers converge onto the exact same index. At that point, returning lo or hi yields the identical value
    return lo if lo < max_limit else -1


if __name__ == "__main__":
    # Example usage of binary_search function
    arr = [1, 3, 5, 7, 9]    
    target = 20
    print(f"Array: {arr} Target: {target}")
    index = binary_search(0, len(arr), lambda x: arr[x] >= target)
    print(f"Index of {target} in array: {index}")  # Output: Index of 5 in array: 2