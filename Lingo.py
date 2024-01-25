
import sqlite3
from ast import Invert
from highscores import Highscores


class Lingo:

# Constructor met de declaratie van het attribuut woord
    def __init__(self):
        self.woord = self.set_woord()
        self.beurt = 0

# Functie om een woord te selecteren uit de databasse

    def set_woord(self):
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.execute("SELECT * FROM vijfletters ORDER BY RANDOM() LIMIT 1; ")
        for row in cursor:
            woord = row[0]
        connection.close()
        print (woord)
        return woord

    def validate_input(self, invoer, naam):

    # Verhoog de beurt
        self.beurt += 1

    # Conventeer de invoer string naar kleine letters
        invoer = str.lower(invoer)

    # Controleeer of de invoer string gelijk is aan het raden
        if (invoer == self.woord):
            
            # Voeg de score toe aan de database
            score = Highscores()
            score.add_score(naam, self.beurt)

            # Retourneer de feedback
            return "Gewonnen"

    # Controleer of het woord 5 letter heeft
        if (len(invoer) != 5):
            return "Voer een woord in van 5 letters!"
        
    # Vergelijk elke letter van de invoerstring met het te raden woord
        uitvoer = "" 
        for i in range(5):
            if (invoer[i] == self.woord[i]):
                uitvoer += str.upper(invoer[i])
            elif(invoer[i] in self.woord):
                uitvoer += invoer[i]
            else:
                uitvoer += "_"
        return uitvoer

    # Geef de uitvoer string terug
        return "Okay"   