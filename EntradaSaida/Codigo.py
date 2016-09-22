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

        self.byteArray = [-1, -1, -1, -1]

        # pegando qual operação será executada
        self.byteArray[0] = ops[self.parametros[0]]

        # pegando o primeiro valor, independe da operação
        self.byteArray[1] = self.solve_value(self.parametros[1])

        # se a operação for add, mov ou imul existe o 3º parametro
        if self.byteArray[0] > ops["inc"]:
            self.byteArray[2] = self.solve_value(self.parametros[2])

            # se a operação for imul existe o 4º parametro
            if self.byteArray[0] > ops["mov"]:
                self.byteArray[3] = self.solve_value(self.parametros[3])

        return self.byteArray

    # converte o valor para posição da memória, registrador ou inteiro
    @staticmethod
    def solve_value(valor):
        retorno = None
        try:
            # tenta covnerter para inteiro
            retorno = int(valor)
            if retorno > Constantes.MAIOR_INTEIRO:
                raise MemoryError("Não é possível armazenar valores maiores que " + Constantes.MAIOR_INTEIRO)
        except ValueError:
            pass

        try:
            # tenta converter para registrador
            retorno = -ord(valor)
            if -retorno > Constantes.MAIOR_REGISTRADOR or -retorno < Constantes.MENOR_REGISTRADOR:
                raise MemoryError("Registrador inexistente")
        except TypeError:
            pass

        # converte para posição de memória
        if retorno == None:
            retorno = -int(valor, 16)
            if -retorno > Constantes.TAMANHO_MEMORIA_DADOS:
                raise MemoryError("Posição de memória inexistente")

        return retorno
