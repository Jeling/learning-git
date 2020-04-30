import os
clear = lambda: os.system('cls')
clear()

# Zadanie 2
print("Zadanie 2")
divisible_by_five = []
powers = []
for number in range(1, 101):
    if number % 5 == 0:
     divisible_by_five.append(number)
for number in divisible_by_five:
    powers.append(number ** 3)
print(f"""Liczby podzielne przez 5: {divisible_by_five}""")
print(f"""Potęgi: {powers}
""")