print("*" * 20 + " LIST " + "*" * 20)

list = ['larry', 'curly', 'moe']

list.append("hien")

print(f"list after appending: {list}")

list.insert(0, "hien")

print(f"list after inserting at 0: {list}")

list.extend(['xxx', 'yyy'])

print(f"list after extending at 0: {list}")

print("index: " + str(list.index('hien')))

list.remove('curly')

print(f"list after remove curly: {list}")

list.pop(1)

print(f"list after pop(1): {list}")