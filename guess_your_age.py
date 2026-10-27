birth_year = input("What year were your born? ")

if len(birth_year) < 4:
    print("Please enter a valid year")
else:
    present_year = 2026
    age = present_year - int(birth_year)
    print(f"Oh! You are {age} years old")

