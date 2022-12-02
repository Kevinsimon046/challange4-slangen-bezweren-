print("vul hier beneden de namen in van de verkiezing. ")

inputs = []
while True:
    inp = input("namen/UITSLAG: ")
    if inp == "UITSLAG":
        break
    inputs.append(inp)
    
print("de gene die de verkiezing heeft gewonnen is... ")

print(str(max(inputs)))