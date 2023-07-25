num = int(input("Informe um numero: "))
if num % 1 == 0 and num % num == 0 and num % 2 != 0:
    if num == 1:
        print("Não é primo")
    else:
        print("É primo")
else:
    print("Não é primo")

