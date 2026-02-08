set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}

# union
print("==== | operator: Union & remove duplicates ====")
print(set_a | set_b)

# intersection
print("==== & operator:Intersection & keep only common elements ====")
print(set_a & set_b)

# difference
print("==== - operator:Difference & keep only elements in set_a but not in set_b ====")
print(set_a - set_b)

# symmetric difference
print("==== ^ operator: Symmetric difference & keep only elements in set_a or set_b but not in both ====")
print(set_a ^ set_b)