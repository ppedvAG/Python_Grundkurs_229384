# Vererbung
# Klassen können Oberklassen haben, und damit eine Vererbungshierarchie herstellen
# Oberklassen geben ihre Funktionen, Variablen nach unten weiter

class Lebewesen:
	"""
	Das ist die Lebewesen Klasse. Sie wird verwendet um Vererbt zu werden, und hat einen Namen und gibt die Bewegen Funktion vor.
	"""
	def __init__(self, name: str):
		"""
		Der Konstruktor des Lebewesens. Er nimmt einen Namen als Parameter.

		:param name: Der Name des Lebewesens
		"""
		self.name = name

	# Die bewegen Funktion wird nach unten weitervererbt -> Mensch hat auch bewegen
	def bewegen(self, distanz: int):  # self hat hier den tatsächlichen Typen des Objekts, und demnach passt sich hier die Ausgabe an
		print(f"{type(self).__name__} hat sich um {distanz}m bewegt")

	def __str__(self):
		return f"Mein Name ist {self.name}"

class Mensch(Lebewesen):
	# Bei __init__ in der Unterklasse sollte __init__ aus der Oberklasse verwendet werden
	# Dafür müssen die Parameter hinzugefügt werden
	def __init__(self, name: str, alter: int):
		super().__init__(name)  # super(): Nach oben greifen
		self.alter = alter

	def sprechen(self, text: str):
		print(text)

	def __str__(self):
		return f"{super().__str__()} und ich bin {self.alter} Jahre alt"

mensch = Mensch("Max", 34)
mensch.bewegen(10)
mensch.sprechen("Das ist ein Text")
print(mensch)

# docstring
# Enthält Beschreibungen zum Code
# Wird geschrieben mit """ ... """ (auch mit ''' möglich)
# Muss unter dem entsprechenden Typen/Member geschrieben werden
# Mit :param <Name>: und :return: können die entsprechenden Dinge dokumentiert werden