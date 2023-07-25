'''
IMC = peso (kg) / altura² (m²)
Abaixo do peso: IMC menor que 18,5
Peso normal: IMC entre 18,5 e 24,9
Sobrepeso: IMC entre 25 e 29,9
Obesidade grau 1: IMC entre 30 e 34,9
Obesidade grau 2: IMC entre 35 e 39,9
Obesidade grau 3 (obesidade mórbida): IMC igual ou maior que 40'''
def pesoIdeal(alt_cm):
    alt_metros = alt_cm / 100
    imc_min = 20
    imc_max = 25
    p_min = imc_min * (alt_metros * alt_metros)
    p_max = imc_max * (alt_metros * alt_metros)
    print("Peso minimo: %.1f \nPeso maximo: %.1f" % (p_min, p_max))

alt_cm = float(input("Digite a altura em centímetros: "))
pesoIdeal(alt_cm)
