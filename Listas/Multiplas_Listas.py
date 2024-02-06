equipamento = []
valor = []
numeroSerial = []
departamento = []
resposta="S"

while resposta=="S":
  equipamento.append(input("Equipamento: "))
  valor.append(float(input("Valor: ")))
  numeroSerial.append(int(input("Número Serial: ")))
  departamento.append(input("Departamento: "))
  resposta=input("Digite \"S\" para continuar: ").upper()

for equipamento in equipamento:
  print("Equipamentos: ", equipamento)