# List Comprehension
# Gibt die Möglichkeit, eine Liste anhand eines Ausdrucks zu erzeugen

# Alle Zahlen von 0 bis 100

# Normal
zahlenBis100 = []
for i in range(0, 100):
	zahlenBis100.append(i)

# Mit List Comprehension
zahlenBis100LC = [i for i in range(100)]  # Normale Schleife, Variablenname davor

print(list(range(100)))

zahlenIHochI = [i ** i for i in range(10)]  # i^i bis 10 in einer Liste
print(zahlenIHochI)

zahlenIHochIUngerade = [i ** i for i in range(10) if i % 2 != 0]  # Mit Bedingungen die LC nochmals einschränken

# Verschachtelte Schleife
kleines1x1 = [f"{z1} * {z2} = {z1 * z2}" for z1 in range(1, 11) for z2 in range(1, 11)]  # Kleines 1x1 mit LC
print(kleines1x1)

# Ternary Operator mit LC
print([f"{i}: Teilbar durch 3" if i % 3 == 0 else f"{i}: Nicht teilbar durch 3" for i in range(100)])

# List Comprehension über eine Liste
wortListe = ["DaS", "iSt", "einE", "ListE"]

# Nur alle Groß geschriebenen Wörter
print([w for w in wortListe if w[0].isupper()])

# Fehler beheben
# print("AbCfdhGDSGSDYCvs".capitalize())
print([w.capitalize() if w[0].isupper() else w.lower() for w in wortListe])

# Wörter die ein "e" oder "E" enthalten
print([w for w in wortListe if "e" in w.lower()])

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt
print([w.upper() for w in "Das ist eine Liste" if w.islower()])

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt
# Verwende hierfür die String Funktion split -> Teilt einen String anhand eines Zeichens in einzelne Array Elemente auf

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben