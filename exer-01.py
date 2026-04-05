# Exercicio 01


print("|===================================================|")
print("|      VALIDAÇÃO DE INTERVALO NUMÉRICO (0 A 9)      |")
print("|===================================================|")

value = int(input("| >> Por favor, digite um valor: "))
print("|===================================================|")

if value >= 0 and value <= 9:
      print("|                 Valor está CORRETO                |")
else:
      print("|                Valor está INCORRETO               |")
      
print("|===================================================|")

# Exercicio 02

print("|=============================================================|")
print("|             SISTEMA DE DESCONTO EM COMPRAS                  |")
print("|=============================================================|")

purchase_value =  float(input("| >> Por favor, informe o valor total da compra: "))
discount = purchase_value * 0.20

if purchase_value > 200:
      discount_purchase_value = purchase_value - discount
      print("|=============================================================|")
      print(f"|  Parabens, voce recebeu um desconto de 20% nas suas compras |")
      print(f"| >> Valor total é de R${discount_purchase_value:.2f}       ")
      print("|=============================================================|")

print(f"| >> Valor total da compra é de R${purchase_value:.2f}")
print("|=============================================================|")


# Exercicio 03
print("|=============================================================|")
print("|                   SISTEMA DE ANÁLISE                        |")
print("|=============================================================|")

name = input("| >> Digite o nome e sobrenome do aluno: ")
print("|=============================================================|")
print("|           Informe as notas (Valores entre 0 a 10)           |")
print("|=============================================================|")
note_A = float(input("| >> Por favor, digite a 1° nota: "))
note_B = float(input("| >> Por favor, digite a 2° nota: "))
note_C = float(input("| >> Por favor, digite a 3° nota: "))


if (0 <= note_A <= 10) and (0 <= note_B <= 10) and (0 <= note_C <= 10):
    print("|=============================================================|")
    print("|           Analisando as notas e fazendo a média...          |")
    print("|=============================================================|")

    average = (note_A + note_B + note_C) / 3
    status = 0

    print(f"| >> O {name}, possue uma média de {average:.1f}")

    if average >= 7:
        status = "APROVADO   "
    elif average >= 5 and average <= 6.9:
        status = "RECUPERAÇÃO"
    else:
        status = "REPROVADO  "

    print(f"| O aluno está {status}                                    |")
else:
    print("| >> Alguma das três notas não está entre 0 a 10")

print("|=============================================================|")

# Exercicio 04

print()

print("|=============================================================|")
print("|                ESCOLHA UMA OPÇÃO ABAIXO                     |")
print("|=============================================================|")
print("| 1 - CELSIUS PARA FAHRENHEIT                                 |")
print("| 2 - FAHRENHEIT PARA CELSIUS                                 |")
print("|=============================================================|")

options_value = int(input("| >>  QUAL OPÇÃO SERIA: "))
temperature = float(input("| >>  Digite o valor da temperatura: "))
print("|=============================================================|")

if options_value == 1:
      calc_F = (temperature * 1.8) + 32
      print(f"| >> FAHRENHEIT: {calc_F:.2f}")

elif options_value == 2:
      calc_C = (temperature - 32)/1.8
      print(f"| >> CELSIUS: {calc_C:.2f}")
else:
      print(" | >> Sua escolha não reflete nenhuma das opções do menu")

print("|=============================================================|")


# Exercicio 05

print()
print("|=============================================================|")
print("|          ESCOLHA QUAL TURNO DE TRABALHO SERIA               |")
print("|=============================================================|")
print("| M - MATUTINO                                                |")
print("| O - OUTROS TURNOS                                           |")
print("|=============================================================|")

work_shift = input("| >> Qual seria a opção: ")
times_work = int(input("| >> Quantas horas trabalhadas: "))

print("|=============================================================|")
if work_shift == "M" or work_shift == "m":
    result = times_work * 45
    print(f"| >> Salário proporcional a horas trabalhadas: R${result:.2f}")
elif work_shift == "O" or work_shift == "o":
    result = times_work * 37.50
    print(f"| >> Salário proporcional a horas trabalhadas: R${result:.2f}")
else:
    print("| >> Opção escolhida invalida, por favor tente novamente!!!")
print("|=============================================================|")

# Exercicio 06


print()

print("|=============================================================|")
print("|                 GERENCIADOR DE VALORES                      |")
print("|=============================================================|")


