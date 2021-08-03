import unittest
from pageobjects.calculator_screen import CalculatorScreen


class CalculatorTestCases(unittest.TestCase):

    def test_set_number(self):
        calculator = CalculatorScreen()
        calculator.click_number(5)
        calculator.click_delete_button()
        #calculator.click_all_numbers()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)