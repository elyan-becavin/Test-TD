class Pizza:
    def __init__(self, nom, ingredients, prix):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

    def __str__(self):
        return f"{self.nom} - {self.prix}€ ({', '.join(self.ingredients)})"

    def __eq__(self, other):
        if isinstance(other, Pizza):
            return self.nom == other.nom
        return False