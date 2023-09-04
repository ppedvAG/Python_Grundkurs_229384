# List
# Typ der mehrere Werte halten kann
# Verschiedene Typen möglich
# Keine fixe Größe
# Ist veränderbar
# Duplikate sind erlaubt
# Hat einen Index wie String

meineListe = [1, 2, 3, 4, True, "Text"]
print(meineListe)

# Index
print(meineListe[0])
print(meineListe[-1])
print(meineListe[0:3])

# list.append(<Wert>)
# Hängt ein Element am Ende an
meineListe.append(5)
print(meineListe)

# list.insert(Index, <Wert>)
# Fügt ein Element am gegebenen Index hinzu
meineListe.insert(1, "Test")
print(meineListe)

# list.pop(Index)
# Entfernt ein Element am gegebenen Index
meineListe.pop(1)
print(meineListe)

# list.remove(<Wert>)
# Entfernt das erste Element, dass dem Wert entspricht
meineListe.remove(True)
print(meineListe)

# list.extend(<Liste>)
# Fügt alle Elemente einer Collection als einzelne neue Elemente hinzu
meineListe.extend([1, 2, 3])
print(meineListe)

meineListe.append([1, 2, 3])
print(meineListe)

# meineListe.sort()
# meineListe.clear()

# Tuple
# Funktioniert wie Liste aber ist nicht veränderbar
# Wird mit normalen Klammern erstellt
# Wird häufig als Rückgabewert oder bei Parametern von Funktionen verwendet
meinTuple = (1, 2, 3, 4)
print(meinTuple)

# Workaround um Tuple zu verändern
temp = list(meinTuple)
temp += [5]
meinTuple = tuple(temp)
print(meinTuple)

# Casting
# Konvertierung von Typen
zahl = "123"
print(int(zahl) * 2)

zahl = 123
print(str(zahl) * 2)

# Unpacking
# Zerlegen von einer Collection in ihre einzelnen Elemente
# Eine Variable pro Element
unpacking = [1, 2, 3, 4]
(a, b, c, d) = unpacking
print(a)
print(b)
print(c)
print(d)

# Range
# Bereich von X bis Y
# Nützlich bei Schleife
r100 = range(100)  # 0 bis Obergrenze -1 -> 0-99
print(r100)  # range(0, 100) -> Range wurde noch nicht erzeugt
print(list(r100))  # Iteration der Range erzwingen

print(list(range(-50, 50)))
print(list(range(-50, 50, 2)))  # Mit Schrittgröße

# Set
# Funktioniert wie Liste, ist aber eindeutig, hat keinen Index
# Benötigt geschweifte Klammern { }
meinSet = {1, 2, 3, 4}
print(meinSet)
meinSet.add(1)  # 1 wird nicht hinzugefügt, da es bereits vorhanden ist
print(meinSet)

# Dictionary
# Liste von Key-Value Paaren
# Keys müssen eindeutig sein
meinCar = {
	"Brand": "Audi",
	"Model": "A3",
	"Year": 2017
}

print(meinCar)
print(meinCar["Year"])

meinCar["Year"] = 2020
meinCar["KM"] = 10000
print(meinCar)

# dict.keys(), dict.values(), dict.items()
# Keys, Values oder beiden in Kombination holen
print(meinCar.keys())
print(meinCar.values())
print(meinCar.items())

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
