import M007
import sys
import os
# from M007 import countCase

# Hier wird durch den import "Das ist M007" in der Konsole ausgegeben
M007.countCase("Das ist ein Text")

# Modul Suchpfade
# 1. Im Ordner des ausgeführten Skripts
# 2. In der Standardbibliothek/venv
# 3. Bei der Konfiguration von der Python Runtime können auch zusätzliche Pfade angegeben werden
# Wenn das Modul nicht gefunden wird -> ModuleNotFoundError
print(sys.path)  # Listet alle Modul Suchpfade auf
print(sys.version)  # Gibt die Python Runtime Version aus
# sys.exit(0)  # Das Skript beenden, Fehlercodes: 0 -> alles OK, nicht 0 -> Fehler, in Dokumentation festhalten

# Externe Pakete installieren
# 2 Möglichkeiten
# - Über Python Packages
# - Über pip (über Terminal, Powershell, Bash, ...)
# -- pip install <Paket>
# -- pip uninstall <Paket>

# __name__
# Gibt den Namen des Skripts aus, oder __main__ wenn das Skript direkt ausgeführt wird
print(__name__)

# __init__.py
# Wird ausgeführt, wenn der gesamte Ordner importiert wird

# Separate Main Methode wird auch öfters gemacht
def main():
	print("Das ist das Hauptskript")

# Diese Zeile wird ausgeführt, wenn das Skript direkt gestartet wird
# Wird in anderen Sprachen als Main Methode bezeichnet
# Generell am Ende eines Python Skripts zu finden
if __name__ == "__main__":
	main()