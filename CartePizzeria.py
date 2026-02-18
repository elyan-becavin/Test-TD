from CartePizzeriaException import CartePizzeriaException
from Pizza import Pizza


class CartePizzeria:
    def __init__(self):
        self._pizzas = []

    def is_empty(self):
        """Retourne True si la carte est vide, False sinon."""
        return len(self._pizzas) == 0

    def nb_pizzas(self):
        """Retourne le nombre de pizzas dans la carte."""
        return len(self._pizzas)

    def add_pizza(self, pizza):
        """Ajoute une pizza à la carte."""
        if not isinstance(pizza, Pizza):
            raise CartePizzeriaException("Seuls les objets Pizza peuvent être ajoutés.")
        self._pizzas.append(pizza)

    def remove_pizza(self, name):
        """
        Retire la pizza nommée 'name' de la carte.
        Lève une CartePizzeriaException si elle n'existe pas.
        """
        for pizza in self._pizzas:
            if pizza.nom == name:
                self._pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte.")