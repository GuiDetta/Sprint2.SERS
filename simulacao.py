preco_base = 1.40

tabela = []
tabela.append([6, 1, 16, 0])
tabela.append([7, 3, 17, 1])
tabela.append([8, 5, 19, 1])
tabela.append([9, 7, 22, 2])
tabela.append([10, 9, 25, 2])
tabela.append([11, 11, 28, 3])
tabela.append([12, 12, 30, 5])
tabela.append([13, 11, 31, 5])
tabela.append([14, 9, 31, 3])
tabela.append([15, 7, 30, 2])
tabela.append([16, 4, 28, 2])
tabela.append([17, 2, 26, 4])
tabela.append([18, 0, 24, 6])
tabela.append([19, 0, 22, 6])
tabela.append([20, 0, 21, 5])
tabela.append([21, 0, 20, 3])
tabela.append([22, 0, 19, 1])

print("ChargeGrid Intelligence - Preco da recarga")
print("Dados simulados")
print("")

print("Dia tipico simulado (hora, sol, temperatura, carros):")
for linha in tabela:
    print("Hora", linha[0], "| Sol", linha[1], "kW | Temp", linha[2], "C | Carros", linha[3])
print("")
print("Dados input")
print("")
hora = int(input("Hora do dia (0 a 23): "))
ceu = input("Ceu (ensolarado, parcial, nublado): ")
temp = float(input("Temperatura em graus: "))
carros = int(input("Carros carregando agora (0 a 6): "))
potencia = float(input("Potencia de recarga em kW (ex 3.4, 7, 11): "))
capacidade = float(input("Capacidade da bateria do carro em kWh (ex 50): "))
bateria = float(input("Bateria do carro agora em %: "))
meta = float(input("Carregar ate quantos %: "))
bateria_loja = float(input("Bateria da loja disponivel em kWh (ex 10): "))
cliente = input("E cliente da loja? (sim/nao): ")

solar = 0
for linha in tabela:
    if linha[0] == hora:
        solar = linha[1]

if ceu == "parcial":
    solar = solar * 0.6
if ceu == "nublado":
    solar = solar * 0.25

if temp > 35:
    solar = solar * 0.8
if temp > 30 and temp <= 35:
    solar = solar * 0.9
if temp < 15:
    solar = solar * 1.05

energia = capacidade * (meta - bateria) / 100
tempo = energia / potencia

preco = preco_base

if hora >= 18 and hora <= 20:
    preco = preco + 0.50
if hora >= 6 and hora <= 9:
    preco = preco - 0.10

if solar >= 6:
    preco = preco - 0.40
if solar >= 1 and solar < 6:
    preco = preco - 0.15

if carros >= 5:
    preco = preco + 0.30
if carros == 4:
    preco = preco + 0.20
if carros <= 1:
    preco = preco - 0.10

if potencia >= 11:
    preco = preco + 0.20

usou_bateria_loja = "nao"
if hora >= 18 and hora <= 20 and bateria_loja >= energia:
    preco = preco - 0.30
    usou_bateria_loja = "sim"

if cliente == "sim":
    preco = preco - 0.15

total = energia * preco

print("")
print("Geracao solar nessa hora:", round(solar, 1), "kW")
print("Energia necessaria:", round(energia, 1), "kWh")
print("Tempo de recarga:", round(tempo, 1), "horas")
print("Usou bateria da loja no pico:", usou_bateria_loja)
print("Preco da recarga: R$", round(preco, 2), "por kWh")
print("Total a pagar: R$", round(total, 2))
