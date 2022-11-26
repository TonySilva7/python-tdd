try:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    print(os.path.join(os.path.dirname(__file__), ".."))
except Exception as exc:
    raise ImportError("Não foi possível importar o módulo") from exc

import unittest
from unittest.mock import patch
from src.tdd_python.pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    pessoa: Pessoa

    def setUp(self) -> None:
        self.pessoa = Pessoa("João", "Silva", 42)

    def test_should_has_correctly_name(self):
        excepted = "João"
        output = self.pessoa.nome
        self.assertEqual(output, excepted, msg=f'Esperado "{excepted}", mas recebido "{output}"')

    def test_should_isinstance_str(self):
        output = isinstance(self.pessoa.nome, str)

        self.assertIsInstance(
            self.pessoa.nome,
            str,
            msg=f'Esperado "{True}", mas recebido "{output}"',
        )

    def test_should_has_correctly_last_name(self):
        excepted = "Silva"
        output = self.pessoa.sobrenome
        self.assertEqual(output, excepted, msg=f'Esperado "{excepted}", mas recebido "{output}"')

    def test_should_has_correctly_age(self):
        excepted = 42
        output = self.pessoa.idade
        self.assertEqual(output, excepted, msg=f'Esperado "{excepted}", mas recebido "{output}"')

    def test_should_has_got_data(self):
        excepted = False
        output = self.pessoa.got_data
        self.assertEqual(output, excepted, msg=f'Esperado "{excepted}", mas recebido "{output}"')

        self.pessoa.got_data = True

        excepted = True
        output = self.pessoa.got_data
        self.assertEqual(output, excepted, msg=f'Esperado "{excepted}", mas recebido "{output}"')

    # Vc pode usar esse mock abaixo para requisições HTTP
    def test_should_got_data_success_200(self):
        self.pessoa.got_data = False

        with patch("requests.get") as mock_get:
            mock_get.return_value.ok = True

            excepted = "SUCCESS"
            output = self.pessoa.obter_todos_dados()
            self.assertEqual(
                output, excepted, msg=f'Esperado "{excepted}", mas recebido "{output}"'
            )

            self.assertTrue(self.pessoa.got_data)

    def test_should_got_data_success_404(self):
        self.pessoa.got_data = True

        with patch("requests.get") as mock_get:
            mock_get.return_value.ok = False

            excepted = "NOT_FOUND"
            output = self.pessoa.obter_todos_dados()
            self.assertEqual(
                output, excepted, msg=f'Esperado "{excepted}", mas recebido "{output}"'
            )
            self.assertFalse(self.pessoa.got_data)

    def tearDown(self) -> None:
        del self.pessoa


if __name__ == "__main__":
    unittest.main(verbosity=2)
