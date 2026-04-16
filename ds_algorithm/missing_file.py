"""
Missing Filename Detection Problem


Problem Statement:
You have a Database that stores unix timestamps as keys, and a list of filenames that were saved at that timestamp.
All of the filenames are unique.


The data from this Database was copied into another one, but one filename did not make it! 
Your job is to find the missing filename.


The Database class is an interface - each operation is really fast:
- int count_filenames(int start_time, int end_time): Counts filenames in timerange, inclusive of endpoints (O(1))
- get_filenames(self, timestamp: int) -> list[str]: Gets all filenames at a timestamp (O(n) where n = number of files at that timestamp)


You can interact with each Database ONLY using these two methods.


Part 1: Find one missing Filename
Write a method:
def find_missing_data(Database db, Database db_copy, int start_time, int end_time) -> str
which should search the two Databases for a missing filename in [start_time, end_time] inclusive and return it.


Part 2: Find All missing filenames
Now there can be any number of missing filenames. Write a method:
def find_all_missing_filenames(db: Database, db_copy: Database, start_time: int, end_time: int) -> List[str]:
which can return all missing filenames in [start_time, end_time], in any order.
"""


from typing import List


class Database:
    """
    Database interface - treat as a black box with really fast operations:
    - count_filenames: O(1) - counts filenames in time range
    - get_filenames: O(n) where n = number of files at that specific timestamp
    """
    def __init__(self, data_dict: dict):
        self._data = data_dict
    
    def count_filenames(self, start_time: int, end_time: int) -> int:
        count = 0
        for timestamp in range(start_time, end_time + 1):
            if timestamp in self._data:
                count += len(self._data[timestamp])
        return count
    
    def get_filenames(self, timestamp: int) -> list[str]:
        return self._data.get(timestamp, [])


def has_file_count_diff(db: Database, db_copy: Database, start_time: int, end_time: int) -> bool:
    count1 = db.count_filenames(start_time=start_time, end_time=end_time)
    count2 = db_copy.count_filenames(start_time=start_time, end_time=end_time)
    return count1 != count2

def find_missing_data(db: Database, db_copy: Database, start_time: int, end_time: int) -> str:
    print(f" start_time: {start_time}, end_time: {end_time}")
    """
    Find exactly one missing filename in the time range [start_time, end_time].
    
    Args:
        db: Original database
        db_copy: Copy database with one missing filename
        start_time: Start of time range (inclusive)
        end_time: End of time range (inclusive)
    
    Returns:
        The missing filename as a string
    """
    # TODO: Implement this function
    # determine which half has a file count difference
    if start_time == end_time:
        db1_file_names = db.get_filenames(start_time)
        db2_file_names = db_copy.get_filenames(start_time)
        
        db2_file_name_set = set(db2_file_names)
        print(f"len1: {len(db1_file_names)}, len2: {len(db2_file_names)}")
        print(f"list1: {db1_file_names}, list2: {db2_file_names}")

        for file_name in db1_file_names:
            if file_name not in db2_file_name_set:
                return file_name


    mid_point = int((start_time + end_time) / 2)
    if has_file_count_diff(db, db_copy, start_time, mid_point):
        return find_missing_data(db, db_copy, start_time, mid_point)
    else:
        return find_missing_data(db, db_copy, mid_point+1, end_time)


# this is a divide and conquer approach, 
# we check if there is a file count difference in the left half of the time range, 
# if there is then we know the missing file is in that half so we recurse on that half, otherwise we recurse on the right half. 
# We continue this process until we narrow it down to a single timestamp, 
# at which point we can directly compare the filenames at that timestamp to find the missing one.
def find_all_missing_filenames(db: Database, db_copy: Database, start_time: int, end_time: int) -> List[str]:
    """
    Find all missing filenames in the time range [start_time, end_time].
    
    Args:
        db: Original database
        db_copy: Copy database with missing filename(s)
        start_time: Start of time range (inclusive)
        end_time: End of time range (inclusive)
    
    Returns:
        List of all missing filenames (order doesn't matter)
    """
    # Step 1: Check if there is a discrepancy in this range
    original_count = db.count_filenames(start_time, end_time)
    copy_count = db_copy.count_filenames(start_time, end_time)
    
    # base case If counts match, no files are missing in this range. Prune the search.
    if original_count == copy_count:
        return []
    
    # Step 2: Base case - we've narrowed it down to a single unix timestamp
    if start_time == end_time:
        files_original = set(db.get_filenames(start_time))
        files_copy = set(db_copy.get_filenames(start_time))
        # Return the filenames present in original but not in copy
        return list(files_original - files_copy)
    
    # Step 3: Divide and Conquer
    mid_time = (start_time + end_time) // 2
    
    # Recurse on the left and right halves
    missing_left = find_all_missing_filenames(db, db_copy, start_time, mid_time)
    missing_right = find_all_missing_filenames(db, db_copy, mid_time + 1, end_time)
    
    return missing_left + missing_right
    



if __name__ == '__main__':
    db_data = {
        2: ["file1", "file2"],
        4: ["file3"],
        5: ["file4", "file5", "file6"],
        6: ["file7", "file8", "file9", "file10"],
        7: ["file11"],
        10: ["file12"]
    }
    
    # Copy database data with missing file
    db_copy_data = {
        2: ["file1", "file2"],
        4: ["file3"],
        5: ["file4", "file5", "file6"],
        6: ["file7", "file8", "file9", "file10"],
        7: [],  # Empty list instead of ["file11"]
        10: ["file12"]
    }
    
    db = Database(db_data)
    db_copy = Database(db_copy_data)
    
    # Test Part 1 - Should print "file11"
    print("======== Finding one missing filename...\n")
    result = find_missing_data(db, db_copy, 2, 10)
    print(f"Missing filename: {result}")
    
    # Test Part 2 - Should print ["file11"]
    print("========Finding all missing filenames...\n")
    all_missing = find_all_missing_filenames(db, db_copy, 2, 10)
    print(f"All missing filenames: {all_missing}")
