import unittest

from src.tdd_python.calculadora import my_sum


class TestCalculadora(unittest.TestCase):
    def test_should_be_five(self):
        result = my_sum(2, 3)
        self.assertEqual(result, 5)

    def test_should_rise_exception_of_type_type_error(self):
        with self.assertRaises(TypeError):
            my_sum(0, "b")


if __name__ == "__main__":
    unittest.main()
