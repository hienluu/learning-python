ages: list[int] = [20, 21, 22, 23, 24, 25]

adult_ages: list[int] = []

adult_page_min = 19

for age in ages:
    if age >= adult_page_min:
        adult_ages.append(age)

print("adult ages:", adult_ages)


# list comprehension starts with the result, then the for loop, 
# then the condition
adult_ages2: list[int] = [age for age in ages if age >= adult_page_min]
print("adult ages2:", adult_ages2)

# list comprehension with a map function
adult_ages3: list[int] = [age + 1 for age in ages if age >= adult_page_min]
print("adult ages3:", adult_ages3)

# list comprehension with a map function and a condition
adult_ages4: list[int] = [age + 1 for age in ages if age >= adult_page_min]
print("adult ages4:", adult_ages4)


