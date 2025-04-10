negativo = 0
for i in range(1,11):
    num = int(input("Digite um número"))
    if num<0:
        negativo += 1
print(f"Foram digitados {negativo} negativos.")