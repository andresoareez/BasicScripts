from replit import clear
from art import logo
print(logo)

apostas = {}
leilao_finalizado = False

def procurar_maior_aposta(apostas_gravadas):
  maioraposta = 0
  vencedor = ''
  for apostador in apostas_gravadas:
    apostatotal = apostas_gravadas[apostador]
    if apostatotal > maioraposta:
      maioraposta = apostatotal
      vencedor = apostador
  print(f"O ganhador é {vencedor} com uma aposta de R$ {maioraposta}")

while not leilao_finalizado:
  nome = input('Qual o seu name?')
  aposta = int(input('Qual sua aposta?'))
  apostas[nome] = aposta

  continuar_leilao = input("Existe mais algum apostador? Escreva 'Sim ou 'Não'?")
  if continuar_leilao == "Não":
    leilao_finalizado = True
    procurar_maior_aposta(apostas)
  elif continuar_leilao == 'Sim':
    clear()