light_value = float(input("| >> Digite o valor da conta de LUZ: R$"))
water_value = float(input("| >> Digite o valor da conta de AGUA: R$"))
cell_value = float(input("| >> Digite o valor da conta de TELEFONE: R$"))
print("| ")


salary = float(input("| >> Por favor, informe o seu salário mensal: R$"))
print("|=============================================================|")

if (salary >= 0) and (light_value >= 0) and (water_value >= 0) and (cell_value >= 0):

    all_count = light_value + water_value + cell_value

    if salary >= all_count:
        result_salary = salary - all_count
        print(
            f"| >> Parabéns, você pagou suas contas. Saldo final é de R${result_salary:.2f}"
        )
    else:
        print("| >> Salário insuficiente...")

else:
    print("| >> Não é possivel fazer o calculo das contas.")
    print("| >> Por favor, verifique os valores passados novamente...")
print("|=============================================================|")


# Exercicio 07
print()
print("|=============================================================|")
print("|              SIMULADOR DE EMPRÉSTIMO                        |")
print("|=============================================================|")
print("| ")


salary_person = float(input("| >> Por favor, informe o seu SALÁRIO MENSAL: R$"))
pendency = int(input("| >> Por favor, informe quantas PENDENCIAS você possue: "))


if pendency == 0:
      borrowing = float(input("| >> Por favor, informe o valor do EMPRESTIMO: R$"))
      parcel = int(input("| >> Por favor, informe o NUMERO DE PARCELAS:  "))

      fees = borrowing * 0.009 * parcel
      total_value = borrowing + fees
      value_fees = total_value / parcel

      print("| ")
      print("|=============================================================|")
      print(f'| >> Valor total a pagar: R$ {total_value:.2f}   ')
      print(f'| >> Valor de cada parcela: R$ {value_fees:.2f} ')
      print("|=============================================================|")

else:
      print('| >> Empréstimo Negado: Cliente possui pendências.')


# Exercicio 8

print()
print("|===========================================================|")
print("|             IMC - INDICE DE MASSA CORPORIA                |")
print("|===========================================================|")
print("| M - MASCULINO                                             |")
print("| F - FEMININO                                              |")
print("|===========================================================|")


sex = input("| >> Por favor, digite seu SEXO: ")
weight = float(input("| >> Por favor, digite o seu PESO: "))
height = float(input("| >> Por favor, digite a sua ALTURA: "))

bmi = weight / (height**2)

print("|===========================================================|")
print(f"| >> Seu IMC é: {bmi:.1f}                                   ")
print("|===========================================================|")
print("| Condição            |  IMC (FEMININO)   | IMC (MASCULINO) |")
print("|=====================|===================|=================|")
print("| Abaixo do peso      | < 19.1            | < 20.7          |")
print("| Peso normal         | 19.1 - 25.8       | < 20.7 - 26.4   |")
print("| Marginalmente acima | 25.8 - 27.3       | < 26.4 - 27.8   |")
print("| Acima do peso ideal | 27.3 - 32.3       | < 27.8 - 31.1   |")
print("| Obesidade           | > 32.3            | > 31.1          |")
print("|=====================|===================|=================|")


if (sex == 'M' or sex == 'm'):

      if bmi < 20.7:
            print("| Seu status é: ABAIXO DO PESO                              |")
      elif bmi < 26.4:
            print("| Seu status é: PESO NORMAL                                 |")
      elif bmi < 27.8:
            print("| Seu status é: MARGINALMENTE ACIMA                         |")
      elif bmi < 31.1:
            print("| Seu status é: ACIMA DO PESO IDEAL                         |")
      elif bmi > 31.1:
            print("| Seu status é: OBESO                                       |")

elif sex == 'F' or sex == 'f':
      if bmi < 19.1:
            print("| Seu status é: ABAIXO DO PESO                              |")
      elif bmi < 25.8:
            print("| Seu status é: PESO NORMAL                                 |")
      elif bmi < 27.3:
            print("| Seu status é: MARGINALMENTE ACIMA                         |")
      elif bmi < 32.3:
            print("| Seu status é: ACIMA DO PESO IDEAL                         |")
      elif bmi > 32.3:
            print("| Seu status é: OBESO                                       |")
else:
      print("Infelizmente a opção de sexo não está presente na tabela")
print("|===========================================================|")
