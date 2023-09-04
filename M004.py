# Schleifen

# while Schleife
# Läuft solange wie die Bedingung True ist
a = 0
b = 10
while a < b:
	print(a)  # Einrückungen beachten
	a += 1

# Endlosschleife
# while True:
#	print()

# for Schleife
# Sozusagen eine Foreach Schleife in anderen Sprachen
# Es gibt keine konventionelle for Schleife wie in anderen Sprachen (int i = 0; i < ...; i++)
# Hier kann eine Range verwendet werden, um einen Zähler darzustellen
liste = ["Das", "ist", "eine", "Liste"]

for element in liste:
	print(element)

for i in range(10):  # (int i = 0; i < 10; i++)
	print(i)  # "Reguläre" for Schleife

for i in range(-10, 10, 2):  # (int i = -10; i < 10; i += 2)
	print(i)

for i in range(0, len(liste)):  # (int i = 0; i < liste.length; i++)
	print(i)
	print(liste[i])

# break & continue
# break: Beendet die Schleife, wird häufig in Kombination mit einer if verwendet
# continue: Springt zum Schleifenkopf zurück, führt den Code danach nicht aus
for i in range(10):
	print(i)
	if i == 5:
		break  # Wenn i 5 ist, wird die Schleife beendet

for i in range(10):
	if i == 5:
		continue  # Wenn i 5 ist, wird der Rest danach übersprungen (hier print)
	print(i)

# Schleife die bis zu einer bestimmten Bedingung geht
# Mache etwas, bis es einmal funktioniert, ansonsten wiederhole das Stück Code
while True:
	# ...
	if liste:  # Hier die Endbedingung angeben
		break

# else bei Schleifen
# Code der nur ausgeführt wird, wenn die Schleife fehlerfrei beendet wurde (und ohne break)
for i in range(10):
	print(i)
	# break  # Wenn dieses break ausgeführt wird, wird das else nicht ausgeführt
else:
	print("Schleife fertig")

# for Schleife über Dictionary
meinCar = {
	"Brand": "Audi",
	"Model": "A3",
	"Year": 2017
}

# Nur keys
for key in meinCar:
	print(key)

for key in meinCar.keys():
	print(key)

# Nur values
for value in meinCar.values():
	print(value)

# Beides
for k, v in meinCar.items():  # Schleife mit 2 Laufvariablen
	print(k)
	print(v)

for kv in meinCar.items():  # Schleife mit normalen Tupel als Laufvariable
	print(kv[0])
	print(kv[1])

# fstring, formatted String
# Code in einen String einbauen
a = 5
ohneFString = "Die Zahl ist: " + str(a)  # Mehr Aufwand
fstring = f"Die Zahl ist: {a}"

for i in range(10):
	# print("Die Zahl ist " + str(i))
	# print("Die quadrierte Zahl ist " + str(i * i))
	# print(str(i) + " * " + str(i) + " = " + str(i * i))

	print(f"Die Zahl ist {i}")
	print(f"Die quadrierte Zahl ist {i * i}")
	print(f"{i} * {i} = {i * i}")

# Übung 1
# FizzBuzz
# 1. Schleife schreiben, die von 0 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
#  4
# Buzz
# ...
# 14
# FizzBuzz
for i in range(1, 100):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)

# Übung 2
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden
for i in range(1, 200):
	if i % 100 == 11 or i % 100 == 12 or i % 100 == 13:
		print(f"{i}: {i}th")
	elif i % 10 == 1:
		print(f"{i}: {i}st")
	elif i % 10 == 2:
		print(f"{i}: {i}nd")
	elif i % 10 == 3:
		print(f"{i}: {i}rd")
	else:
		print(f"{i}: {i}th")