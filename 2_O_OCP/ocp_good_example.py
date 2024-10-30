from abc import ABC, abstractmethod


# Interface para Exame
class Exame(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def verifica_condicoes(self):
        pass


# Classe para Exame de Sangue
class ExameSangue(Exame):
    def __init__(self):
        super().__init__(tipo="sangue")

    def verifica_condicoes(self):
        # Implemente as condições específicas do exame de sangue
        print("Verificando condições para exame de sangue...")
        return True


# Classe para Exame de Raio-X
class ExameRaioX(Exame):
    def __init__(self):
        super().__init__(tipo="raio-x")

    def verifica_condicoes(self):
        # Implemente as condições específicas do exame de raio-x
        print("Verificando condições para exame de raio-x...")
        return True


# Classe AprovaExame que utiliza a interface Exame
class AprovaExame:
    @staticmethod
    def aprovar_solicitacao_exame(exame: Exame):
        if exame.verifica_condicoes():
            print(f"{exame.tipo.capitalize()} aprovado!")
        else:
            print(f"{exame.tipo.capitalize()} não aprovado!")


# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
