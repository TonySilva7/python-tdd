try:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
except Exception as exc:
    raise ImportError("Não foi possível importar o módulo") from exc

import unittest
from src.tdd_python.bacon_com_ovos import BaconComOvos


class TestBaconComOvos(unittest.TestCase):
    bco: BaconComOvos

    def setUp(self) -> None:
        self.bco = BaconComOvos()

    def test_should_rise_exception_no_int(self) -> None:
        with self.assertRaises(TypeError):
            self.bco.bacon_com_ovos("b")

    def test_should_return_bacon_com_ovos_if_multiple_tree_and_five(self) -> None:
        entries = (15, 30, 45, 60, 75, 90, 105, 120, 135, 150)
        excepted = "Bacon com ovos"
        for entry in entries:
            with self.subTest(message="Bacon com Ovos", entry=entry, excepted=excepted):
                output = self.bco.bacon_com_ovos(entry)
                self.assertEqual(
                    output, excepted, msg=f'Esperado "{excepted}" mas recebeu "{output}"'
                )

    def test_should_return_passar_fome_if_not_multiple_tree_and_five(self) -> None:
        entries = (1, 2, 4, 7, 8)
        excepted = "Passar fome"
        for entry in entries:
            with self.subTest(message="Bacon com Ovos", entry=entry, excepted=excepted):
                output = self.bco.bacon_com_ovos(entry)
                self.assertEqual(
                    output, excepted, msg=f'Esperado "{excepted}" mas recebeu "{output}"'
                )

    def test_should_return_bacon_if_not_multiple_tree(self) -> None:
        entries = (3, 6, 9, 12, 18, 27)
        excepted = "Bacon"
        for entry in entries:
            with self.subTest(message="Bacon com Ovos", entry=entry, excepted=excepted):
                output = self.bco.bacon_com_ovos(entry)
                self.assertEqual(
                    output, excepted, msg=f'Esperado "{excepted}" mas recebeu "{output}"'
                )

    def test_should_return_ovos_if_not_multiple_five(self) -> None:
        entries = (5, 10, 20, 25, 35, 40)
        excepted = "Ovos"
        for entry in entries:
            with self.subTest(message="Bacon com Ovos", entry=entry, excepted=excepted):
                output = self.bco.bacon_com_ovos(entry)
                self.assertEqual(
                    output, excepted, msg=f'Esperado "{excepted}" mas recebeu "{output}"'
                )

    def tearDown(self) -> None:
        del self.bco


if __name__ == "__main__":
    unittest.main(verbosity=2)
