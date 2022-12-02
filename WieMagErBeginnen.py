import random

spelers = int(input("hoeveel spelers doen ermee? "))

for i in range(spelers):

    inputs = []
while True:
    inp = input("naam/KLAAR: ")
    if inp == "KLAAR":
        break
    inputs.append(inp)
    
print(inputs)

print("de gene die mag beginnen is... ")

print(random.choice(inputs))
    