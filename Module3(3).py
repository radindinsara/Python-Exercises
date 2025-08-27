gender = input("Enter biological gender (male/female): ").lower()
hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

if gender == "male" and 134 <= hemoglobin_value <= 167 :
    print("Your hemoglobin is normal.")
elif gender == "female" and 117 <= hemoglobin_value <= 155  :
    print("Your hemoglobin is normal.")
elif gender == "male" and hemoglobin_value < 134:
    print("Your hemoglobin is low.")
elif gender == "male" and hemoglobin_value > 167:
    print("Your hemoglobin is high.")
elif gender == "female" and hemoglobin_value < 117 :
    print("Your hemoglobin is low.")
elif gender == "female" and hemoglobin_value > 155:
    print("Your hemoglobin is high.")
else:
    print("Invalid gender.")
