data: list[tuple[str, int]] = [("apple", 1), ("banana", 2), ("cherry", 3)]

data_dict: dict[str, int] = {k.upper():v*10 for k,v in data}
 
print(data_dict)