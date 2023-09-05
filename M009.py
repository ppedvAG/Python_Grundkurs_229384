# Klassen und Objekte

# Objekt
# Alles in Python sind Objekte (Variablen, Funktionen, Klassen, ...)
# Jedes Objekt hat einen Typen (int, str, bool, list, func, ...)
# Jedes Objekt hat den Inhalt seiner entsprechenden Klasse (Variablen, Funktionen)

i = 12  # Hier wird ein Int Objekt erstellt und in i geschrieben
i.as_integer_ratio()  # Hier eine Funktion des Objekts benutzen
print(type(i))  # <class 'int'>

# Typvergleiche
# Manchmal muss überprüft werden, was ein Objekt für einen Typen hat

# Genauer Typvergleich
if type(i) == int:  # Ist i genau ein int?
	print("i ist genau ein int")  # True

if type(i) == object:  # Ist i genau ein object?
	print("i ist genau ein object")  # False

# Vererbungshierarchie Typvergleich
# isinstance(<Objekt>, <Typ>)
if isinstance(i, int):
	print("i ist ein int")

if isinstance(i, object):
	print("i ist ein object")

# Funktionen sind selbst auch Objekte
def hallo():
	print("Hallo")

print(type(hallo))

# Klasse
# Bauplan, der Objekte erstellt
# Struktur des Objekts wird hier vorgegeben (keine konkreten Werte)
class Tisch:
	# Konstruktor
	# Ist in Python eine normale Funktion namens __init__
	# Hier MÜSSEN alle Instanzvariablen deklariert werden (-> Attribute, die das Objekt besitzen soll)
	# Um mehrere Konstruktoren zu ermöglichen, müssen optionale Parameter verwendet werden
	def __init__(self, laenge, breite, hoehe=0):  # self: Immer das Objekt selbst, muss bei jeder Funktion angegeben werden
		self.laenge = laenge  # Hier bekommt der Tisch Variablen
		self.breite = breite
		self.hoehe = hoehe

	def move(self, x: int, y: int):
		print(f"Der Tisch hat sich {pow(pow(x, 2) + pow(y, 2), -1)}cm bewegt")

	# __str__: Gibt eine Stringrepräsentation des Objekts zurück
	# Wird in anderen Sprachen als ToString bezeichnet
	# Wenn das Objekt in print verwendet wird, wird dabei die __str__ aufgerufen
	def __str__(self):
		return f"Der Tisch ist {self.laenge}cm lang und {self.breite}cm breit"

	# Klassenvariable
	# "Globale" Variable, die zwischen jedem Objekt der Klasse geteilt ist
	# Wenn x bei einem Tisch Objekt geändert wird, wird es bei jedem Objekt geändert
	x = 100


# Objekt erstellen
# <Klassenname>(), ohne new
tisch = Tisch(laenge=200, breite=100)  # Hier müssen die geforderten Werte übergeben werden
print(tisch.laenge)  # Jedes Tisch Objekt hat separate Werte für Länge und Breite
print(tisch.breite)

tisch.move(200, 150)  # Jedes Tisch Objekt hat jetzt die move Funktion

# Ohne __str__: <__main__.Tisch object at 0x0000025153A2BFD0> (Typ, Speicheradresse)
# Mit __str__: Der Tisch ist 200cm lang und 100cm breit
print(tisch.__str__())
print(tisch)

# Dynamische Properties
# In Python können beliebige Werte zu Objekten hinzugefügt werden
# Dynamic Properties sollten vermieden werden
tisch.keineAhnung = 123
print(tisch.keineAhnung)

del tisch.keineAhnung

# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten:
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen (Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum) -> Parameter int (Wieviel soll beschleunigt werden)
#     - StarteMotor (Setze Motorzustand auf True, funktioniert nur wenn das Auto noch nicht gestartet ist)
#     - StoppeMotor (Motor kann nur gestoppt werden, wenn das Auto nicht fährt)
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion (Konkrete Werte)
