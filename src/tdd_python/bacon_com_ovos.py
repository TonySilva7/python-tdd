"""
1. Receber apenas número inteiro
2. Se o número for múltiplo de 3 e 5, retornar "Bacon com ovos"
3. Se o número for múltiplo de 3, retornar "Bacon"
4. Se o número for múltiplo de 5, retornar "Ovos"
5. Se o número não for múltiplo de 3 nem de 5, retornar "Passa fome"
"""


class BaconComOvos:
    def bacon_com_ovos(self, number) -> str:
        switcher: dict[int, str] = {
            1: "Bacon com ovos",
            2: "Bacon",
            3: "Ovos",
            4: "Passar fome",
        }

        return switcher[
            1
            if number % 3 == 0 and number % 5 == 0
            else 2
            if number % 3 == 0
            else 3
            if number % 5 == 0
            else 4
        ]
