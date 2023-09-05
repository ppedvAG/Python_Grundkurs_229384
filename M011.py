# Lambda Expressions

# Anonyme Funktionen: Funktionen die nur temporär in einer Variable gespeichert werden, oder als Parameter definiert werden, ohne explizit angelegt zu werden
# In anderen Sprachen =>, ->
# In Python gibt es stattdessen das lambda Keyword
# Eigenschaften
# - Kein Name
# - Beliebig viele Parameter
# - Body ohne return
# - Nur eine Zeile Code
# - Keine Schleifen, kein break/continue

# Syntax:
# lambda <Parameter>: <Funktion>
addiere = lambda x, y: x + y  # Return Wert ist hier vorhanden aber ohne return
print(addiere(3, 4))

printAddiere = lambda x, y: print(x + y)
printAddiere(5, 6)

# Verwendung von Lambda Expressions
def lambdaTest(l):
	l()

lambdaTest(lambda: print("Hallo"))  # Über den Lambda-Parameter die Funktionsweise der Funktion anpassen

# *args und **kwargs sind auch möglich als Parameter
argsLambda = lambda *zahlen: sum(zahlen)
print(argsLambda(3, 4, 5, 6, 7, 8))

# Häufig verwendete Lambda-Funktionen
# filter(): Filtert die Collection anhand einer Bedingung
# map(): Wandelt die Collection in eine neue Form um

# filter()
zahlenListe = list(range(100))

# Schleife
zahlenGerade = []
for i in zahlenListe:
	if i % 2 == 0:
		zahlenGerade.append(i)

# List Comprehension
print([i for i in zahlenListe if i % 2 == 0])

# Mit filter()
# Die filter Funktion geht die Liste in einer Schleife durch, und nimmt alle Elemente mit die in die Lambda-Expression passen
print(filter(lambda x: x % 2 == 0, zahlenListe))  # filter() erzeugt ein Filter Objekt, muss iteriert werden um den Inhalt zu bekommen
print(list(filter(lambda x: x % 2 == 0, zahlenListe)))

# Bei Lambda Expressions können auch normale Funktionen eingesetzt werden
def mod3(x):
	return x % 3 == 0

print(list(filter(mod3, zahlenListe)))


# map()
zahlenListeString = []
for i in zahlenListe:
	zahlenListeString.append(f"Die Zahl ist {i}")

# LC
print([f"Die Zahl ist {i}" for i in zahlenListe])

# Mit map()
print(list(map(lambda x: f"Die Zahl ist {x}", zahlenListe)))

# Mit map() eine "Tabelle" erzeugen
for t in map(lambda x: (x, f"Die Zahl ist {x}", x ** x), zahlenListe):
	print(t)