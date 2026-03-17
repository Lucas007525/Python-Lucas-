#calculadora simples em python, cada operação é colocada como 1, 2, 3 e 4 identificando a operação.
operacao = int(input("1- Multiplicação 2-Divisão 3-Adição 4-Subtração:"))
numero2 = int(input("Segundo número"))
# um int define as operações e o outro define o outro número que vai ser usado.
if (operacao = 1):
    resultado = numero1 * numero2
elif (operacao = 2):
    resultado = numero1 / numero2
elif (operacao = 3):
    resultado = numero1 + numero2
elif (operacao = 4):
    resultado = numero1 - numero2
        #acima foi usado elif para armazenar a forma de como vai ser feita a operação.
print(resultado)
def verificar_par_ou_impar(numero):
     if numero % 1 != 0:
            return f"O resultado {numero} é um decimal (não é classificado como par ou ímpar)."
 if numero % 2 == 0:
        return f"O resultado {int(numero)} é PAR."
    else:
        return f"O resultado {int(numero)} é ÍMPAR."
# (numero % 1 != 0) verifica se o número é inteiro ou não.
# (numero % 2 == 0) essa parte é usada de forma que se o restante do número for zero o número é par.
# se não for zero ele é classificado como ímpar.
if type(numero, str):
    print("ta errado, precisa ser numero")
    