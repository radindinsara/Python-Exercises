import random

code_1 = "".join(str(random.randint(0, 9)) for _ in range(3))
code_2 = "".join(str(random.randint(1, 6)) for _ in range(4))

print("3-digit code:", code_1)
print("4-digit code:", code_2)