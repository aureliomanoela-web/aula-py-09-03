media_final = float(input ("Média final = "))
if media_final>=6:
    print ("Aprovado)")
else:
    print("reprovado")
print()



Velocidade= int(input("Velocidade em km = "))
if Velocidade> 80:
    print("Você foi multado")
    multa= (Velocidade-80)*5
    print(f"Multa é de R${multa:.2f} ")
else:
    print("Você ama o Detran")

print()

num1= float(input("Número 1 ="))
num2= float(input("Número 2="))
num3= float(input("Número 3 ="))

maior = num1
if num2 >= num1 and num2 >=num3:
    maior = num2
if num3 >= num1 and num3 >= num2:
    maior =  num3

print(maior)

menor = num1
if num2 <= num1 and num2 <=num3:
    menor = num2
if num3 <= num1 and num3 <= num2:
    menor =  num3

print (f"O número maior é {maior}")
print (f"O número menor é {menor}")

print()

distancia =float(input ("Qual distancia você deseja percorrer?"))
if distancia <=200:
    valormenor = distancia*0.50
    print(valormenor)
else:
    valormaior= distancia*0.45
    print(valormaior)


print()

sal = float(input ("Salario = "))
if sal>1250:
    aumento= sal * 0.1
else:
    aumento = sal * 0.15
print(f"0 aumento é de R${aumento:.2f}")