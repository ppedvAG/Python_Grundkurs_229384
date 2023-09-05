import time
# Decorator
# Sind Funktionen die andere Funktion modifizieren können
# Werden mit @<Name> hinzugefügt


# Funktionen sind auch Objekte
def test():
	pass

print(type(test))

func = test
print(func)

# Eigenen Decorator, kann später an Funktionen angehängt werden
def testDecorator(func):
	def wrapper():  # Hier werden die Konfigurationen der Funktion vorgenommen
		print("Vor der Funktion")
		func()
		print("Nach der Funktion")
	return wrapper  # Hier wird die fertige dekorierte Funktion zurückgegeben


@testDecorator  # Hier wird die Hello Funktion dekoriert
def hello():
	print("Hello World")

hello()

# Decorator mit Parametern
def testDecoratorParam(func):
	def wrapper(*args, **kwargs):  # Hier werden die Konfigurationen der Funktion vorgenommen
		print("Vor der Funktion")
		func(*args, **kwargs)
		print("Nach der Funktion")
	return wrapper


@testDecoratorParam
def printAddiere(x, y):
	print(x + y)

printAddiere(5, 8)

# Decorator mit Return
def testDecoratorReturn(func):
	def wrapper(*args, **kwargs):  # Hier werden die Konfigurationen der Funktion vorgenommen
		print("Vor der Funktion")
		return func(*args, **kwargs)
	return wrapper


@testDecoratorReturn
def addiere(x, y):
	return x + y

print(addiere(4, 5))


# Sinnvoller Decorator
def measureTime(func):
	def wrapper(*args, **kwargs):
		starttime = time.time()
		func(*args, **kwargs)
		print(f"Benötigte Zeit: {time.time() - starttime}s")
	return wrapper


@measureTime
def print100_000():
	for i in range(1000000):
		print(i)

print100_000()

class Square:
	def __init__(self, seitenlaenge):
		self._seitenlaenge = seitenlaenge  # Felder mit _ sollten ein private Feld darstellen

	# Get-Property
	@property
	def seitenlaenge(self):
		return self._seitenlaenge

	# Set-Property
	@seitenlaenge.setter
	def seitenlaenge(self, neueLaenge):
		if neueLaenge > 0 and neueLaenge < 100:
			self._seitenlaenge = neueLaenge
		else:
			print("Neue Länge zu klein/groß")

square = Square(10)
print(square._seitenlaenge)  # Sollte nicht angegriffen werden
print(square.seitenlaenge)
square.seitenlaenge = 20