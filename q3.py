def fatorial_duplo(x):
    if x == 0 or x == 1:
        return 1

    # Caso geral: incluir apenas os números pares
    if x % 2 == 0:
        return x * fatorial_duplo(x - 2)
    else:
        return x * fatorial_duplo(x - 2)
        
print(fatorial_duplo(0)) #1
print(fatorial_duplo(1)) #1
print(fatorial_duplo(2)) #2
print(fatorial_duplo(3)) #3
print(fatorial_duplo(4)) #8
print(fatorial_duplo(5)) #8
print(fatorial_duplo(6))  #8

print(fatorial_duplo(7)) #8
