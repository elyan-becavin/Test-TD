import unittest
from unittest.mock import Mock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from CartePizzeria import CartePizzeria, CartePizzeriaException
from Pizza import Pizza

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        """Initialisation commune à chaque test."""
        self.carte = CartePizzeria()
        self.pizza_mock = Mock(spec=Pizza)
        self.pizza_mock.nom = "Margherita"

    # -------------------------
    # Test is_empty()
    # -------------------------
    def test_is_empty_initialement_vide(self):
        self.assertTrue(self.carte.is_empty())

    def test_is_empty_apres_ajout(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertFalse(self.carte.is_empty())

    # -------------------------
    # Test nb_pizzas()
    # -------------------------
    def test_nb_pizzas(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    # -------------------------
    # Test add_pizza()
    # -------------------------
    def test_add_pizza_ajoute_correctement(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    # -------------------------
    # Test remove_pizza()
    # -------------------------
    def test_remove_pizza_existante(self):
        self.carte.add_pizza(self.pizza_mock)
        self.carte.remove_pizza("Margherita")
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_pizza_inexistante_leve_exception(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("4 Fromages")

if __name__ == "__main__":
    unittest.main()
