zander_length = float(input("Enter the length of the zander in centimeters: "))

size_limit = 42.0

if zander_length < size_limit:
    missing = size_limit - zander_length
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")