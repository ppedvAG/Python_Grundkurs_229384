# Fehlerbehandlung

def test(test):
	print(test)

# print("Vor dem Fehler")

# test()  # TypeError, fehlendes Argument

def rec():
	rec()

# rec()  # RecursionError

try:
	eingabe = int(input("Gib eine Zahl ein: "))
except ValueError as e:
	print("Keine Zahl eingegeben")
	print(e)
except Exception:
	pass
else:
	# Wenn kein Fehler aufgetreten ist
	pass
finally:
	# Passiert immer (egal ob Fehler oder kein Fehler)
	pass

class CoffeeError(Exception):
	pass

raise CoffeeError  # raise = throw
