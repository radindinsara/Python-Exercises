names = set()

print("Enter names (press Enter with empty input to finish):")

while True:
    name = input().strip()

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nAll entered names:")
for name in names:
    print(name)