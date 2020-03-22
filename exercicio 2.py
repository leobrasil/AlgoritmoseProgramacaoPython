#Reescreva o programa que leia três números inteiros e encontra o menor deles, 
# agora usando if-elif-else

num1 = int(input("escreva um numero inteiro: "))
num2 = int(input("escreva um numero inteiro: "))
num3 = int(input("escreva um numero inteiro: "))

if num1>num2 and num2>num3:
    print("num3 menor numero")
elif num1>num3 and num3>num2:
    print("num2 menor numero")
elif num1>num2 and num3>num2:
    print("num2 menor numero")
else:
    print("num1 menor numero")


