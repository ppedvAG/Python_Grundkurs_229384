# Ich bin ein Kommentar
# Keine mehrzeiligen Kommentare

x = 5  # Variablen nehmen den Typen anhand ihres Inhalts an
x = "Test"  # x ändert ihren Typen auf str

# Datentypen
# int, float, str, bool

# Integer, kann beliebig große/kleine Zahlen halten
zahl = 32795230589742976032716589023756742907596423865932074568439756739

# Float, kann beliebig große/kleine Kommazahlen halten
kommazahl = 23765792385627391475236.23857692183577623940528635772368759293576459035479045234920454647940213546

# String, auch verantwortlich für einzelne Zeichen (char)
test = "Ein Text"
zeichen = 'A'  # Einzelne Hochkomma sind identisch zu doppelten Hochkomma (Konvention gibt einzelne Hochkomma vor)

# Boolean, True oder False
wahr = True
falsch = False

# Stringfunktionen
text = "Max Mustermann"

# str.count("Zeichen"): Zählt die Anzahl der Vorkommnisse des Zeichens
text.count("M")  # Diese Zeile macht alleine nichts, berechnet nur den Wert
print(text.count("M"))  # Groß-/Kleinschreibung wird hier nicht beachtet

# str.lower(), str.upper(): String lowercase oder UPPERCASE machen
print(text.lower())
print(text.upper())
print(text)  # Originaler String wird nicht verändert

# Beide Funktionen kombinieren um das gewünschte Ergebnis zu bekommen
print(text.lower().count("m"))

# Index
# Ermöglicht, auf bestimmte Stellen in einer Collection zuzugreifen
# String ist eine Liste von einzelnen Zeichen -> angreifbar durch Index
print(text[0])
print(text[0].islower())  # Nachdem alles in Python was ein Textzeichen enthält ein String ist, können hier auch Stringfunktionen angewandt werden

print(text[0:3])  # Nimm alle Elemente von 0 bis 2 (Obergrenze exkludiert)
print(text[-1])  # Nimm von rechts das erste Zeichen (hier ist -1 sozusagen 0 von der anderen Seite)
print(text[-4:-1])  # Nimm alle Elemente vom 4t letzten Zeichen bis zum vorletzten Zeichen (Obergrenze exkludiert)
print(text[-4:])  # Nimm alle Elemente vom 4t letzten Zeichen bis zum letzten Zeichen
print(text[:3])

# str.isalpha(), str.isnumeric(), str.isalnum()
print(text.isalpha())  # Nur Buchstaben
print(text.isnumeric())  # Nur Zahlen
print(text.isalnum())  # Nur Zahlen und Zeichen

# len(<Variable>)
# Gibt die Länge des Objekts aus
print(len(text))

# type(<Variable>)
# Gibt den Typen der Variable aus
print(type(text))

# complex
# Komplexe Zahlen
complex = 5 + 12j

# Arithmetik
# +, -, *, /
# Modulo %
# Potenzierung **
# Ganzzahldivision //
zahl1 = 5
zahl2 = 8

print(zahl1 + zahl2)  # Berechnet nur die Summe, verändert nicht die originalen Zahlen
zahl1 += zahl2  # Hier wird zahl1 verändert

print(zahl1 % zahl2)
print(zahl1 ** zahl2)
print(zahl1 // zahl2)  # Normalerweise 1.625 -> hier 1

# Arithmetik bei Strings
wort1 = "Ein"
wort2 = "Test"
print(wort1 + wort2)
wort1 += wort2
print(wort1)

# Strings multiplizieren
print(wort1 * 20)  # EinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTestEinTest
wort1 *= 5

# Übung1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable

# Übung2
# Nimm die potenzierte Zahl aus Übung1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist

# Übung3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein

# Übung4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus
