#primeiro programa
"""primeiro programa"""
print("Helo world!")

check1 = 8
check2 = 6.5
print(type(check1)) #int= valor inteiro
print(type(check2)) #float= valor decimal
print(check1+check2) #certo mas não mais usado
soma = check1+check2 #mais usual
print(soma)

#Exercicios
#1
print("Manoela de Almeida Aurelio")

nome= "Manoela de Almeida Aurelio" #outro jeito
print(nome)

print() #maneira caseira de pular uma linha no resultado final
#2
a = 3
b = 5
soma=2*a*3*b
print(soma,"\n") #\n = pular linha tbm

#3
x = 10
y = 20
z = 30
soma= x+y+z
print(soma)

print()

pi = 3.14159265
print(f"pi={pi:.2f}") #deixar apenas duas casas decimais, o F= f-string (formatando)

nome= "Manoela Aurelio"
print(type(nome)) #variavel string

print(12%3) #resto da divisao = %
print(5//2) #valor inteiro da divisão
print()

check1 = float(input("Checkpoint 1 =")) #input = usuario traz informaçao
check2 = float(input("Checkpoint 2 ="))
media = (check1+check2)/2
print(f"Media = {media:.1f}")