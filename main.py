from datetime import datetime
import os

ALTURA_MINIMA = 100

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def preencher_tela(linhas_usadas=0):
    linhas_restantes = ALTURA_MINIMA - linhas_usadas
    if linhas_restantes > 0:
        print("\n" * linhas_restantes)

def cabecalho(titulo):
    print("=" * 80)
    print(titulo.center(80))
    print("=" * 80)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Paciente(Pessoa):
    def __init__(self, nome, idade, emergencia):
        super().__init__(nome, idade)
        self.emergencia = emergencia

    def prioridade_info(self):
        if self.idade >= 60 and self.emergencia:
            return "Altissima", 3
        elif self.idade >= 60 or self.emergencia:
            return "Prioritaria", 2
        else:
            return "Normal", 1


class FilaAtendimento:
    def __init__(self):
        # nome -> (peso, prioridade_texto, horario_chegada)
        self.fila = {}

    def adicionar_paciente(self, paciente):
        prioridade_texto, peso = paciente.prioridade_info()
        horario = datetime.now()
        self.fila[paciente.nome] = (peso, prioridade_texto, horario)

        cabecalho("PACIENTE ADICIONADO")
        print(f"Nome       : {paciente.nome}")
        print(f"Prioridade : {prioridade_texto}")
        print(f"Chegada    : {horario.strftime('%H:%M:%S')}")
        preencher_tela(5)

    def chamar_proximo(self):
        limpar_tela()

        if not self.fila:
            cabecalho("ATENDIMENTO")
            print("Nenhum paciente na fila.")
            preencher_tela(3)
            return

        nome_escolhido = min(
            self.fila,
            key=lambda nome: (-self.fila[nome][0], self.fila[nome][2])
        )

        peso, prioridade_texto, horario = self.fila.pop(nome_escolhido)

        cabecalho("CHAMADA DE PACIENTE")
        print(f"Nome              : {nome_escolhido}")
        print(f"Prioridade        : {prioridade_texto}")
        print(f"Horario de chegada: {horario.strftime('%H:%M:%S')}")
        print("-" * 80)
        preencher_tela(6)

    def listar_fila(self):
        limpar_tela()
        cabecalho("FILA DE ATENDIMENTO")

        if not self.fila:
            print("Fila vazia.")
            preencher_tela(3)
            return

        linhas = 3
        for nome, (peso, prioridade, horario) in self.fila.items():
            print(f"{nome:<25} | {prioridade:<12} | {horario.strftime('%H:%M:%S')}")
            linhas += 1

        preencher_tela(linhas)


def menu():
    limpar_tela()
    cabecalho("POSTO DE SAUDE - SISTEMA DE TRIAGEM")
    print("1 - Adicionar paciente")
    print("2 - Chamar proximo paciente")
    print("3 - Listar fila")
    print("4 - Sair")
    print("-" * 80)


fila = FilaAtendimento()


while True:
    
    menu()
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome do paciente: ")
        idade = int(input("Idade do paciente: "))
        emergencia = input("Eh caso de emergencia? (s/n): ").lower() == "s"

        paciente = Paciente(nome, idade, emergencia)
        fila.adicionar_paciente(paciente)

    elif opcao == "2":
        fila.chamar_proximo()
        input("\nPressione ENTER para continuar...")

    elif opcao == "3":
        fila.listar_fila()
        input("\nPressione ENTER para continuar...")

    elif opcao == "4":
        limpar_tela()
        cabecalho("SISTEMA ENCERRADO")
        preencher_tela(5)
        break

    else:
        print("Opção inválida.")
        input("Pressione ENTER para continuar...")

print('Feito por Yuri, Otavio e Joao Victor. Com carinho.')
