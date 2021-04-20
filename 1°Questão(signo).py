'''Data dos signos
21/01 a 18/02
19/02 a 20/03
21/03 a 20/04
21/04 a 20/05
21/05 a 20/06
21/06 a 22/07
23/07 a 22/08
23/08 a 22/09
23/09 a 22/10
23/10 a 21/11
22/10 a 21/11
22/11 a 21/12
21/12 a 20/01'''
import os
from time import sleep
class signo:
  def __init__(self):
    self.signo = {1:{'capricornio':20,'aquario':21},2:{'aquario':21,'peixes':22},3:{'peixes':20,'aries':21},4:{'aries':20,'touro':21},5:{'touro':20,'gemeos':21},6:{'gemeos':20,'cancer':21},7:{'cancer':22,'leão':23},8:{'leão':22,'virgem':23},9:{'virgem':22,'libra':23},10:{'libra':22,'escorpião':23},11:{'escorpião':21,'sagitario':22},12:{'sagitario':21,'capricornio':22}}
  def menu(self):
    while True:
      self.perguntas()
      self.conferir_mês()
  def perguntas(self):
    os.system("cls" or "clear")
    print("~"*40)
    self.x = int(input("Digite o dia do seu aniversario: "))
    print("~"*40)
    self.y = int(input("Digite o mês do seu aniversario: "))
    print("~"*40)
  def conferir_mês(self):
      for s in self.signo:
        if self.y == s:
          z = list(self.signo[s].values())
          q = list(self.signo[s].keys())
          if self.x <= z[0]:
            print("")
            print("*"*20)
            print(f"seu signo é {q[0]}")
            print("*"*20)
            print("")
          else:
            print("")
            print("*"*20)
            print(f"seu signo é {q[1]}")
            print("*"*20)
            print("")
        sleep(0.3)

dany = signo()
dany.menu()