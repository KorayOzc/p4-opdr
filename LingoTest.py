from Lingo import Lingo

# Maak een instantie van Lingo
mijnLingo = Lingo()



# Controleer het woord
print(mijnLingo.validate_input("lingo"))

# Test het juiste woord
uitvoer = mijnLingo.validate_input("lingo")
if (uitvoer == "Gewonnen"):
    print("Test OK! - Het juiste woord is:" + uitvoer)
else: 
    print("Test failed - Het juiste woord is: " + uitvoer)

# Test de juiste lengte 
uitvoer = mijnLingo.validate_input("lingo")
if (uitvoer == "Gewonnen"):
    print("Test OK! - De juiste lengte: " + uitvoer)
else: 
    print("Test failed - De juiste lengte: " + uitvoer)


# Test de juiste letter op de juiste plek
invoer ="liaaa"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "LI___"):
    print("Test OK! - DE juiste letter op de juiste plek:  " + uitvoer)
else: 
    print("Test failed - DE juiste letter op de juiste plek: " + uitvoer)

# Test de juiste letter op de verkeerde plek
invoer ="liaaa"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "___li"):
    print("Test OK! - DE juiste letter op de juiste plek:  " + uitvoer)
else: 
    print("Test failed - DE juiste letter op de juiste plek: " + uitvoer)

# Test de foute letters
invoer ="aaaaa"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "_____"):
    print("Test OK! - DE juiste letter op de juiste plek:  " + uitvoer)
else: 
    print("Test failed - DE juiste letter op de juiste plek: " + uitvoer)
