import os
import json

# Input/Output

# print(...)

# input(string): Gibt dem User die Möglichkeit, einen Text in die Konsole einzugeben
# Wartet auf den Input vom Benutzer
# Eingabe vom Benutzer wird in eine Variable geschrieben
# name = input("Gib deinen Namen ein: ")
# print(f"Dein Name ist: {name}")
#
# z1 = int(input("Gib eine Zahl ein: "))  # Hier explizit zu int konvertieren
# z2 = int(input("Gib eine Zahl ein: "))
# print(f"Summe: {z1 + z2}")

# Escape-Sequenzen
# Zeichen, die mit der Tastatur nicht getippt werden können (z.B. Zeilenumbruch, Tab, ...)
# \n, \r: Zeilenumbruch
# \t: Tabulator
# \", \', \\

file = open("Test.txt", "w")
file.writelines("Test1\r")
file.writelines("Test2\r")
file.writelines("Test3\r")
file.flush()
file.close()  # close ist hier wichtig, da sonst der Stream offen bleiben könnte
# Wenn der Stream geöffnet bleibt, können andere Programme nicht auf das File zugreifen
# Generell wird am Ende vom Skript der Stream automatisch geschlossen

readFile = open("Test.txt")
zeilen = readFile.readlines()
print(zeilen)

# with Block
# Ermöglicht, das Öffnen von Dateien mit automatischem Schließen am Ende von dem Block
with open("Test.txt", "w") as writeFile:
	writeFile.writelines("Test1\r")
	writeFile.writelines("Test2\r")
	writeFile.writelines("Test3\r")
	writeFile.flush()
# Hier wird writeFile automatisch geschlossen

# rstring, raw String
# String, der Escape-Sequenzen ignoriert
# Besonders nützlich für Pfade
pfad = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2023_09_04"
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2023_09_04"

# os Paket
# Verschiedene Dinge die mit dem OS gemacht werden können
# U.a. auch Pfad- und Dateioperationen
if os.path.exists("Test.txt"):
	print("Datei existiert")

fullPath = os.path.join("Mehrere", "Pfade", "kombinieren")  # Betriebssystemunabhängig Pfade zusammenbauen
print(fullPath)

# Json
# Ermöglicht, Objekte in Json Strings umzuwandeln
# Wird verwendet, für Datenaustausch im Internet (z.B. Webschnittstelle)
testList = [1, 2, 3]

# json.load, json.dump
# Ermöglicht, Erstellen und Laden von Json aus einem File
with open("Json.txt", "w") as writeJson:
	json.dump(testList, writeJson)

# json.loads, json.dumps
# Ermöglicht, Erstellen und Laden von Json aus einem String
jsonStr = json.dumps(testList)
print(jsonStr)

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden
# Bonus: Frage den Benutzer nach dem File, welches geöffnet werden soll

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Berechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Berechnung durchführen will
