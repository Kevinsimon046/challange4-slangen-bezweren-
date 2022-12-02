import random

number = random.randint(1,100)

if number < 45:
    print("common")
    
elif number >= 45 and number <65:
    print("uncommon")
    
elif number >= 65 and number <80:
    print("rare")
    
elif number >= 80 and number <95:
    print("epic") 
    
elif number >= 95:
    print("legendary")