from highscores import Highscores
import sqlite3

# Test het maken van tabel
scores = Highscores()

# Verwijder de tabel weer
connection = sqlite3.connect('lingo.sqlite3')
cursor = connection.cursor()
cursor.execute("DROP TABLE highscores; ")
connection.close

# Test het toevoegen van een score
scores.add_score(" Tomas", 100)
