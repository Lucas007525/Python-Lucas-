def verificar_par_ou_impar(numero):
    """
    Esta função recebe o resultado de um cálculo e decide sua categoria.
    """
    # 1. Verificação de número decimal:
    # O operador % 1 retorna o que sobra da divisão por 1 (os decimais).
    # Exemplo: 5.5 % 1 = 0.5. Se for diferente de 0, não é um inteiro puro.
    if numero % 1 != 0:
        return f"O resultado {numero} é um decimal (não é classificado como par ou ímpar)."

    # 2. Verificação de Par ou Ímpar:
    # Se o resto da divisão por 2 for zero, o número é par.
    if numero % 2 == 0:
        return f"O resultado {int(numero)} é PAR."
    else:
        return f"O resultado {int(numero)} é ÍMPAR."

def main():
    print("=== ESTUDO DE LOOP E EVAL EM PYTHON ===")
    print("Instruções: Digite uma conta (ex: 5*2) ou 'sair' para parar.")

    # 3. O Loop Infinito (while True):
    # Ele manterá o programa rodando repetidamente até encontrar um 'break'.
    while True:
        # Captura a entrada e remove espaços extras com .strip()
        entrada = input("\nO que deseja calcular? ").strip().lower()

        # 4. Condição de Saída:
        # Verificamos logo no início se o usuário quer encerrar.
        if entrada == 'sair':
            print("Encerrando o loop de estudos. Até a próxima!")
            break 

        # 5. Bloco de Tratamento de Erros (try/except):
        # Usamos isso para que o programa não "trave" se o usuário digitar bobagem.
        try:
            # O 'eval' interpreta a string como uma expressão matemática real.
            # Ele transforma o texto "10 / 2" no número 5.0.
            resultado_calculo = eval(entrada)
            
            # Mostra o valor calculado
            print(f"Calculando... {entrada} = {resultado_calculo}")
            
            # 6. Integração:
            # Passamos o resultado do eval para a nossa função de verificação.
            mensagem = verificar_par_ou_impar(resultado_calculo)
            print(mensagem)

        except ZeroDivisionError:
            # Erro específico para quando alguém tenta dividir por zero.
            print("Erro: Não existe divisão por zero na matemática!")
            
        except Exception as erro:
            # Captura qualquer outro erro (como letras ou símbolos inválidos).
            print(f"Ops! Algo deu errado: {erro}")
            print("Dica: Digite apenas números e operadores (+, -, *, /).")

# Ponto de entrada do script
if __name__ == "__main__":
    main()