print("type hier uw getallen... ")

getal1 = int(input("voer hier uw eerste getal in. "))
getal2 = int(input("voer hier uw tweede getal in. "))
getal3 = int(input("voer hier uw derde getal in. "))
getal4 = int(input("voer hier uw vierde getal in. "))
getal5 = int(input("voer hier uw vijfde getal in. "))
getal6 = int(input("voer hier uw zesde getal in. "))

getallen = getal1, getal2, getal3, getal4, getal5, getal6

print(sorted(getallen, reverse=True))