# Module
# Sind Bibliotheken, die sich aus Skripten bilden, und Funktionalitäten bringen die wir benötigen
# Enthalten die Code, der sich genau mit einem Thema befasst
# Können importiert und installiert werden

# Wie importiere ich ein Modul?
# import turtle  # Durch diesen Import wird das Skript vollständig ausgeführt

# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(400)
#     turtle.left(170)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill()
# turtle.done()

# Alias
# Gibt die Möglichkeit, ein Skript umzubenennen
# import turtle as t  # Durch den Alias kann das Skript nun mit t angesprochen werden, statt mit turtle

# t.color('red', 'yellow')
# t.begin_fill()
# while True:
#     t.forward(400)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t.done()

# from import
# Ermöglicht das importieren von bestimmten Funktionen und Klassen anstatt von allen Membern
# Bei den entsprechenden Funktionen muss dann nicht mehr der Prefix angegeben werden um die Funktionen aufzurufen (Member sind jetzt im Skript implementiert)
# from turtle import color, begin_fill, forward, left, pos, end_fill, done
# from turtle import *

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(400)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

def countCase(text: str):
	k, g, s = 0, 0, 0
	for buchstabe in text:
		if buchstabe.islower():
			k += 1
		elif buchstabe.isupper():
			g += 1
		else:
			s += 1
	print(f"Kleinbuchstaben: {k} | Großbuchstaben: {g} | Sonderzeichen: {s}")

print("Das ist M007")