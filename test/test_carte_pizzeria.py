import unittest
from unittest.mock import Mock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from CartePizzeria import CartePizzeria, CartePizzeriaException
from Pizza import Pizza




class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        self.carte = CartePizzeria()

    # -------------------------
    # Test is_empty()
    # -------------------------
    def test_is_empty_initialement_vide(self):
        self.assertTrue(self.carte.is_empty())

    def test_is_empty_apres_ajout(self):
        pizza_mock = Mock(spec=Pizza)
        pizza_mock.nom = "Margherita"

        self.carte.add_pizza(pizza_mock)

        self.assertFalse(self.carte.is_empty())

    # -------------------------
    # Test nb_pizzas()
    # -------------------------
    def test_nb_pizzas(self):
        pizza1 = Mock(spec=Pizza)
        pizza1.nom = "Margherita"

        pizza2 = Mock(spec=Pizza)
        pizza2.nom = "Reine"

        self.carte.add_pizza(pizza1)
        self.carte.add_pizza(pizza2)

        self.assertEqual(self.carte.nb_pizzas(), 2)

    # -------------------------
    # Test add_pizza()
    # -------------------------
    def test_add_pizza_ajoute_correctement(self):
        pizza = Mock(spec=Pizza)
        pizza.nom = "Margherita"

        self.carte.add_pizza(pizza)

        self.assertEqual(self.carte.nb_pizzas(), 1)

    # -------------------------
    # Test remove_pizza()
    # -------------------------
    def test_remove_pizza_existante(self):
        pizza = Mock(spec=Pizza)
        pizza.nom = "Margherita"

        self.carte.add_pizza(pizza)
        self.carte.remove_pizza("Margherita")

        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_pizza_inexistante_leve_exception(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("4 Fromages")


if __name__ == "__main__":
    unittest.main()
