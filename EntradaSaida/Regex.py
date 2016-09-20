import re
import Codigo


class Regex:

    def __init__(self, linhas):
        self.linhas = linhas
        self.traducao = []
        self.traduzir()

    def traduzir(self):
        pattern = r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*$" # pattern está incorreto para a multiplicacao
        patternmult = r"^\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s*,\s*(\w+)\s*$" # só funciona multiplicacao

        comp = re.compile(pattern)
        comp2 = re.compile(patternmult)

        for i in self.linhas:
            m = None

            m = comp.findall(i)
            if len(m) == 0:
                m = comp2.findall(i) # aqui deve ser colocado o pattern da multiplicação

            codigo = Codigo(m)

            self.traducao.append(codigo)

        return self.traducao