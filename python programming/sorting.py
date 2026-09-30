items = input("Enter items separated by spaces: ").split()

if all(item.replace('.', '', 1).isdigit() for item in items):
    
    items = [float(item) if '.' in item else int(item) for item in items]


sorted_items = sorted(items)


print("Sorted list:", sorted_items)