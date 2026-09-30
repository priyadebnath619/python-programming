month = input("Enter month name: ").lower()

if month in ["march", "april", "may"]:
    print("Spring")
elif month in ["june", "july", "august"]:
    print("Summer")
elif month in ["september", "october", "november"]:
    print("Autumn")
elif month in ["december", "january", "february"]:
    print("Winter")
else:
    print("Invalid month")