dentroN = 0
foraN = 0
for i in range(10):
    n = int(input("Digite um número: "))
    if n >= 10 and n <= 20:
        dentroN += 1
    else:
        foraN += 1
print(f"No intervalo entre 10 e 20 tem {dentroN} números, e fora tem {foraN} números.")
