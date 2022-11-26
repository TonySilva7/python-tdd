import requests


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade
        self._got_data: bool = False

    @property
    def got_data(self) -> bool:
        return self._got_data

    @got_data.setter
    def got_data(self, value: bool) -> None:
        self._got_data = value

    def obter_todos_dados(self) -> str:
        response = requests.get("https://api.github.com/users", timeout=10)
        self.got_data = True if response.ok else False
        return "SUCCESS" if response.ok else "NOT_FOUND"
