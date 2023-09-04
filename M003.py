# Kontrollstrukturen

# Werden in Kombination mit logischen Operatoren verwendet

# Vergleichsoperatoren
# <, >, <=, >=
# ==, !=

# Logische Operatoren
# and, or, not
# &, |, ~
# in: Ist ein Element in einer Liste enthalten?
# is: Sind zwei Objekte identisch? (Speicheradressenvergleich)

a = 4
b = 8
if a < b:  # Hier Doppelpunkt
	print("a kleiner b")  # Hier Einrückung

	if a < 5:
		print("a kleiner als 5")  # Zwei Einrückungen

	print("Innerhalb der if, aber nicht in der inneren if")
print("Außerhalb beider ifs")


if a < b:
	print("a kleiner b")
elif a > b:  # Eigenes elif Keyword
	print("a größer b")
else:
	print("a gleich b")

# Ternary Operator
# Ermöglicht die Komprimierung von if-elif-else Blöcken in eine Zeile
# Bei diesem Operator muss ein Rückgabewert herauskommen (z.B. string)
evaluation = "a kleiner b" if a < b else "a größer b" if a > b else "a gleich b"
print(evaluation)

print("a kleiner b" if a < b else "a größer b" if a > b else "a gleich b")


print("a kleiner b" if a < b else "a größer-gleich b")

c = 10
if a < b and a < c or b < c:
	print()

if not a < b:
	print()

if 3 in [1, 2, 3, 4, 5]:  # Beliebiges Iterierbares Objekt (List, Tuple, String, ...)
	print("3 ist in der Liste vorhanden")

if "m" in "Max Mustermann":
	print("m ist in Max Mustermann vorhanden")

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10