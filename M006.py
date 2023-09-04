# Funktionen

# Code wiederverwendbar machen
# Funktionen in Python sind Objekte und werden beim Ausführen des Skripts instanziert
# Wenn das Python Skript in einem anderen Skript geladen wird, wird es komplett ausgeführt
# def Statements werden danach ausgeführt, und dadurch werden alle Funktionen instanziert

# hallo()  # Hier ist die Funktion hallo() noch nicht definiert

def hallo():
	print("Hallo")


hallo()  # Funktion ausführen


# Funktion mit Parameter
def hallo(deinName):
	print(f"Dein Name ist: {deinName}")


hallo("Lukas")
hallo(123)
hallo([1, 2, 3])  # Hier kann ein beliebiger Wert eingesetzt werden


def halloGut(deinName: str):  # Mit : <Typ> den Benutzer auf einen Typen hinweisen
	if type(deinName) == str:  # Hier eine Typprüfung durchführen um Fehlerverhalten zu vermeiden
		print(deinName)


halloGut("Lukas")
halloGut(123)  # Warning, kein Fehler
halloGut([1, 2, 3])

# Funktionen mit Rückgabewert
"ABC".count("B")  # Ergebnis 1, kann weiterverwendet werden (z.B. in if)


def addiere(x, y):
	return x + y  # Hier kommt bei Ausführung der Funktion ein Ergebnis zurück


addiere(3, 4)
addiere(3.5, 4.5)
addiere("ABC", "123")
addiere([1, 2, 3], [4, 5, 6])


def addiereGut(x: int, y: int) -> int:  # Funktion typisieren, return Typ wurde auch angegeben (-> int)
	return x + y


addiereGut(3, 4)
addiereGut(3.5, 4.5)
addiereGut("ABC", "123")
addiereGut([1, 2, 3], [4, 5, 6])


# Alle Typangaben in Python sind nur Empfehlungen

# Default Werte
# Standardwerte bei Parametern festlegen, die der User anpassen kann aber nicht muss
def subtrahiere(x: int, y: int, z=0):
	return x - y - z


subtrahiere(3, 4)  # Hier z=0
subtrahiere(3, 4, 5)  # Hier z=5


def addOrSub(x: int, y: int, sub=False):  # Optionaler Boolean Parameter um das Verhalten der Funktion anzupassen, falls notwendig
	if ~sub:
		return x + y
	else:
		return x - y


addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(4, 5)
addOrSub(2, 8, True)  # Hier ein Einzelfall bei dem die Funktion anders arbeiten soll


def printPerson(vorname="", nachname="", alter=0, adresse=""):  # Methode mit 10+ Parametern
	print("...")


printPerson(alter=30, adresse="Zuhause")  # Über optionale Parameter die Funktion konfigurieren
printPerson(vorname="Max", alter=25)  # Nur die Parameter befüllen die ich wirklich brauche


# Arbitrary Arguments (* Parameter)
# Gibt die Möglichkeit, bei Ausführung der Funktion, beliebig viele Parameter zu übergeben
def sumNumbers(*numbers: int):
	summe = 0
	for i in numbers:
		summe += i
	return summe


sumNumbers(1, 2, 3)  # 3 Parameter
sumNumbers(1, 2, 3, 4, 5, 6, 7)  # 7 Parameter
sumNumbers()  # Keine Parameter sind auch beliebig viele Parameter


# Arbitrary Keyword Arguments (** Parameter)
# Gibt die Möglichkeit, beliebig viele Key-Value Paare bei einer Funktion zu übergeben
def listTeilnehmer(**teilnehmer):  # **teilnehmer ist ein dict
	for key, value in teilnehmer.items():
		print(f"Der Name von {key} ist {value}")


listTeilnehmer(Teilnehmer1="Max", Teilnehmer2="Lukas", Teilnehmer3="Uwe", Teilnehmer4="Muhammad")

# Unpacking Operatoren
# Ermöglichen, eine Liste von Einträgen bei * oder ** Argumenten zu übergeben
# * für Listen, ** für Dictionary
print(sumNumbers(*[1, 2, 3, 4, 5, 6]))

tn = {
	"T1": "Max",
	"T2": "Lukas",
	"T3": "Uwe",
	"T4": "Muhammad"
}

listTeilnehmer(**tn)


# / Parameter
# Ermöglicht, die Reihenfolge von normalen Parametern zu erzwingen
def test(x, y, z, w):
	print("...")


test(z=5, w=3, x=1, y=9)  # Reihenfolge kann beliebig angepasst werden


def test2(x, y, /, z, w):  # x und y müssen genau an der richtigen Position sein
	print("...")


test2(3, 4, w=3, z=1)
test2(3, 4, z=3, w=1)


# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# und uns die größte dieser Zahlen zurückgibt
# Auch negative Zahlen sollen berücksichtigt werden
def ersteFunktion(*mehrereParameter):
	print(mehrereParameter)
	maximum = mehrereParameter[0]
	for i in mehrereParameter:
		if i > maximum:
			maximum = i
	print(maximum)


ersteFunktion(-77, -2, -3, -4, -5, -6, -10, -66)

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
