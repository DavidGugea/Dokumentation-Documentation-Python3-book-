import math

class MeineKlasse:
    """Beispiel fuer Docstrings.

    Diese Klasse zeigt, wie Docstrings verwendet
    werden.
    """
    pass

def MeineFunktion():
    """Diese Funktion macht nichts.

    Im Ernst, diese Funktion macht wirklich nichts.
    """
    pass

print(MeineKlasse.__doc__) # Gets the docstring of the class
print(MeineFunktion.__doc__) # Gets the docstring of the function
print(math.__doc__)
print(help(math))
