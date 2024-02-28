
opcao = 0
while opcao != 5:
    num1 = int(input("digite um numero:"))
    num2 = int(input("digite outro numero:"))
    print ("1: somar")
    print ("2: multiplicar")
    print ("3: dividir")
    print ("4: diminuir")
    print ("5: sair")
    opcao = int(input("qual a opção desejada: "))
    if opcao ==1:
        soma = num1 + num2
        print(f"a soma entre{num1} e {num2} é {soma}")
    elif opcao == 2:
        multi = (num1 * num2) 
        print(f"a multiplicação entre {num1} e {num2} é a {multi}")
    elif opcao == 3:
        divi = num1 / num2
        print(f"a divisão entre {num1} e {num2} é {divi}")
    elif opcao ==4:
        dimi = num1 - num2
        print (f"a subtração entre {num1} {num2} é {dimi}")
    elif opcao ==5:
        print("finalizando...")
    else:
        print("opcao invalida")
    print("=-=" *10)
print("fim") 