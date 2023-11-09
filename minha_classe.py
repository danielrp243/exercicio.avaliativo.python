# No arquivo minha_classe.py

class MinhaClasse:
    def __init__(self):
        print("Método Construtor da MinhaClasse")

# No arquivo main.py

from minha_classe import MinhaClasse

minha_instancia = MinhaClasse()
