import re
import Codigo


class Regex:

    def __init__(self, linhas):
        self.linhas = linhas
        self.traducao = []
        self.traduzir()

    def traduzir(self):
        pettern = r"(\w+)"

        operacao = re.compile(pettern)

        patterns = {
            "add": r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*$",
            "mov": r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*$",
            "imul": r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*,\s*(\w+)\s*$",
            "inc": r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*,\s*(\w+)\s*$", FAZER EXPRESSAO
        }

        for linha in self.linhas:
            expressao = None

            expressao = patterns[operacao]

            if expressao == None:
                raise Exception('Operador inexistente')



            codigo = Codigo(patterns[expressao], linha)

            self.traducao.append(codigo)

        return self.traducao