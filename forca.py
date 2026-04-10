import random as rd 

def mensagem_inicial():
    print('*--------------------*')
    print('BEM VINDO AO JOGO DE FORCA')
    print('*--------------------*')

def seleciona_palavra_aleatoria():
    arquivo = open("palavras.txt", "r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)
        
    arquivo.close
    posicao = rd.randrange(0, len(palavra))

    palavra_secreta = palavra[posicao].lower()
    return palavra_secreta 

def entrada_dados():
    chute = input('Digite uma Letra:')
    chute = chute.strip().upper()
    return chute

def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra 
            index = index + 1 
def letras_corretas():
    ["_" for letra in seleciona_palavra_aleatoria]

def jogar_forca():
    mensagem_inicial()
    palavra_secreta = seleciona_palavra_aleatoria()
   

    
    letras_acertadas = letras_acertadas(palavra_secreta)

    for letras in palavra_secreta:
        letras_acertadas.append("_")

    perdeu = False
    acertou = False
    erros = 0 


    while(not perdeu and not acertou):
        chute =  entrada_dados()
        #Index define a posição da letra
        
        if(chute in palavra_secreta):
             chute_correto(palavra_secreta, chute, letras_acertadas)

        else:
            erros = erros + 1
            acertou = "_" not in letras_acertadas


           
            perdeu = erros == 6 
        print(letras_acertadas)
        

if(__name__ == "__main__"):
    jogar_forca()