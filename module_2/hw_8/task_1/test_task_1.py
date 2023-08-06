from Beetroot_homeworks.module_2.hw_8.task_1.task_1 import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator(50, 2)

    def test_addition(self):
        self.assertEqual(self.calculator.addition(), "Your answer is: 52")

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(), "Your answer is: 48")

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(), "Your answer is: 100")

    def test_exponentiation(self):
        self.assertEqual(self.calculator.exponentiation(), "Your answer is: 2500")

    def test_division(self):
        self.assertEqual(self.calculator.division(), "Your answer is: 25.0")

    def test_floor_division(self):
        self.assertEqual(self.calculator.floor_division(), "Your answer is: 25")

    def test_modulus(self):
        self.assertEqual(self.calculator.modulus(), "Your answer is: 0")


if __name__ == "__main__":
    unittest.main()
