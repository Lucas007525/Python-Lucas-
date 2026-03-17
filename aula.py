# Importa a biblioteca 'random' para gerar números aleatórios e 'string' para acessar conjuntos de caracteres
import random
import string

# Função que gera uma senha aleatória com o comprimento especificado
def gerar_senha(tamanho):
    # 'random.choices' escolhe aleatoriamente 'k' caracteres de uma string que contém letras (maiúsculas e minúsculas) e dígitos
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

# Define o número total de rodadas
total = 5

# Inicializa a variável 'mao_bot' (não utilizada no momento, mas pode ser útil em lógica futura)
mao_bot = 0

# Inicializa a variável que vai controlar o número da rodada
turno = 1

# Inicia o loop 'while', que continuará até que o número de rodadas atinja o total
while turno <= total:
    # Exibe qual rodada está sendo executada, com a contagem total de rodadas
    print(f"Rodada {turno} de {total}")
    
    # Chama a função 'gerar_senha' para gerar uma senha aleatória de 8 caracteres
    senha = gerar_senha(8)
    
    # Exibe a senha gerada para o usuário (geralmente, senhas aleatórias são ocultadas, mas aqui é só para demonstração)
    print(f"A senha gerada é: {senha}")
    
    # Incrementa a variável 'turno' para passar para a próxima rodada
    turno += 1
    # Diferença entre o loop 'for' e o loop 'while':
# - 'for' é ideal quando você sabe o número de iterações antes de começar o loop.
#   Ele é usado para iterar sobre uma sequência ou intervalo fixo de números.
#   Exemplo: Loop que percorre de 1 até 5.
# 
# - 'while' é usado quando o número de iterações não é conhecido e você quer que o loop continue
#   enquanto uma condição for verdadeira. É importante garantir que a condição de parada seja atingida
#   para evitar um loop infinito.
#   Exemplo: Loop que continua enquanto uma variável for menor ou igual a 5.