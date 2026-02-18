from CartePizzeria import CartePizzeria
from Pizza import Pizza

carte = CartePizzeria()

pizza1 = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
pizza2 = Pizza("Reine", ["tomate", "jambon", "champignons", "mozzarella"], 10)

carte.add_pizza(pizza1)
carte.add_pizza(pizza2)

print(carte.nb_pizzas())  # 2

carte.remove_pizza("Margherita")
print(carte.nb_pizzas())  # 1

carte.remove_pizza("4 Fromages")  # Lève une exception
