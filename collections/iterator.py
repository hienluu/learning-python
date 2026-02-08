#map 

#map iterating through an iterator
string_list: list[str] = ['apple', 'banana', 'cherry', 'pear']

# first arg is the function to apply to each item in the iterator
# second arg is the iterator to apply the function to
# convert the iterator to a list
length_list: list[int] = list(map(len, string_list))

print("==== Map Iterating Through an Iterator ====")
print(length_list, end="\n\n")


# filter function
# first arg is the function to apply to each item in the iterator
# second arg is the iterator to apply the function to
# convert the iterator to a list to print the result    
filtered_list: list[str] = list(filter(lambda x: len(x) > 4, string_list))

print("==== Filter Function ====")
print(filtered_list)


# enumerate function

print("==== Enumerate Function ====\n")
print("--- without enumerate ---")
# w/o using enumerate
for idx in range(len(string_list)):
    val: str = string_list[idx]
    print(f'{idx +1}: {val}')

# using enumerate
print("\n--- with enumerate ---")
for idx, value in enumerate(string_list):
    print(f'{idx+1}: {value}')

print("\n--- enumerate as a list of tuples ---")
print(list(enumerate(string_list)))


print("\n==== Zip Function ====\n")
# zip automatically stops when the shortest list is exhausted

prices: list[float] = [10.0, 20.0, 30.0, 40.0]
quantities: list[int] = [20, 11, 4]

print("--- zip as a list of tuples ---")
print(list(zip(string_list, prices)))

print("\n---iterating though the zip of string_list and prices lists ---")
for item, price in zip(string_list, prices):
    print(f'{item}: {price}')

print("\n---iterating though the zip of string_list, prices, quantities lists ---")
# notice the output contains only the common elements of the three lists
for item, price, quantity in zip(string_list, prices, quantities):
    print(f'{item}: {price}: {quantity}')

# resource: https://www.youtube.com/watch?v=kGcUtckifXc