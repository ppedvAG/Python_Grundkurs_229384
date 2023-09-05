import sqlite3 as sql
# Datenbankverbindung

# Hierfür verwende ich sqlite3

# Eine Verbindung besteht immer aus Connection und Cursor
# Connection für die Verbindung
# Cursor für die Daten

class Person:
	def __init__(self, row: tuple):
		self.id = row[0]
		self.name = row[1]

	def __str__(self):
		return f"Die Person hat die ID {self.id} und heißt {self.name}"

connection = sql.connect("Test.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE Personen(id int, name varchar(50))")
# for i in range(2, 10):
# 	cursor.execute(f"INSERT INTO Personen VALUES({i}, 'Lukas')")
# connection.commit()

results = cursor.execute("SELECT * FROM Personen").fetchall()  # Hier kommt eine Liste von Tupeln als Ergebnis heraus
print(list(map(lambda row: Person(row), results)))
connection.commit()


try:
	with sql.connect("Test.db") as connection:
		cursor = connection.cursor()

		results = cursor.execute("SELECT * FROM Personen").fetchall()  # Hier kommt eine Liste von Tupeln als Ergebnis heraus
		print(list(map(lambda row: Person(row), results)))
except sql.Error:
	print("Fehler")