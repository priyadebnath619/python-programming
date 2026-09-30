contacts = []

contacts.append(["Priya", 6033512264])
contacts.append(["Raj", 6573267889])

print(contacts)

name = input("Search: ")

for c in contacts:
    if c[0] == name:
        print(c[1])