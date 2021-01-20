def horasInt(x):
  x *= 100
  inteiro = x // 100
  resto = (x % 100) / 100
  resto = (resto * 10) / 6
  x = inteiro + resto
  return x

soma = 0
qtdclientes = int(input("Digite a quantidade de funcionários: "))
while qtdclientes > 0:
  nome = input("Digite o nome do funcionário: ")
  salario = float(input("Digite o valor do honorário: "))
  dias = int(input("Digite a quantidade de dias úteis no mês: "))
  domingos = int(input("Digite a quantidade de domingos do mês: "))
  HE60 = float(input("Digite a quantidade de horas extra 60%: "))
  HE60 = horasInt(HE60)
  HE80 = horasInt(float(input("Digite a quantidade de horas extra 80%: ")))
  HE100 = horasInt(float(input("Digite a quantidade de horas extra 100%: ")))
  atraso = horasInt(float(input("Digite a quantidade de horas de atraso: ")))
  
  reaisPorHora = salario / 220
  VE60 = (reaisPorHora * 1.6) * HE60
  VE80= (reaisPorHora * 1.8) * HE80
  VE100 = (reaisPorHora * 2) * HE100
  
  DSR = ((VE60 + VE80 + VE100) / dias) * domingos
  
  VAtraso = reaisPorHora * atraso
  
  tFloat = salario + VE60 + VE80 + VE100 + DSR - VAtraso
  tResto = int((tFloat % 1) * 100) / 100
  total = int(tFloat) + tResto
  
  print()
  print("O valor total do salário de ", nome, ", com horas extras e atrasos, é de: R$", total)
  print()

  soma += total
  qtdclientes -= 1

print("O valor total a ser pago é R$", soma)
  
  
  
  
