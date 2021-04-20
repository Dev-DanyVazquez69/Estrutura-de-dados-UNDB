import os
from time import sleep
class SobranSheila:
    def __init__(self):
        self.resultado = {}
        self.funcionarios =  ["Ana","João","Carlos","Beatriz","Jorje"]
        self.id = 0
        self.media = 0
    def menu(self):
        while True:
            print("-~" * 30)
            print('''
      Bem vindo a votação de funcionario do mês SobranSheila\n
      [1] Votar
      [2] Ver ranking
      [3] sair
      ''')
            print("-~" * 30)
            try:
                self.menu = int(input("=>>"))
                if self.menu == 1:
                    os.system("clear")
                    self.redirecionar()
                    os.system('clear')
                    print("✅  ✅    Voto armazenados com sucesso   ✅  ✅ ")
                elif self.menu == 2:
                    self.redirecionar()
                elif self.menu == 3:
                    os.system("clear")
                    sleep(1)
                    print(" 😍😍  obrigado por participar 😍😍 ")
                    break
                else:
                    os.system('clear')
                    print(" ⚠ ⚠ Digite 1 ou 2  ⚠ ⚠ ")
                    sleep(1)
            except:
                os.system('clear')
                print(" ⚠ ⚠ Erro, digite apenas os numeros apresentados ⚠ ⚠ ")
                sleep(1)
                pass

    def redirecionar(self):
        if self.menu == 1:
            self.perguntas()
        elif self.menu == 2:
            self.mostrar_resultado()

    def perguntas(self):
        print('''
        FUNCIONARIOS = [Ana] [João] [Carlos] [Beatriz] [Jorje]
        🛑  🛑 POR FAVOR EVITEM VOTOS IGUAIS 🛑  🛑 
        ''')
        print("-~" * 30)
        contf=0
        for s in self.funcionarios:
          self.nome = s
          while True:
            self.nota = int(input(f"Nota funcionario(a) {self.funcionarios[contf]}=>"))
            if self.nota <=10 and self.nota >=0:
              break
            print("💥 erro, digite uma nota entre 0 e 10 💥")
          print("-~" * 30)
          self.registrar()
          contf +=1
    def registrar(self):
        self.resultado[self.nota] = self.nome
    def mostrar_resultado(self):
        os.system("clear")
        if len(self.resultado)>0:
          nota = list(self.resultado.keys())
          nota.sort(reverse=True)
          cont = 1
          for x in nota:
            print("~"*10)
            print(f'{cont}°LUGAR')
            print("~"*10)
            print(f'NOME:{self.resultado[x]}\nNOTA:{x}')
            cont +=1
        else:
          print("🛑  🛑  Não há candidatos válidos  🛑  🛑")
        input("\nTecle enter para voltar")
        os.system("clear")


dany = SobranSheila()
dany.menu()
