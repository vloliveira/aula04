soma = 0
quant = int(input("Digite quantos números deseja colocar: "))
for i in range (quant):
    num = float(input("DIgite um número: "))
    soma+=num
media = soma/quant
print(media)