while True:
    print("Escolha a opção que deseja utilizar:")
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potência\n6 - Raiz Quadrada\n7 - Fatorial")

    opcao = int(input("Digite a opção desejada: "))

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    match opcao:
        case 1:
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
            print("Deseja realizar outra operação? (s/n)")
            if input().lower() != 's':
                    print("Desligando...")
                    break
        case 2:
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
            print("Deseja realizar outra operação? (s/n)")
            if input().lower() != 's':
                    print("Desligando...")
                    break
        case 3:
            resultado = num1 * num2
            print(f"{num1} x {num2} = {resultado}")
            print("Deseja realizar outra operação? (s/n)")
            if input().lower() != 's':
                    print("Desligando...")
                    break
        case 4:
            if num2 == 0:
                print("Erro - Divisão por zero não é permitido.")
            else:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
                print("Deseja realizar outra operação? (s/n)")
            if input().lower() != 's':
                    print("Desligando...")
                    break
        case 5:
            resultado = num1 ** num2
            print(f"{num1} ^ {num2} = {resultado}")
            print("Deseja realizar outra operação? (s/n)")
            if input().lower() != 's':
                    print("Desligando...")
                    break
        case 6:
            if num1 < 0:
                print("Erro - Raiz quadrada de número negativo não é permitido.")
            else:
                resultado = num1 ** 0.5
                print(f"Raiz quadrada de {num1} = {resultado}")
                print("Deseja realizar outra operação? (s/n)")
            if input().lower() != 's':
                    print("Desligando...")
                    break
        case 7:
            if num1 < 0:
                print("Erro - Fatorial de número negativo não é permitido.")
            else:
                fatorial = 1
                for i in range(1, int(num1) + 1):
                    fatorial *= i

                print(f"Fatorial de {int(num1)} = {fatorial}")
                print("Deseja reaizar outra operação? (s/n)")
                if input().lower() != 's':

                    print("Desligando...")
                    break
        case _:
               print("Opção inválida. Tente novamente.")

               continue 

