from Memoria import Constantes


class Codigo:
    operacoes = {
        "inc": 1,
        "add": 2,
        "mov": 3,
        "imul": 4
    }

    def __init__(self, args):
        self.parametros = args
        self.byteArray = self.to_byte_array()

    def to_byte_array(self):
        ops = self.__class__.operacoes

        byteArray = [-1, -1, -1, -1]

        # pegando qual operacao sera executada
        byteArray[0] = ops[self.parametros[0]]

        # pegando o primeiro valor, independe da operacao
        byteArray[1] = self.solve_value(self.parametros[1])

        # se a operacao for add, mov ou imul existe o 3 parametro
        if byteArray[0] > ops["inc"]:
            byteArray[2] = self.solve_value(self.parametros[2])

            # se a operacao for imul existe o 4 parametro
            if byteArray[0] > ops["mov"]:
                byteArray[3] = self.solve_value(self.parametros[3])

        return byteArray

    # converte o valor para posicao da memoria, registrador ou inteiro
    @staticmethod
    def solve_value(valor):
        retorno = None
        try:
            # tenta covnerter para inteiro
            retorno = int(valor)
            if retorno > Constantes.MAIOR_INTEIRO:
                raise MemoryError("Nao e possivel armazenar valores maiores que " + Constantes.MAIOR_INTEIRO)
            return retorno
        except ValueError:
            pass

        try:
            # tenta converter para registrador
            retorno = -ord(valor)
            if -retorno > Constantes.MAIOR_REGISTRADOR or -retorno < Constantes.MENOR_REGISTRADOR:
                raise MemoryError("Registrador inexistente")
            return retorno
        except TypeError:
            pass

        # converte para posicao de memoria
        if retorno == None:
            retorno = -int(valor, 16)
            if -retorno > Constantes.TAMANHO_MEMORIA_DADOS:
                raise MemoryError("Posicao de memoria inexistente")
        return retorno

